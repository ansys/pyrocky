# Copyright (C) 2023 - 2026 ANSYS, Inc. and/or its affiliates.
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

import sys

from ansys.rocky.core.rocky_api_proxies import ApiExportToolkitProxy


def test_minimal_simulation(rocky_api, version, tmp_path):
    """Minimal test to be run with all the supported Rocky version to ensure
    minimal backwards compatibility.
    """
    study = create_basic_project_with_results(
        rocky_api, str(tmp_path / "rocky-testing.rocky")
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


def test_sequences_interface(rocky_api):
    """Ensure that API objects that are sequences have their dunder methods exposed."""
    project = rocky_api.CreateProject()

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


def test_export_toolkit(rocky_api, version, tmp_path):
    study = create_basic_project_with_results(
        rocky_api,
        str(tmp_path / "rocky-testing-export.rocky"),
        simulation_duration=0.1,
        time_interval=0.1,
    )

    export_toolkit = study.GetExportToolkit()
    assert isinstance(export_toolkit, ApiExportToolkitProxy)

    stl_to_save = str(tmp_path / "particles_as_stl.stl")
    export_toolkit.ExportParticleToStl(stl_to_save, "Particle <01>")


def test_pyro_excepthook_installed(rocky_api, capsys) -> None:
    """Test that the pyro exception hook that shows remote traceback is installed."""
    project = rocky_api.CreateProject()
    study = project.GetStudy()

    try:
        study.UnknownMethod()
    except AttributeError:
        # We must call excepthook explicitly because pytest handles exceptions internally.
        sys.excepthook(*sys.exc_info())

    out_err = capsys.readouterr()
    assert (
        "AttributeError: 'RAStudy' object has no attribute 'UnknownMethod'" in out_err.err
    )
    assert "Remote traceback" in out_err.err


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
