import pickle
from typing import Generator

import Pyro5.api
import serpent

from ansys.rocky.core.exceptions import RockyApiError

_ROCKY_API = None


def connect_to_rocky(host: str = "localhost", port: int = 50615) -> "RockyClient":
    """Connect to a Rocky Application instance.

    Parameters
    ----------
    host : str, optional
        The host name where the application is running, by default "localhost".
    port : int, optional
        The service port to connect, by default 50615.
    
    Returns
    -------
    RockyClient
        A client object to interact with the Rocky Application.
    """
    uri = f"PYRO:rocky.api@{host}:{port}"
    global _ROCKY_API
    _ROCKY_API = Pyro5.api.Proxy(uri)
    rocky_client = RockyClient(_ROCKY_API)
    return rocky_client


class RockyClient:
    """A client object to interact with the Rocky Application.
    
    Parameters
    ----------
    rocky_api : Pyro5.api.Proxy
        The Pyro5 proxy object to interact with the Rocky Application.
    """
    def __init__(self, rocky_api):
        self._api_adapter = rocky_api

    @property
    def api(self):
        return self._api_adapter

    def close(self):
        self._api_adapter.Exit()


class _ApiElementProxy:
    """A proxy object for API Elements.
    
    Parameters
    ----------
    pyro_api : Pyro5.api.Proxy
        The Pyro5 proxy object to interact with the Rocky Application.
    pool_id : int
        The ID of the API Element.
    """
    def __init__(self, pyro_api, pool_id):
        self._pool_id = pool_id
        self._pyro_api = pyro_api

    def __getattr__(self, attr_name: str) -> object:
        def CallProxy(*args, **kwargs):
            return self._pyro_api.SendToApiElement(
                self._pool_id, attr_name, *args, **kwargs
            )

        return CallProxy

    @classmethod
    def deserialize(cls, classname: str, serialized: dict) -> "_ApiElementProxy":
        """Deserialize an API Element Proxy object.

        Parameters
        ----------
        serialized : dict
            The serialized object.

        Returns
        -------
        _ApiElementProxy
            The deserialized object.
        """
        return cls(_ROCKY_API, serialized["_api_element_id"])

    @classmethod
    def serialize(cls, classname: str, obj) -> dict:
        """Serialize an API Element Proxy object.

        Parameters
        ----------
        obj : Any
            The object to be serialized.

        Returns
        -------
        dict
            The serialized object.
        """
        return {"__class__": cls.__name__, "_api_element_id": obj._pool_id}


class _ApiListProxy(_ApiElementProxy):
    """A proxy object for API Elements that implement the sequence interface.
    """

    def __len__(self) -> int:
        return self._pyro_api.SendToApiElement(self._pool_id, "__len__")

    def __getitem__(self, index: int) -> _ApiElementProxy:
        return self._pyro_api.SendToApiElement(self._pool_id, "__getitem__", index)

    def __iter__(self) -> Generator[_ApiElementProxy, None, None]:
        for index in range(len(self)):
            yield self[index]

    def __delitem__(self, index: int) -> None:
        self._pyro_api.SendToSubject(self._pool_id, "__delitem__", index)


def deserialize_api_error(classname: str, serialized: dict) -> RockyApiError:
    """Deserialize an API Error.
    
    Parameters
    ----------
    serialized : dict
        The serialized object.

    Returns
    -------
    RockyApiError
        The error in serialized object.
    """
    return RockyApiError(serialized["message"])


def deserialize_numpy(classname, serialized) -> "Any":
    """Deserialize a numpy array.

    Parameters
    ----------
    serialized : dict
        The serialized object.

    Returns
    -------
    Any
        The deserialized object.
    """
    bytes_rocky = serpent.tobytes(serialized["bytes"])
    return pickle.loads(bytes_rocky)


Pyro5.api.register_dict_to_class("ApiElementProxy", _ApiElementProxy.deserialize)
Pyro5.api.register_dict_to_class("ApiListProxy", _ApiListProxy.deserialize)
Pyro5.api.register_dict_to_class("RockyApiError", deserialize_api_error)
Pyro5.api.register_dict_to_class("ndarray", deserialize_numpy)

Pyro5.api.register_class_to_dict(_ApiElementProxy, _ApiElementProxy.serialize)



