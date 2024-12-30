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
import sys
import time
from typing import Optional, Union
import winreg

from Pyro5.errors import CommunicationError
from ansys.tools.path import get_available_ansys_installations

from ansys.rocky.core.client import DEFAULT_SERVER_PORT, RockyClient, connect
from ansys.rocky.core.exceptions import FreeflowLaunchError, RockyLaunchError

_CONNECT_TO_SERVER_TIMEOUT = 60
MINIMUM_ANSYS_VERSION_SUPPORTED = 242
COMPANY = "Ansys"


def get_exec_using_winreg(
    product_name: str,
    version: Optional[str] = None,
    executable: Optional[Union[Path, str]] = None,
) -> Path:
    """
    This method will search for the Rocky/Freeflow executable using the
    Windows registry.

    Parameters
    ----------
    product_name:
        The name of the product (Rocky or Freeflow)
    version:
        The version of the executable
    executable:
        The path to the executable, in case the user wants to pass this directly

    Returns
    -------
    Path
        The Path to the executable
    """
    if executable is None:
        product_reg_path = rf"SOFTWARE\{COMPANY}\{product_name}"

        try:
            if version is None:
                # If no version is defined, the default is the 'current_version' attribute
                with winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE, product_reg_path
                ) as wr_key:
                    version, _ = winreg.QueryValueEx(wr_key, "current_version")

            version_reg_path = rf"{product_reg_path}\{version}"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, version_reg_path) as wr_key:
                executable_str, _ = winreg.QueryValueEx(wr_key, "local_executable")
                executable_path = Path(executable_str)
                if not executable_path.is_file():
                    raise FileNotFoundError(
                        f"{product_name} executable is not found at {executable_str}."
                    )
                return executable_path
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Local executable not found for {product_name} {version}."
            )
    elif isinstance(executable, str):
        executable = Path(executable)
        if not executable.is_file():
            raise FileNotFoundError(
                f"{product_name} executable is not found at {executable}."
            )

    return executable


def get_exec_using_tools_path(
    product_name: str,
    executable: Optional[Union[Path, str]] = None,
    version: Optional[int] = None,
) -> Path:
    """
    This method will search for the Rocky/Freeflow executable using the
    ansys-tools-path module. Currently, we are using this approach only
    for Linux, since the ansys-tools-path depends on the AWP_ROOT variable,
    which may not be defined in Rocky standalone for Windows.

    Parameters
    ----------
    product_name:
        The name of the product (Rocky or Freeflow)
    executable:
        The path to the executable, in case the user wants to pass this directly
    version:
        The version of the executable

    Returns
    -------
    Path
        The Path to the executable
    """
    ansys_installations = get_available_ansys_installations()

    if executable is None:
        if version is None:
            for installation in sorted(ansys_installations, reverse=True):
                executable = (
                    Path(ansys_installations[installation])
                    / f"{product_name}/bin/{product_name}.exe"
                )
                if (
                    executable.is_file()
                    and installation >= MINIMUM_ANSYS_VERSION_SUPPORTED
                ):
                    break
            else:  # pragma: no cover
                raise FileNotFoundError(f"{product_name} executable is not found.")
        else:
            if version in ansys_installations:
                ansys_installation = ansys_installations.get(version)
            else:  # pragma: no cover
                raise FileNotFoundError(f"{product_name} executable is not found.")

            executable = (
                Path(ansys_installation) / f"{product_name}/bin/{product_name}.exe"
            )
            if not executable.is_file():  # pragma: no cover
                raise FileNotFoundError(
                    f"{product_name} executable for version {version} is not found."
                )
    elif isinstance(executable, str):
        executable = Path(executable)
        if not executable.is_file():
            raise FileNotFoundError(
                f"{product_name} executable is not found at {executable}."
            )

    return executable


