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
"""Module that exposes functions to launch a Rocky application session."""
import contextlib
from pathlib import Path
import subprocess
import time

from Pyro5.errors import CommunicationError
from ansys.tools.path import get_available_ansys_installations

from ansys.rocky.core.client import DEFAULT_SERVER_PORT, RockyClient, connect_to_rocky
from ansys.rocky.core.exceptions import RockyLaunchError

_CONNECT_TO_SERVER_TIMEOUT = 60
MINIMUM_ANSYS_VERSION_SUPPORTED = 242


def launch_rocky(
    rocky_version: str | int = None,
    *,
    headless: bool = True,
    server_port: int = DEFAULT_SERVER_PORT,
    close_existing: bool = False,
) -> RockyClient:
    """
    Launch the Rocky executable with the PyRocky server enabled.

    This method waits for Rocky to start up and then returns a
    ```RockyClient`` instance.

    Parameters
    ----------
    rocky_version:
        Rocky version to run. If the version is not specified, this method tries to
        find the path using the latest Ansys path returned by ansys-tools-path API
    headless:
        Whether to launch Rocky in headless mode. The default is ``True``.
    server_port:
        Set the port for Rocky RPC server.
    close_existing:
        Checks if a session exists under the given server_port and closes it
        before attempting to launch a new session.

    Returns
    -------
    RockyClient
        Rocky client instance connected to the launched Rocky app.
    """
    if isinstance(rocky_version, str):
        rocky_version = int(rocky_version)

    if _is_port_busy(server_port):
        if close_existing:
            # Will try to connect to an existing session using the
            # given server port and attempt to close it.
            client = connect_to_rocky(port=server_port)
            try:
                client.close()
            except CommunicationError:
                # Maybe the session closed in the meantime so we just pass
                pass
        else:
            raise RockyLaunchError(f"Port {server_port} is already in use.")

    ansys_installations = get_available_ansys_installations()

    if rocky_version is None:
        for installation in sorted(ansys_installations, reverse=True):
            rocky_exe = Path(ansys_installations[installation]) / "Rocky/bin/Rocky.exe"
            if rocky_exe.is_file() and installation >= MINIMUM_ANSYS_VERSION_SUPPORTED:
                break
        else:
            raise FileNotFoundError("Rocky executable is not found.")
    else:
        if rocky_version < MINIMUM_ANSYS_VERSION_SUPPORTED:
            raise ValueError(
                f"Rocky version {rocky_version} is not supported. "
                f"The minimum supported version is {MINIMUM_ANSYS_VERSION_SUPPORTED}"
            )

        if rocky_version in ansys_installations:
            ansys_installation = ansys_installations.get(rocky_version)
        else:
            raise FileNotFoundError(
                f"Rocky executable for version {rocky_version} is not found."
            )

        rocky_exe = Path(ansys_installation) / "Rocky/bin/Rocky.exe"
        if not rocky_exe.is_file():
            raise FileNotFoundError(
                f"Rocky executable for version {rocky_version} is not found."
            )

    cmd = [rocky_exe, "--pyrocky", "--pyrocky-port", str(server_port)]
    if headless:
        cmd.append("--headless")
    with contextlib.suppress(subprocess.TimeoutExpired):
        rocky_process = subprocess.Popen(cmd)
        rocky_process.wait(timeout=3)

    # Rocky.exe call returned to soon, something happen
    if rocky_process.returncode is not None:
        raise RockyLaunchError(f"Error launching Rocky:\n  {' '.join(cmd)}")

    client = connect_to_rocky(port=server_port)

    # TODO: A more elegant way to find out that Rocky Pyro server started.
    now = time.time()
    while (time.time() - now) < _CONNECT_TO_SERVER_TIMEOUT:
        try:
            client.api.GetProject()
        except CommunicationError:
            time.sleep(1)
        else:
            break
    else:
        raise RockyLaunchError("Could not connect Rocky remote server: timed out")

    client._process = rocky_process
    return client


def _is_port_busy(port: int) -> bool:
    """
    Check if there is already a Rocky server running.

    Parameters
    ----------
    port : int
        Port to check.

    Returns
    -------
    bool
        ``True`` if the port is busy, ``False`` otherwise.
    """
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0
