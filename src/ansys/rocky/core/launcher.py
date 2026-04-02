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
"""Module that exposes functions to launch a Rocky application session."""

import contextlib
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Callable, Literal

from Pyro5.errors import CommunicationError
from ansys.tools.common.path import get_available_ansys_installations

from ansys.rocky.core.client import (
    PYROCKY_DEFAULT_PORT,
    RockyClient,
    _uds_socket_path,
    connect,
)
from ansys.rocky.core.exceptions import (
    LaunchError,
    NotSupportedError,
)

MINIMUM_ANSYS_VERSION_SUPPORTED = 242
COMPANY = "Ansys"
_DEFAULT_LAUNCH_CONNECT_TIMEOUT = (
    120  # Cold start of Rocky/FreeFlow can take a long time.
)


def _launch_product(
    *,
    product_name: Literal["Rocky", "FreeFlow"],
    executable: Path | str | None,
    version: int | None,
    headless: bool,
    server_port: int,
    close_existing: bool,
    connect_timeout: int,
) -> RockyClient:
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
            raise LaunchError(f"Port {server_port} is already in use.")

    if version is not None and version < MINIMUM_ANSYS_VERSION_SUPPORTED:
        raise NotSupportedError(
            f"{product_name} version {version} is not supported. "
            f"The minimum supported version is {MINIMUM_ANSYS_VERSION_SUPPORTED}"
        )

    if executable is None:
        executable = _find_executable(product_name=product_name, version=version)
    elif isinstance(executable, str):
        executable = Path(executable)

    if executable is None or not executable.is_file():
        raise FileNotFoundError(f"{product_name} executable is not found.")

    cmd = [str(executable), "--pyrocky", "--pyrocky-port", str(server_port)]
    if headless:
        cmd.append("--headless")
    with contextlib.suppress(subprocess.TimeoutExpired):
        rocky_process = subprocess.Popen(cmd)
        rocky_process.wait(timeout=3)

    if rocky_process.returncode is not None:  # pragma: no cover
        raise LaunchError(f"Error launching {product_name}:\n  {' '.join(cmd)}")

    client = _wait_for(
        lambda: connect(port=server_port),
        timeout=connect_timeout,
        expected_exc=ConnectionRefusedError,
    )

    client._process = rocky_process
    return client


