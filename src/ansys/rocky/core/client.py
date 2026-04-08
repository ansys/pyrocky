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
"""
Module that defines the ``RockyClient`` class, which acts as a proxy for a Rocky
application session.
"""
import hashlib
import os
from pathlib import Path
import sys
from typing import TYPE_CHECKING, Final
import warnings

import Pyro5.api
from Pyro5.errors import CommunicationError

from ansys.rocky.core.exceptions import NotSupportedError
from ansys.rocky.core.serializers import register_proxies

if TYPE_CHECKING:
    from ansys.rocky.app.rocky_api_application import RockyApiApplication

PYROCKY_DEFAULT_PORT: Final[int] = 9011
_API_PROXY_INSTANCES: dict[str, Pyro5.api.Proxy] = {}
_LEGACY_PROXY_INSTANCE: Pyro5.api.Proxy | None = (
    None  # Used for backward compatibility with versions < 26.1
)
# Compatibility with dependants that still import this constant.
DEFAULT_SERVER_PORT = PYROCKY_DEFAULT_PORT


def connect(host: str | None = None, port: int = PYROCKY_DEFAULT_PORT) -> "RockyClient":
    """Connect to a Rocky/Freeflow app instance.

    Parameters
    ----------
    host : str, optional
        Host name where the app is running. On Windows, default is ``"localhost"``. On
        Linux, it defaults to a unix domain socket connection.
    port : int, optional
        Service port to connect to.
    Returns
    -------
    RockyClient
        Client object for interacting with the Rocky/Freeflow app.
    """
    if sys.platform == "win32":
        # Use TCP for Windows as default
        if host is None:
            host = "localhost"
        pyro_uri = f"PYRO:rocky.api@{host}:{port}"
    else:
        # Use UDS for Linux as default
        if host:
            raise NotSupportedError(
                "TCP connections are not supported on Linux. Please omit the"
                " 'host' parameter."
            )

        socket_path = _uds_socket_path(port)
        if not socket_path.is_socket():
            raise ConnectionRefusedError(f"No socket open at '{socket_path.name}'")

        pyro_uri = f"PYRO:rocky.api@./u:{socket_path}"

    hash_str = f"localhost:{port}"
    md5_hash = hashlib.md5(hash_str.encode()).hexdigest()

    global _LEGACY_PROXY_INSTANCE

    if not _API_PROXY_INSTANCES and _LEGACY_PROXY_INSTANCE is None:
        register_proxies()

    # Remove any existing proxy for this host:port to prevent using a stale or invalid
    # connection
    _API_PROXY_INSTANCES.pop(md5_hash, None)

    proxy_instance = Pyro5.api.Proxy(pyro_uri)

    def is_proxy_connected() -> bool:
        try:
            proxy_instance._pyroBind()
        except CommunicationError:
            return False
        return proxy_instance._pyroConnection is not None

    if not is_proxy_connected():
        raise ConnectionRefusedError("Could not connect to the remote server")

    rocky_version = _get_numerical_version(proxy_instance)
    if rocky_version >= 261:
        _API_PROXY_INSTANCES[md5_hash] = proxy_instance
    else:
        _LEGACY_PROXY_INSTANCE = proxy_instance  # For backward compatibility

    rocky_client = RockyClient(proxy_instance)

    # Install Pyro hook to automatically print remote error tracebacks.
    sys.excepthook = Pyro5.errors.excepthook

    return rocky_client


def connect_to_rocky(  # pragma: no cover
    host: str | None = None,
    port: int = PYROCKY_DEFAULT_PORT,
) -> "RockyClient":
    """This function is deprecated.
    Use connect() instead.
    """
    warnings.warn(
        "connect_to_rocky() is deprecated, please use connect() instead.",
        DeprecationWarning,
    )
    return connect(host, port)


def _uds_socket_path(socket_number: int) -> Path:
    """
    ``socket_number`` parameter is used to enable the creation of different socket
    files based on the provided number.
    """
    socket_folder = (
        os.environ["XDG_RUNTIME_DIR"]
        if "XDG_RUNTIME_DIR" in os.environ
        else os.path.expanduser("~/.ansys")
    )
    return Path(socket_folder) / f"ansys-rocky-{socket_number}.sock"


class RockyClient:
    """Provides the client object for interacting with the Rocky/Freeflow app.

    Parameters
    ----------
    rocky_api : Pyro5.api.Proxy
        Pyro5 proxy object for interacting with the Rocky app.
    """

    def __init__(self, rocky_api):
        self._api_adapter = rocky_api

    @property
    def api(self) -> "RockyApiApplication":
        return self._api_adapter

    def close(self):
        if self._api_adapter.GetProject() is not None:
            # Make sure "Exit" won't be blocked by the "Unsaved Changes" dialog.
            self._api_adapter.CloseProject(check_save_state=False)
        self._api_adapter.Exit()


def _get_numerical_version(rocky_api: Pyro5.api.Proxy) -> int:
    """Provides the current Rocky app version as a numerical value
    (24R2 becomes 242, 25R1 becomes 251, ...).

    Parameters
    ----------
    rocky_api : Pyro5.api.Proxy
        Pyro5 proxy object for interacting with the Rocky app.

    Returns
    -------
    int
        Rocky app version as int.
    """
    rocky_version = rocky_api.GetVersion().split(".")
    return int(rocky_version[0] + rocky_version[1])  # major + minor
