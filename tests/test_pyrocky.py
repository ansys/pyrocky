# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
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
from ansys.rocky.core.client import DEFAULT_SERVER_PORT
from ansys.rocky.core.launcher import RockyLaunchError
from ansys.rocky.core.rocky_api_proxies import ApiExportToolkitProxy

if os.getenv("ANSYS_VERSION"):
    VERSION = int(os.getenv("ANSYS_VERSION"))
else:
    raise EnvironmentError("No ANSYS_VERSION environment variable set.")

FREEFLOW_VERSION = 251


@pytest.fixture()
def rocky_session():
    rocky = pyrocky.launch_rocky(rocky_version=VERSION)
    yield rocky
    rocky.close()


@pytest.fixture()
def freeflow_session():
    freeflow = pyrocky.launch_freeflow(freeflow_version=FREEFLOW_VERSION)
    yield freeflow
    freeflow.close()


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


def test_not_supported_version_error():
    with pytest.raises(ValueError, match=f"Rocky version 222 is not supported.*"):
        pyrocky.launch_rocky(rocky_version=222)


def test_freeflow_not_supported_version_error():
    with pytest.raises(
        ValueError, match=f"Freeflow version 222 is not supported.*"
    ):
        pyrocky.launch_freeflow(freeflow_version=222)


def test_rocky_exe_parameter():
    from ansys.rocky.core.client import RockyClient

    exe_file = "C:\\Program Files\\ANSYS Inc\\v251\\Rocky\\bin\\Rocky.exe"
    rocky = pyrocky.launch_rocky(rocky_exe=exe_file)

    assert isinstance(rocky, RockyClient)

    rocky.close()


def test_invalid_rocky_exe_parameter():
    with pytest.raises(FileNotFoundError, match=f"Rocky executable is not found at*"):
        pyrocky.launch_rocky(rocky_exe="C:\\Folder\\Rocky.exe")


def test_minimal_simulation(tmp_path, request):
    """Minimal test to be run with all the supported Rocky version to ensure
    minimal backwards compatibility.
    """
    rocky = pyrocky.launch_rocky(rocky_version=VERSION)
    request.addfinalizer(rocky.close)

    from ansys.rocky.core.client import _ROCKY_API, _get_numerical_version

    ROCKY_VERSION = _get_numerical_version(_ROCKY_API)
    assert ROCKY_VERSION == VERSION

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
    project = rocky_session.api.CreateProject()

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
    study = create_basic_project_with_results(
        rocky_session.api,
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
            pyrocky.launch_rocky(rocky_version=VERSION)


def test_close_existing_session():
    """
    Launches a pyrocky session on top another one using the
    same server port. PyRocky should attempt closing the
    existing session before launching the second one.
    """
    from ansys.rocky.core.client import _get_numerical_version

    rocky_one = pyrocky.launch_rocky(rocky_version=VERSION)
    rocky_two = pyrocky.launch_rocky(rocky_version=VERSION, close_existing=True)

    assert _get_numerical_version(rocky_two.api) is not None

    rocky_two.close()


def test_close_freeflow_existing_session():
    """
    Launches a freeflow session on top another one using the
    same server port. PyRocky should attempt closing the
    existing session before launching the second one.
    """
    from ansys.rocky.core.client import _get_numerical_version

    pyrocky.launch_freeflow(freeflow_version=FREEFLOW_VERSION)
    freeflow_two = pyrocky.launch_freeflow(
        freeflow_version=FREEFLOW_VERSION, close_existing=True
    )

    assert _get_numerical_version(freeflow_two.api) is not None

    freeflow_two.close()


def test_freeflow_launcher(freeflow_session):
    """Test to check if freeflow launcher is working as expected"""
    project = freeflow_session.api.CreateProject()

    study = project.GetStudy()

    inlets_outlets = study.GetInletsOutletsCollection()
    inlet = inlets_outlets.AddVolumetricInlet()
    inlet.SetName("Inlet1")

    # Test __len__
    assert len(inlets_outlets) == 1
    # Test __getitem__
    assert inlets_outlets[0].GetName() == "Inlet1"


def test_freeflow_launcher_with_specified_version(request):
    """Test to check if freeflow launcher works when a version is specified"""
    freeflow = pyrocky.launch_freeflow(freeflow_version=FREEFLOW_VERSION)
    request.addfinalizer(freeflow.close)

    from ansys.rocky.core.client import _ROCKY_API, _get_numerical_version

    ROCKY_VERSION = _get_numerical_version(_ROCKY_API)
    assert ROCKY_VERSION == FREEFLOW_VERSION


def test_no_valid_local_winreg_exe():
    with pytest.raises(FileNotFoundError, match=f"Local executable not found for*"):
        pyrocky.launch_rocky(rocky_version=900)
