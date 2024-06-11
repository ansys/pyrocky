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
from collections.abc import Callable, Generator
import pickle
from typing import Any, Final

import Pyro5.api
import serpent

from ansys.rocky.core.exceptions import RockyApiError

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


class _ApiElementProxy:
    """Provides a proxy object for an API element.

    Parameters
    ----------
    pyro_api : Pyro5.api.Proxy
        Pyro5 proxy object for interacting with the Rocky app.
    pool_id : int
        ID of the API element.
    """

    def __init__(self, pyro_api: Pyro5.api.Proxy, pool_id: str):
        self._pyro_api = pyro_api
        self._pool_id = pool_id

    def __getattr__(self, attr_name: str) -> object:
        def CallProxy(*args, **kwargs):
            return self._pyro_api.SendToApiElement(
                self._pool_id, attr_name, *args, **kwargs
            )

        return CallProxy

    @classmethod
    def deserialize(cls, classname: str, serialized: dict) -> "_ApiElementProxy":
        """Deserialize the proxy objects for the API element.

        Parameters
        ----------
        serialized : dict
            Dictionary of serialized objects.
        classname : str
            Name of the class to deserialize. This parameter is required by the
            superclass but is not used.

        Returns
        -------
        _ApiElementProxy
            Deserialized object.
        """
        assert _ROCKY_API is not None, "API Proxy not initialized"
        return cls(_ROCKY_API, serialized["_api_element_id"])

    @classmethod
    def serialize(cls, obj) -> dict:
        """Serialize a proxy object of the API element.

        Parameters
        ----------
        obj : Any
            Object to serialize.

        Returns
        -------
        dict
            Dictionary of the serialized object.
        """
        return {"__class__": cls.__name__, "_api_element_id": obj._pool_id}


class _ApiListProxy(_ApiElementProxy):
    """Provides a proxy object for API elements that implement the sequence interface."""

    def __len__(self) -> int:
        return self._pyro_api.SendToApiElement(self._pool_id, "__len__")

    def __getitem__(self, index: int) -> _ApiElementProxy:
        return self._pyro_api.SendToApiElement(self._pool_id, "__getitem__", index)

    def __iter__(self) -> Generator[_ApiElementProxy, None, None]:
        for index in range(len(self)):
            yield self[index]

    def __delitem__(self, index: int) -> None:
        self._pyro_api.SendToSubject(self._pool_id, "__delitem__", index)


class _ApiGridFunctionProxy:
    def __init__(self, grid_pool_id: str, gf_name: str, pyro_api) -> None:
        self._grid_pool_id = grid_pool_id
        self._gf_name = gf_name
        self._pyro_api = pyro_api

    def __getattr__(self, attr_name: str) -> Callable:
        def CallProxy(*args: tuple, **kwargs: dict):
            return self._pyro_api.SentToGridFunction(
                self._grid_pool_id, self._gf_name, attr_name, *args, **kwargs
            )

        return CallProxy

    @classmethod
    def deserialize(cls, classname: str, serialized: dict) -> "_ApiGridFunctionProxy":
        """Deserialize the proxy objects for the API element.

        Parameters
        ----------
        classname : str
            Name of the class to deserialize. This parameter is required by the
            superclass but is not used.
        serialized : dict
            Dictionary of serialized objects.

        Returns
        -------
        _ApiElementProxy
            Deserialized object.
        """
        return cls(serialized["grid_pool_id"], serialized["gf_name"], _ROCKY_API)


def deserialize_api_error(classname: str, serialized: dict) -> RockyApiError:
    """Deserialize an API error.

    Parameters
    ----------
    classname : str
        Name of the class to deserialize. This parameter is required by the superclass
        but is not used.
    serialized : dict
        Dictionary of the serialized object.

    Returns
    -------
    RockyApiError
        Error in the serialized object.
    """
    return RockyApiError(serialized["message"])


def deserialize_numpy(classname, serialized) -> Any:
    """Deserialize a numpy array.

    Parameters
    ----------
    classname : str
        Name of the class to deserialize. This parameter is required by the
        superclass but is not used.
    serialized : dict
        Dictionary of the serialized object.

    Returns
    -------
    Any
        Deserialized object.
    """
    deserialized_bytes = serpent.tobytes(serialized["bytes"])
    return pickle.loads(deserialized_bytes)


Pyro5.api.register_dict_to_class("ApiElementProxy", _ApiElementProxy.deserialize)
Pyro5.api.register_dict_to_class("ApiListProxy", _ApiListProxy.deserialize)
Pyro5.api.register_dict_to_class(
    "ApiGridFunctionProxy", _ApiGridFunctionProxy.deserialize
)
Pyro5.api.register_dict_to_class("RockyApiError", deserialize_api_error)
Pyro5.api.register_dict_to_class("ndarray", deserialize_numpy)

Pyro5.api.register_class_to_dict(_ApiElementProxy, _ApiElementProxy.serialize)