def launch_rocky(
    rocky_exe: Optional[Union[Path, str]] = None,
    rocky_version: Optional[int] = None,
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
    rocky_exe:
        Path to the Rocky executable.
    rocky_version:
        Rocky version to run. If no executable is passed and the version is not
        specified, this method tries to find the path using the latest Ansys path
        returned by ansys-tools-path API.
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
    if _is_port_busy(server_port):
        if close_existing:
            # Will try to connect to an existing session using the
            # given server port and attempt to close it.
            client = connect(port=server_port)
            try:
                client.close()
            except CommunicationError:
                # Maybe the session closed in the meantime so we just pass
                pass
        else:
            raise RockyLaunchError(f"Port {server_port} is already in use.")

    if rocky_version is not None:
        if rocky_version < MINIMUM_ANSYS_VERSION_SUPPORTED:
            raise ValueError(
                f"Rocky version {rocky_version} is not supported. "
                f"The minimum supported version is {MINIMUM_ANSYS_VERSION_SUPPORTED}"
            )

    if sys.platform == "win32":
        if rocky_version is not None:
            rocky_version = f"{rocky_version // 10}.{rocky_version % 10}.0"
        rocky_exe = get_exec_using_winreg(
            product_name="Rocky", version=rocky_version, executable=rocky_exe
        )
    else:  # pragma: no cover
        rocky_exe = get_exec_using_tools_path(
            product_name="Rocky", executable=rocky_exe, version=rocky_version
        )

    cmd = [rocky_exe, "--pyrocky", "--pyrocky-port", str(server_port)]
    if headless:
        cmd.append("--headless")
    with contextlib.suppress(subprocess.TimeoutExpired):
        rocky_process = subprocess.Popen(cmd)
        rocky_process.wait(timeout=3)

    # Rocky.exe call returned to soon, something happen
    if rocky_process.returncode is not None:  # pragma: no cover
        raise RockyLaunchError(f"Error launching Rocky:\n  {' '.join(cmd)}")

    client = connect(port=server_port)

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


def launch_freeflow(  # pragma: no cover
    freeflow_exe: Optional[Union[Path, str]] = None,
    freeflow_version: Optional[int] = None,
    *,
    headless: bool = True,
    server_port: int = DEFAULT_SERVER_PORT,
    close_existing: bool = False,
) -> RockyClient:
    """
    Launch the FreeFlow executable with the PyRocky server enabled.

    This method waits for Rocky to start up and then returns a
    ```RockyClient`` instance.

    Parameters
    ----------
    freeflow_exe:
        Path to the Freeflow executable.
    freeflow_version:
        Freeflow version to run. If no executable is passed and the version is not
        specified, this method tries to find the path using the latest Ansys path
        returned by ansys-tools-path API.
    headless:
        Whether to launch Freeflow in headless mode. The default is ``True``.
    server_port:
        Set the port for Rocky RPC server.
    close_existing:
        Checks if a session exists under the given server_port and closes it
        before attempting to launch a new session.

    Returns
    -------
    RockyClient
        Rocky client instance connected to the launched Rocky/Freeflow app.
    """
    if _is_port_busy(server_port):
        if close_existing:
            # Will try to connect to an existing session using the
            # given server port and attempt to close it.
            client = connect(port=server_port)
            try:
                client.close()
            except CommunicationError:
                # Maybe the session closed in the meantime so we just pass
                pass
        else:
            raise FreeflowLaunchError(f"Port {server_port} is already in use.")

    if freeflow_version is not None:
        if freeflow_version < MINIMUM_ANSYS_VERSION_SUPPORTED:
            raise ValueError(
                f"Freeflow version {freeflow_version} is not supported. "
                f"The minimum supported version is {MINIMUM_ANSYS_VERSION_SUPPORTED}"
            )

    if sys.platform == "win32":
        if freeflow_version is not None:
            freeflow_version = f"{freeflow_version // 10}.{freeflow_version % 10}.0-BETA"
        freeflow_exe = get_exec_using_winreg(
            product_name="Freeflow", version=freeflow_version
        )
    else:  # pragma: no cover
        freeflow_exe = get_exec_using_tools_path(
            product_name="Freeflow", executable=freeflow_exe, version=freeflow_version
        )

    cmd = [freeflow_exe, "--pyrocky", "--pyrocky-port", str(server_port)]
    if headless:
        cmd.append("--headless")
    with contextlib.suppress(subprocess.TimeoutExpired):
        rocky_process = subprocess.Popen(cmd)
        rocky_process.wait(timeout=3)

    # Freeflow.exe call returned to soon, something happen
    if rocky_process.returncode is not None:
        raise FreeflowLaunchError(f"Error launching Freeflow:\n  {' '.join(cmd)}")

    client = connect(port=server_port)

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
        raise FreeflowLaunchError("Could not connect Freeflow remote server: timed out")

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