def launch_rocky(
    rocky_exe: Path | str | None = None,
    rocky_version: int | None = None,
    *,
    headless: bool = True,
    server_port: int = PYROCKY_DEFAULT_PORT,
    close_existing: bool = False,
    connect_timeout: int | None = None,
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
    connect_timeout:
        How long to wait, in seconds, when connecting to the launched Rocky session.

    Returns
    -------
    RockyClient
        Rocky client instance connected to the launched Rocky app.
    """
    return _launch_product(
        product_name="Rocky",
        executable=rocky_exe,
        version=rocky_version,
        headless=headless,
        server_port=server_port,
        close_existing=close_existing,
        connect_timeout=(
            connect_timeout if connect_timeout else _DEFAULT_LAUNCH_CONNECT_TIMEOUT
        ),
    )


def launch_freeflow(  # pragma: no cover
    freeflow_exe: Path | str | None = None,
    freeflow_version: int | None = None,
    *,
    headless: bool = True,
    server_port: int = PYROCKY_DEFAULT_PORT,
    close_existing: bool = False,
    connect_timeout: int = _DEFAULT_LAUNCH_CONNECT_TIMEOUT,
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
    connect_timeout:
        How long to wait, in seconds, when connecting to the launched Freeflow session.

    Returns
    -------
    RockyClient
        Rocky client instance connected to the launched Rocky/Freeflow app.
    """
    return _launch_product(
        product_name="FreeFlow",
        executable=freeflow_exe,
        version=freeflow_version,
        headless=headless,
        server_port=server_port,
        close_existing=close_existing,
        connect_timeout=(
            connect_timeout if connect_timeout else _DEFAULT_LAUNCH_CONNECT_TIMEOUT
        ),
    )


def launch_container(  # pragma: no cover
    product: Literal["rocky", "freeflow"] = "rocky",
    version_tag: str = "26.1.0",
    port: int = PYROCKY_DEFAULT_PORT,
    license_server: str | None = None,
) -> RockyClient:
    """
    Launch a Rocky or FreeFlow container with the PyRocky server enabled.

    Parameters
    ----------
    product:
        The product variant of the container to launch ("rocky" or "freeflow").
    version_tag:
        Semantic version tag of the container image. e.g. "26.1.0".
    port:
        Port to use for the PyRocky server inside the container.
    license_server:
        Optional license server string to set in the container. If not provided,
        the function will attempt to read the `ANSYSLMD_LICENSE_FILE` environment
        variable from the host system.

    Returns
    -------
    RockyClient
        Rocky client instance connected to the launched container.
    """
    import docker

    image = f"{product}:{version_tag}"
    uds_socket_dir = _uds_socket_path(port).parent

    if license_server is not None:
        license_file = f"1055@{license_server}"
    else:
        license_file = os.environ.get("ANSYSLMD_LICENSE_FILE")

    if license_file is None:
        raise LaunchError("Could not obtain the license file.")

    try:
        docker_client = docker.from_env()

        container = docker_client.containers.run(
            image=image,
            command=["--pyrocky", "--pyrocky-port", str(port), "--headless"],
            detach=True,
            volumes={str(uds_socket_dir): {"bind": str(uds_socket_dir), "mode": "rw"}},
            environment={
                "ANSYSLMD_LICENSE_FILE": license_file,
                "XDG_RUNTIME_DIR": str(uds_socket_dir),
            },
            remove=True,
        )
    except docker.errors.DockerException as e:
        raise LaunchError(f"Failed to start {product.capitalize()} container: {e}")

    client = connect(port=port)
    client._process = container
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
    product_name: Literal["Rocky", "FreeFlow"],
    version: int | None = None,
) -> Path | None:
    """
    This function will search for the Rocky/FreeFlow executable using the
    ansys-tools-path module.

    Parameters
    ----------
    product_name:
        The name of the product (Rocky or FreeFlow)
    version:
        The version of the executable

    Returns
    -------
    Path
        The Path to the executable
    """

    ansys_installations = get_available_ansys_installations()
    executable: Path | None = None

    def get_platform_executable_path(
        installation_path: str, product_name: Literal["Rocky", "FreeFlow"]
    ) -> Path:
        """
        Get the executable path for the current platform (Windows or Linux).
        """
        if sys.platform == "win32":
            return Path(installation_path) / f"{product_name}/bin/{product_name}.exe"
        else:  # pragma: no cover
            return Path(installation_path) / f"{product_name.lower()}/bin/{product_name}"

    if version is None:
        for installation in sorted(ansys_installations, reverse=True):
            executable = get_platform_executable_path(
                ansys_installations[installation], product_name
            )

            if executable.is_file() and installation >= MINIMUM_ANSYS_VERSION_SUPPORTED:
                break
    else:
        if version in ansys_installations:
            ansys_installation = ansys_installations.get(version)
            executable = get_platform_executable_path(ansys_installation, product_name)

    return executable


def _wait_for(predicate_callback: Callable, *, timeout: int, expected_exc) -> Any:
    """
    Repeatedly calls ``predicate_callback`` until it succeeds or timeout is reached.

    Parameters
    ----------
    predicate_callback :
        Callable invoked until it returns successfully.
    timeout :
        Maximum wait time in seconds.
    expected_exc :
        Exception type to catch and retry while waiting.

    Returns
    -------
    Any
        The return value from ``predicate_callback``.

    Raises
    ------
    expected_exc
        Raised when retries exceed ``timeout``.
    """
    started = time.time()
    latest_exception = None
    while True:
        try:
            return predicate_callback()
        except expected_exc as exception:
            latest_exception = exception
            if (time.time() - started) < timeout:
                time.sleep(1)
            else:
                if latest_exception is not None:
                    raise latest_exception
