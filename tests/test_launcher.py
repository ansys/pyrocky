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
import time

import pytest

import ansys.rocky.core as pyrocky
from ansys.rocky.core.client import PYROCKY_DEFAULT_PORT
from ansys.rocky.core.exceptions import NotSupportedError
from ansys.rocky.core.launcher import LaunchError, _wait_for


def test_not_supported_version_error():
    with pytest.raises(NotSupportedError, match=f"Rocky version 222 is not supported.*"):
        pyrocky.launch_rocky(rocky_version=222)


def test_invalid_rocky_exe_parameter():
    with pytest.raises(FileNotFoundError, match=f"Rocky executable is not found."):
        pyrocky.launch_rocky(rocky_exe="C:\\Folder\\Rocky.exe")


def test_pyrocky_launch_multiple_servers(version):
    """
    Test that start multiple rocky servers is not allowed.
    """
    import socket

    # Emulating Rocky server already running by binding socket to the server address.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        time.sleep(1)  # Wait to ensure the address is properly released before binding
        s.bind(("localhost", PYROCKY_DEFAULT_PORT))
        s.listen(10)

        with pytest.raises(LaunchError, match=r"Port \d+ is already in use"):
            pyrocky.launch_rocky(rocky_version=version)


def test_launcher_closing_existing_session(version):
    """
    Launches a pyrocky session on top another one using the
    same server port. PyRocky should attempt closing the
    existing session before launching the second one.
    """
    from ansys.rocky.core.client import _get_numerical_version

    pyrocky.launch_rocky(rocky_version=version)
    rocky_two = pyrocky.launch_rocky(rocky_version=version, close_existing=True)

    assert _get_numerical_version(rocky_two.api) is not None

    rocky_two.close()


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


def test_connection_timeout(request):
    """
    Test if the connection check works as expected:
    - Raises ConnectionRefusedError after the configured connect_timeout
    - Can connect after that.
    """
    with pytest.raises(LaunchError, match="Port \d+ is already in use"):
        pyrocky.launch_rocky(connect_timeout=1)

    cli = _wait_for(pyrocky.connect, timeout=30, expected_exc=ConnectionRefusedError)
    request.addfinalizer(cli.close)

    assert cli.api._pyroConnection
    assert cli.api.GetVersion() is not None
