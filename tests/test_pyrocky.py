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
from functools import partial
import os
import time

from Pyro5.errors import CommunicationError
import pytest

import ansys.rocky.core as pyrocky
from ansys.rocky.core.client import DEFAULT_SERVER_PORT
from ansys.rocky.core.exceptions import PyRockyError, RockyLaunchError
from ansys.rocky.core.launcher import _CONNECT_TO_SERVER_TIMEOUT, _find_executable
from ansys.rocky.core.rocky_api_proxies import ApiExportToolkitProxy

VERSION = int(os.getenv("ANSYS_VERSION", "252"))

def close_pyro_session(client):
    """Closes the supplied Pyro client. Raise a "PyRockyError" if it is not possible to
    close the client within the expected time."""
    session_uri = client.api._pyroUri
    now = time.time()
    while (time.time() - now) < _CONNECT_TO_SERVER_TIMEOUT:
        try:
            client.close()
            time.sleep(1)
        except CommunicationError:
            break
    else:
        raise PyRockyError(f"Unable to close the Pyro session: {session_uri}")


@pytest.fixture()
def rocky_session(rocky_version):
    """Launch a Rocky session."""
    rocky = pyrocky.launch_rocky(rocky_version=rocky_version)
    yield rocky
    close_pyro_session(rocky)


@pytest.fixture()
def freeflow_session(freeflow_version):
    """Launch a FreeFlow session."""
    freeflow = pyrocky.launch_freeflow(freeflow_version=freeflow_version)
    yield freeflow
    close_pyro_session(freeflow)


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


def test_rocky_exe_parameter(request, rocky_version):
    from ansys.rocky.core.client import RockyClient

    rocky_exe = _find_executable("Rocky", rocky_version)

    rocky = pyrocky.launch_rocky(rocky_exe)
    request.addfinalizer(partial(close_pyro_session, rocky))

    assert isinstance(rocky, RockyClient)


def test_invalid_rocky_exe_parameter():
    import tempfile

    with pytest.raises(FileNotFoundError, match="Rocky executable is not found."):
        pyrocky.launch_rocky(
            rocky_exe=os.path.join(tempfile.gettempdir(), "invalid_rocky_exe")
        )


def test_minimal_simulation(rocky_session, tmp_path, rocky_version):
    """Minimal test to be run with all the supported Rocky version to ensure
    minimal backwards compatibility.
    """
    from ansys.rocky.core.client import _ROCKY_API, _get_numerical_version

    if rocky_version < 251:
        expected_rocky_version = 240
    else:
        expected_rocky_version = rocky_version

    obtained_rocky_version = _get_numerical_version(_ROCKY_API)
    assert obtained_rocky_version == expected_rocky_version

    study = create_basic_project_with_results(
        rocky_session.api, str(tmp_path / "rocky-testing.rocky")
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


def test_sequences_interface(rocky_session, rocky_version):
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


def test_export_toolkit(rocky_session, tmp_path, rocky_version):
    if rocky_version < 251:
        pytest.skip("PyRocky support for RAExportToolkit was added in 2025R1.")

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


def test_pyrocky_launch_multiple_servers(request, rocky_version):
    """
    Test that start multiple rocky servers is not allowed.
    """
    rocky = pyrocky.launch_rocky(rocky_version=rocky_version)
    request.addfinalizer(partial(close_pyro_session, rocky))

    with pytest.raises(RockyLaunchError, match=r"Port \d+ is already in use"):
        pyrocky.launch_rocky(rocky_version=rocky_version)


def test_close_existing_session(request, rocky_version):
    """
    Launches a pyrocky session on top another one using the
    same server port. PyRocky should attempt closing the
    existing session before launching the second one.
    """
    from ansys.rocky.core.client import _get_numerical_version

    pyrocky.launch_rocky(rocky_version=rocky_version)

    rocky_two = pyrocky.launch_rocky(rocky_version=rocky_version, close_existing=True)
    request.addfinalizer(partial(close_pyro_session, rocky_two))

    assert _get_numerical_version(rocky_two.api) is not None


def test_invalid_rocky_version():
    with pytest.raises(FileNotFoundError, match=f"Local executable is not found*"):
        pyrocky.launch_rocky(rocky_version=900)


def test_close_freeflow_existing_session(request, freeflow_version):
    """
    Launches a freeflow session on top another one using the
    same server port. PyRocky should attempt closing the
    existing session before launching the second one.
    """
    from ansys.rocky.core.client import _get_numerical_version

    pyrocky.launch_freeflow(freeflow_version=freeflow_version)

    freeflow_two = pyrocky.launch_freeflow(
        freeflow_version=freeflow_version, close_existing=True
    )
    request.addfinalizer(partial(close_pyro_session, freeflow_two))

    assert _get_numerical_version(freeflow_two.api) is not None


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


def test_freeflow_launcher_with_specified_version(freeflow_session, freeflow_version):
    """Test to check if freeflow launcher works when a version is specified"""
    from ansys.rocky.core.client import _ROCKY_API, _get_numerical_version

    if freeflow_version < 251:
        expected_freeflow_version = 240
    else:
        expected_freeflow_version = freeflow_version

    obtained_freeflow_version = _get_numerical_version(_ROCKY_API)
    assert obtained_freeflow_version == expected_freeflow_version


def test_invalid_rocky_version():
    with pytest.raises(FileNotFoundError, match=f"Local executable is not found*"):
        pyrocky.launch_rocky(rocky_version=900)


def test_connection_check(request, monkeypatch):
    """Test if the connection check works as expected."""
    from ansys.rocky.core import client

    with pytest.raises(
        PyRockyError, match="Could not connect to the remote server: timed out"
    ):
        with monkeypatch.context() as m:
            m.setattr(client, "_CONNECT_TO_SERVER_TIMEOUT", 0)
            pyrocky.launch_rocky(server_port=DEFAULT_SERVER_PORT)

    cli = pyrocky.connect(port=DEFAULT_SERVER_PORT)
    request.addfinalizer(cli.close)

    assert cli.api._pyroConnection
    assert cli.api.CreateProject()
    assert cli.api.CloseProject(check_save_state=False) is None


def test_freeflow_not_supported_version_error():
    with pytest.raises(ValueError, match=f"FreeFlow version 222 is not supported.*"):
        pyrocky.launch_freeflow(freeflow_version=222)
