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
"""Module for launching operations of the Rocky backend."""
import contextlib
import os
from pathlib import Path
import subprocess
import time
from typing import Optional, Union

from Pyro5.errors import CommunicationError

from ansys.rocky.core.client import DEFAULT_SERVER_PORT, RockyClient, connect_to_rocky
from ansys.rocky.core.exceptions import RockyLaunchError

_CONNECT_TO_SERVER_TIMEOUT = 60


def launch_rocky(
    rocky_exe: Optional[Union[Path, str]] = None,
    *,
    headless: bool = True,
    server_port: int = DEFAULT_SERVER_PORT,
) -> RockyClient:
    """
    Launch the Rocky executable with the PyRocky server enabled.

    This method waits for Rocky to start up and then returns a
    ```RockyClient`` instance.

    Parameters
    ----------
    rocky_exe : Optional[Path], optional
        Path to the Rocky executable. If a path is not specified, this method
        tries to find the path in the ``AWP_ROOT241`` and ``AWP_ROOT232``
        environment variables.
    headless : bool, optional
        Whether to launch Rocky in headless mode. The default is ``True``.
    server_port: int, optional
        Port that hosts the Rocky server.

    Returns
    -------
    RockyClient
        Rocky client instance connected to the launched Rocky app.
    """
    if isinstance(rocky_exe, str):
        rocky_exe = Path(rocky_exe)

    if _is_port_busy(server_port):
        raise RockyLaunchError(f"Port {server_port} is already in use.")

    if rocky_exe is None:
        for awp_root in ["AWP_ROOT241", "AWP_ROOT232"]:
            if awp_root not in os.environ:
                continue

            rocky_exe = Path(os.environ[awp_root]) / "Rocky/bin/Rocky.exe"
            if rocky_exe.is_file():
                break
        else:
            raise FileNotFoundError("Rocky executable is not found.")
    else:
        if not rocky_exe.is_file():
            raise FileNotFoundError(f"Rocky executable is not found at {rocky_exe}.")

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
