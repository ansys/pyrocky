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
"""
Module that defines the ``ApiElementProxy`` classes, which acts as a proxy for a
Rocky application internal objects.
"""
import pickle
from typing import Any

import Pyro5.api
import serpent

from ansys.rocky.core.rocky_api_proxies import (
    ApiElementProxy,
    ApiExportToolkitProxy,
    ApiGridFunctionProxy,
    ApiListProxy,
)


def register_proxies() -> None:
    Pyro5.api.register_dict_to_class("ApiElementProxy", deserialize_api_element)
    Pyro5.api.register_dict_to_class("ApiListProxy", deserialize_api_list)
    Pyro5.api.register_dict_to_class(
        "ApiGridFunctionProxy", deserialize_api_grid_function
    )
    Pyro5.api.register_dict_to_class(
        "ApiExportToolkitProxy", deserialize_api_exporttoolkit
    )
    Pyro5.api.register_dict_to_class("RockyApiError", deserialize_api_error)
    Pyro5.api.register_dict_to_class("ndarray", deserialize_numpy)

    Pyro5.api.register_class_to_dict(ApiElementProxy, _ApiElementProxySerializer)


def _ApiElementProxySerializer(obj: ApiElementProxy) -> dict:
    """
    Serialize an `ApiElementProxy` ensuring backward compatibility with
    ROCKY 24.2 and older versions.
    """
    from ansys.rocky.core.client import _get_numerical_version

    rocky_api = obj._api
    ROCKY_VERSION = _get_numerical_version(rocky_api)

    serialized = ApiElementProxy.serialize(obj)

    if ROCKY_VERSION is not None and ROCKY_VERSION < 250:
        serialized["__class__"] = f'_{serialized["__class__"]}'
    return serialized


def deserialize_api_element(classname: str, serialized: dict) -> ApiElementProxy:
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
    from .client import RockyClient

    rocky_api = RockyClient._thread_local.rocky_api
    assert rocky_api is not None, "API Proxy not initialized"
    return ApiElementProxy(rocky_api, serialized["_api_element_id"])


def deserialize_api_list(classname: str, serialized: dict) -> ApiListProxy:
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
    from .client import RockyClient

    rocky_api = RockyClient._thread_local.rocky_api
    assert rocky_api is not None, "API Proxy not initialized"
    return ApiListProxy(rocky_api, serialized["_api_element_id"])


def deserialize_api_grid_function(
    classname: str, serialized: dict
) -> ApiGridFunctionProxy:
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
    from .client import RockyClient

    rocky_api = RockyClient._thread_local.rocky_api
    assert rocky_api is not None, "API Proxy not initialized"
    return ApiGridFunctionProxy(
        serialized["grid_pool_id"], serialized["gf_name"], rocky_api
    )


def deserialize_api_exporttoolkit(
    classname: str, serialized: dict
) -> ApiExportToolkitProxy:
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
    from .client import RockyClient

    rocky_api = RockyClient._thread_local.rocky_api
    assert rocky_api is not None, "API Proxy not initialized"
    return ApiExportToolkitProxy(rocky_api)


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
