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
"""Module that exposes functions to launch a Rocky application session."""
import contextlib
from pathlib import Path
import subprocess
import sys
import time

from Pyro5.errors import CommunicationError
from ansys.tools.path import get_available_ansys_installations

from ansys.rocky.core.client import PYROCKY_DEFAULT_PORT, RockyClient, connect
from ansys.rocky.core.exceptions import FreeflowLaunchError, RockyLaunchError

MINIMUM_ANSYS_VERSION_SUPPORTED = 242
COMPANY = "Ansys"


def launch_rocky(
    rocky_exe: Path | str | None = None,
    rocky_version: int | None = None,
    *,
    headless: bool = True,
    server_port: int = PYROCKY_DEFAULT_PORT,
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

    if rocky_exe is None:
        rocky_exe = _find_executable(product_name="Rocky", version=rocky_version)
    else:
        if isinstance(rocky_exe, str):
            rocky_exe = Path(rocky_exe)

    if rocky_exe is None or not rocky_exe.is_file():
        raise FileNotFoundError(f"Rocky executable is not found.")

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
    client._process = rocky_process
    return client


def launch_freeflow(  # pragma: no cover
    freeflow_exe: Path | str | None = None,
    freeflow_version: int | None = None,
    *,
    headless: bool = True,
    server_port: int = PYROCKY_DEFAULT_PORT,
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

    if freeflow_exe is None:
        freeflow_exe = _find_executable(product_name="Freeflow", version=freeflow_version)
    else:
        if isinstance(freeflow_exe, str):
            freeflow_exe = Path(freeflow_exe)

    if freeflow_exe is None or not freeflow_exe.is_file():
        raise FileNotFoundError(f"Freeflow executable is not found.")

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
    client._process = rocky_process
    return client


def _is_port_busy(port: int, timeout: int = 10) -> bool:
    """
    Check if there is already a Rocky server running.

    Parameters
    ----------
    port : int
        Port to check.
    timeout : int
        How long to wait for the port to be freed.

    Returns
    -------
    bool
        ``True`` if the port is busy, ``False`` otherwise.
    """
    import socket

    for _ in range(timeout):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("localhost", port)) == 0:
                time.sleep(1)
            else:
                return False
    return True


def _find_executable(
    product_name: str,
    version: int | None,
) -> Path:
    """
    This function will search for the Rocky/Freeflow executable

    Parameters
    ----------
    product_name:
        The name of the product (Rocky or Freeflow)
    version:
        The version of the executable

    Returns
    -------
    Path
        The Path to the executable
    """
    if sys.platform == "win32":
        if version is not None:
            if product_name == "Rocky" or version >= 261:
                version = f"{version // 10}.{version % 10}.0"
            else:
                version = f"{version // 10}.{version % 10}.0-BETA"

        executable = _get_exec_using_winreg(product_name=product_name, version=version)
    else:  # pragma: no cover
        executable = _get_exec_using_tools_path(
            product_name=product_name, version=version
        )

    return executable


def _get_exec_using_winreg(
    product_name: str,
    version: str | None = None,
) -> Path:
    """
    This function will search for the Rocky/Freeflow executable using the
    Windows registry.

    Parameters
    ----------
    product_name:
        The name of the product (Rocky or Freeflow)
    version:
        The version of the executable

    Returns
    -------
    Path
        The Path to the executable
    """
    import winreg

    product_reg_path = rf"SOFTWARE\{COMPANY}\{product_name}"

    try:
        if version is None:
            # If no version is defined, the default is the 'current_version' attribute
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, product_reg_path) as wr_key:
                version, _ = winreg.QueryValueEx(wr_key, "current_version")

        version_reg_path = rf"{product_reg_path}\{version}"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, version_reg_path) as wr_key:
            executable_str, _ = winreg.QueryValueEx(wr_key, "local_executable")
            return Path(executable_str)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Local executable not found for {product_name} {version}."
        )


def _get_exec_using_tools_path(  # pragma: no cover
    product_name: str,
    version: int | None = None,
) -> Path | None:
    """
    This function will search for the Rocky/Freeflow executable using the
    ansys-tools-path module. Currently, we are using this approach only
    for Linux, since the ansys-tools-path depends on the AWP_ROOT variable,
    which may not be defined in Rocky standalone for Windows.

    Parameters
    ----------
    product_name:
        The name of the product (Rocky or Freeflow
    version:
        The version of the executable

    Returns
    -------
    Path
        The Path to the executable
    """
    ansys_installations = get_available_ansys_installations()

    if version is None:
        for installation in sorted(ansys_installations, reverse=True):
            executable = (
                Path(ansys_installations[installation])
                / f"{product_name.lower()}/bin/{product_name}"
            )
            if executable.is_file() and installation >= MINIMUM_ANSYS_VERSION_SUPPORTED:
                break
        else:
            return
    else:
        if version in ansys_installations:
            ansys_installation = ansys_installations.get(version)
        else:
            raise FileNotFoundError(f"{product_name} executable is not found.")

        executable = (
            Path(ansys_installation) / f"{product_name.lower()}/bin/{product_name}"
        )

    return executable
