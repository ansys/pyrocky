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
Module that defines the ``ApiElementProxy`` classes, which acts as a proxy for a
Rocky application internal objects.
"""
import pickle
from collections.abc import Callable, Generator
from typing import Any

import Pyro5.api
import serpent


class ApiElementProxy:
    """Provides a proxy object for an API element.

    Parameters
    ----------
    pyro_api : Pyro5.api.Proxy
        Pyro5 proxy object for interacting with the Rocky app.
    pool_id : int
        ID of the API element.
    """

    def __init__(self, pyro_api: Pyro5.api.Proxy, pool_id: str) -> None:
        self._pyro_api = pyro_api
        self._pool_id = pool_id

    def __getattr__(self, attr_name: str) -> object:
        def CallProxy(*args: tuple, **kwargs: dict) -> Any:
            return self._pyro_api.SendToApiElement(self._pool_id, attr_name, *args, **kwargs)

        return CallProxy

    @classmethod
    def serialize(cls, obj: "ApiElementProxy") -> dict:
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
        return {"__class__": obj.__class__.__name__, "_api_element_id": obj._pool_id}


class ApiListProxy(ApiElementProxy):
    """Provides a proxy object for API elements that implement the sequence interface."""

    def __len__(self) -> int:
        return self._pyro_api.SendToApiElement(self._pool_id, "__len__")

    def __getitem__(self, index: int) -> ApiElementProxy:
        return self._pyro_api.SendToApiElement(self._pool_id, "__getitem__", index)

    def __iter__(self) -> Generator[ApiElementProxy, None, None]:
        for index in range(len(self)):
            yield self[index]

    def __delitem__(self, index: int) -> None:
        self._pyro_api.SendToSubject(self._pool_id, "__delitem__", index)


class ApiGridFunctionProxy:
    def __init__(self, grid_pool_id: str, gf_name: str, pyro_api: Pyro5.api.Proxy) -> None:
        self._grid_pool_id = grid_pool_id
        self._gf_name = gf_name
        self._pyro_api = pyro_api

    def __getattr__(self, attr_name: str) -> Callable:
        def CallProxy(*args: tuple, **kwargs: dict) -> Any:
            return self._pyro_api.SentToGridFunction(
                self._grid_pool_id, self._gf_name, attr_name, *args, **kwargs
            )

        return CallProxy

    @classmethod
    def serialize(cls, obj: "ApiGridFunctionProxy") -> dict:
        """Serialize a proxy object of the API Grid Functions.

        Parameters
        ----------
        obj : Any
            Object to serialize.

        Returns
        -------
        dict
            Dictionary of the serialized object.
        """
        return {
            "__class__": cls.__name__,
            "grid_pool_id": obj._grid_pool_id,
            "gf_name": obj._gf_name,
        }


class ApiExportToolkitProxy:
    def __init__(self, pyro_api: Pyro5.api.Proxy) -> None:
        self._pyro_api = pyro_api

    def __getattr__(self, attr_name: str) -> Callable:
        def CallProxy(*args: tuple, **kwargs: dict) -> Any:
            return self._pyro_api.SendToRAStudy("GetExportToolkit", attr_name, *args, **kwargs)

        return CallProxy

    @classmethod
    def serialize(cls, obj: "ApiExportToolkitProxy") -> dict:
        """Serialize a proxy object of the API ExportToolkit object.

        Parameters
        ----------
        obj : Any
            Object to serialize.

        Returns
        -------
        dict
            Dictionary of the serialized object.
        """
        return {"__class__": cls.__name__}


def deserialize_api_element(classname: str, serialized: dict) -> "ApiElementProxy":
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
    ApiElementProxy
        Deserialized object.
    """
    from .client import _ROCKY_API

    assert _ROCKY_API is not None, "API Proxy not initialized"
    return ApiElementProxy(_ROCKY_API, serialized["_api_element_id"])


def deserialize_api_list(classname: str, serialized: dict) -> "ApiListProxy":
    """Deserialize the proxy objects for the API list element.

    Parameters
    ----------
    serialized : dict
        Dictionary of serialized objects.
    classname : str
        Name of the class to deserialize. This parameter is required by the
        superclass but is not used.

    Returns
    -------
    ApiListProxy
        Deserialized object.
    """
    from .client import _ROCKY_API

    assert _ROCKY_API is not None, "API Proxy not initialized"
    return ApiListProxy(_ROCKY_API, serialized["_api_element_id"])


def deserialize_api_grid_function(classname: str, serialized: dict) -> "ApiGridFunctionProxy":
    """Deserialize the proxy objects for the API grid function.

    Parameters
    ----------
    classname : str
        Name of the class to deserialize. This parameter is required by the
        superclass but is not used.
    serialized : dict
        Dictionary of serialized objects.

    Returns
    -------
    ApiGridFunctionProxy
        Deserialized object.
    """
    from .client import _ROCKY_API

    assert _ROCKY_API is not None, "API Proxy not initialized"
    return ApiGridFunctionProxy(serialized["grid_pool_id"], serialized["gf_name"], _ROCKY_API)


def deserialize_api_exporttoolkit(classname: str, serialized: dict) -> "ApiExportToolkitProxy":
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
    ApiExportToolkitProxy
        Deserialized object.
    """
    from .client import _ROCKY_API

    assert _ROCKY_API is not None, "API Proxy not initialized"
    return ApiExportToolkitProxy(_ROCKY_API)


def deserialize_api_error(classname: str, serialized: dict) -> Exception:
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
    from ansys.rocky.core.exceptions import RockyApiError

    return RockyApiError(serialized["message"])


def deserialize_numpy(classname: str, serialized: dict) -> Any:
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


def register_proxies() -> None:
    Pyro5.api.register_dict_to_class("ApiElementProxy", deserialize_api_element)
    Pyro5.api.register_dict_to_class("ApiListProxy", deserialize_api_list)
    Pyro5.api.register_dict_to_class("ApiGridFunctionProxy", deserialize_api_grid_function)
    Pyro5.api.register_dict_to_class("ApiExportToolkitProxy", deserialize_api_exporttoolkit)
    Pyro5.api.register_dict_to_class("RockyApiError", deserialize_api_error)
    Pyro5.api.register_dict_to_class("ndarray", deserialize_numpy)

    Pyro5.api.register_class_to_dict(ApiElementProxy, ApiElementProxy.serialize)
