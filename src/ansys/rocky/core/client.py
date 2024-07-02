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
"""
Module that defines the ``RockyClient`` class, which acts as a proxy for a Rocky
application session.
"""
from typing import Final

import Pyro5.api
<<<<<<< Updated upstream
from serializers import register_proxies
=======

from ansys.rocky.core.serializers import register_proxies
>>>>>>> Stashed changes

register_proxies()

DEFAULT_SERVER_PORT: Final[int] = 50615

_ROCKY_API: Pyro5.api.Proxy | None = None


def connect_to_rocky(
    host: str = "localhost", port: int = DEFAULT_SERVER_PORT
) -> "RockyClient":
    """Connect to a Rocky app instance.

    Parameters
    ----------
    host : str, optional
        Host name where the app is running. The default is ``"localhost"``.
    port : int, optional
        Service port to connect to. The default is ``DEFAULT_SERVER_PORT``,
        which is 50615.

    Returns
    -------
    RockyClient
        Client object for interacting with the Rocky app.
    """
    uri = f"PYRO:rocky.api@{host}:{port}"
    global _ROCKY_API
    _ROCKY_API = Pyro5.api.Proxy(uri)
    rocky_client = RockyClient(_ROCKY_API)
    return rocky_client


class RockyClient:
    """Provides the client object for interacting with the Rocky app.

    Parameters
    ----------
    rocky_api : Pyro5.api.Proxy
        Pyro5 proxy object for interacting with the Rocky app.
    """

    def __init__(self, rocky_api):
        self._api_adapter = rocky_api

    @property
    def api(self):
        return self._api_adapter

    def close(self):
        self._api_adapter.Exit()
