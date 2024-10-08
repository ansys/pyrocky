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
import pytest

import ansys.rocky.core as pyrocky
from ansys.rocky.core.client import DEFAULT_SERVER_PORT
from ansys.rocky.core.launcher import RockyLaunchError
from ansys.rocky.core.rocky_api_proxies import ApiExportToolkitProxy


@pytest.fixture()
def rocky_session():
    rocky = pyrocky.launch_rocky()
    yield rocky
    rocky.close()


def create_basic_project_with_results(
    rocky_api,
    project_filename,
    simulation_duration: float = 2,
    time_interval: float = 0.25,
):
    """Helper to create a basic scenario. Returns the study proxy."""
    project = rocky_api.CreateProject()
    assert project, "No project created"

    study = project.GetStudy()
    particle = study.CreateParticle()

    inlet_surface = study.CreateCircularSurface()
    study.CreateParticleInlet(entry_point=inlet_surface, particle=particle)

    domain = study.GetDomainSettings()
    domain.DisableUseBoundaryLimits()
    domain.SetCoordinateLimitsMaxValues((10, 1, 10))

    solver = study.GetSolver()
    solver.SetSimulationDuration(simulation_duration)
    solver.SetTimeInterval(time_interval, "s")

    project.SaveProject(project_filename)
    study.StartSimulation()
    return study


@pytest.mark.parametrize(
    "version, expected_version",
    [
        ("25.1", 251),
        ("24.2", 240),
    ],
)
def test_minimal_simulation(version, expected_version, tmp_path, request):
    """Minimal test to be run with all the supported Rocky version to ensure
    minimal backwards compatibility.
    """
    short_v = version.replace(".", "")
    exe_file = f"C:\\Program Files\\ANSYS Inc\\v{short_v}\\Rocky\\bin\\Rocky.exe"
    pyrocky.launch_rocky(exe_file)
    rocky = pyrocky.connect_to_rocky()
    request.addfinalizer(rocky.close)

    from ansys.rocky.core.client import _ROCKY_VERSION

    global _ROCKY_VERSION
    assert _ROCKY_VERSION == expected_version

    study = create_basic_project_with_results(
        rocky.api, str(tmp_path / "rocky-testing.rocky")
    )

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


def test_export_toolkit(rocky_session, tmp_path):
    rocky = pyrocky.connect_to_rocky()
    study = create_basic_project_with_results(
        rocky.api,
        str(tmp_path / "rocky-testing-export.rocky"),
        simulation_duration=0.1,
        time_interval=0.1,
    )

    export_toolkit = study.GetExportToolkit()
    assert isinstance(export_toolkit, ApiExportToolkitProxy)

    stl_to_save = str(tmp_path / "particles_as_stl.stl")
    export_toolkit.ExportParticleToStl(stl_to_save, "Particle <01>")


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


def test_close_existing_session():
    """
    Launches a pyrocky session on top another one using the
    same server port. PyRocky should attempt closing the
    existing session before launching the second one.
    """
    from ansys.rocky.core.client import _get_numerical_version

    rocky_one = pyrocky.launch_rocky()
    rocky_two = pyrocky.launch_rocky(close_existing=True)

    assert _get_numerical_version(rocky_two.api) is not None

    rocky_two.close()
