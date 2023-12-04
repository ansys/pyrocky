import pickle
from typing import Generator

import Pyro5.api
import serpent

_ROCKY_API = None


def connect_to_rocky(host: str = "localhost", port: int = 50615) -> "RockyClient":
    """
    Connect to a Rocky Application instance.

    :param host: The host name where the application is running.

    :param port: The service port to connect.
    """
    uri = f"PYRO:rocky.api@{host}:{port}"
    global _ROCKY_API
    _ROCKY_API = Pyro5.api.Proxy(uri)
    rocky_client = RockyClient(_ROCKY_API)
    return rocky_client


class RockyClient:
    def __init__(self, rocky_api):
        self._api_adapter = rocky_api

    @property
    def api(self):
        return self._api_adapter

    def close(self):
        self._api_adapter.Exit()


class _ApiElementProxy:
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
    def deserialize(cls, classname, serialized):
        return cls(_ROCKY_API, serialized["_api_element_id"])

    @classmethod
    def serialize(cls, obj) -> dict:
        return {"__class__": cls.__name__, "_api_element_id": obj._pool_id}


class _ApiListProxy(_ApiElementProxy):
    """
    A proxy object for API Elements that implement the sequence interface.
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


def deserialize_api_error(classname, serialized):
    return RockyApiError(serialized["message"])


def deserialize_numpy(classname, serialized):
    bytes = serpent.tobytes(serialized["bytes"])
    return pickle.loads(bytes)


Pyro5.api.register_dict_to_class("ApiElementProxy", _ApiElementProxy.deserialize)
Pyro5.api.register_dict_to_class("ApiListProxy", _ApiListProxy.deserialize)
Pyro5.api.register_dict_to_class("RockyApiError", deserialize_api_error)
Pyro5.api.register_dict_to_class("ndarray", deserialize_numpy)

Pyro5.api.register_class_to_dict(_ApiElementProxy, _ApiElementProxy.serialize)


class RockyApiError(Exception):
    """
    Exception class representing an error generated in the API layer.
    """
