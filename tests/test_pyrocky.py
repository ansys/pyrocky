# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os

import pytest

import ansys.rocky.core as pyrocky
from ansys.rocky.core.client import _ROCKY_VERSION, DEFAULT_SERVER_PORT
from ansys.rocky.core.launcher import RockyLaunchError


@pytest.fixture()
def rocky_session():
    rocky = pyrocky.launch_rocky()
    yield rocky
    rocky.close()


def test_minimal_simulation(rocky_session, tmp_path):
    rocky = pyrocky.connect_to_rocky()
    project = rocky.api.CreateProject()
    assert project, "No project created"

    study = project.GetStudy()
    particle = study.CreateParticle()

    inlet_surface = study.CreateCircularSurface()
    study.CreateParticleInlet(entry_point=inlet_surface, particle=particle)

    domain = study.GetDomainSettings()
    domain.DisableUseBoundaryLimits()
    domain.SetCoordinateLimitsMaxValues((10, 1, 10))

    solver = study.GetSolver()
    solver.SetSimulationDuration(2)  # Simulate for 2 sec.

    project.SaveProject(str(tmp_path / "rocky-testing.rocky"))
    study.StartSimulation()

    seconds = study.GetTimeSet()
    assert seconds[-1] > 1.75

    particles = study.GetParticles()
    particles_count = particles.GetNumpyCurve("Particles Count")
    # Just check that simulation results are at a reasonable ballpark
    assert particles_count[1][-1] > 20, "Too few particles generated"

    pid_gf = particles.GetGridFunction("Particle ID")
    pid_values = pid_gf.GetArray(time_step=-1)
    assert any(pid_values), "Particle ID should not be a zero-array"
    assert len(pid_values) > 20, "Too few values for the grid function"

    global _ROCKY_VERSION
    awp_roots = sorted(
        [k for k in os.environ.keys() if k.startswith("AWP_ROOT")], reverse=True
    )
    assert False, f"cur_version: {_ROCKY_VERSION}, all_versions: {awp_roots}"


def test_sequences_interface(rocky_session):
    """Ensure that API objects that are sequences have their dunder methods exposed."""
    rocky = pyrocky.connect_to_rocky()
    project = rocky.api.CreateProject()

    study = project.GetStudy()

    inlets_outlets = study.GetInletsOutletsCollection()
    inlet = inlets_outlets.AddParticleInlet()
    inlet.SetName("Inlet1")
    inlet = inlets_outlets.AddVolumetricInlet()
    inlet.SetName("Inlet2")

    # Test __len__
    assert len(inlets_outlets) == 2
    # Test __getitem__
    assert inlets_outlets[1].GetName() == "Inlet2"
    # Test __iter__
    assert {e.GetName() for e in inlets_outlets} == {"Inlet1", "Inlet2"}
    # Test __del__
    del inlets_outlets[0]
    assert {e.GetName() for e in inlets_outlets} == {"Inlet2"}


def test_pyrocky_launch_multiple_servers():
    """
    Test that start multiple rocky servers is not allowed.
    """
    import socket

    # Emulating Rocky server already running by binding socket to the server address.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", DEFAULT_SERVER_PORT))
        s.listen(10)

        with pytest.raises(RockyLaunchError, match=r"Port \d+ is already in use"):
            pyrocky.launch_rocky()
