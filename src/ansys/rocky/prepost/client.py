import pickle

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

    def GetNumpyCurve(self, curve_name, unit=None):
        api = self._pyro_api
        serpent_dicts = api.SendToApiElement(
            self._pool_id, "GetNumpyCurve", curve_name, unit
        )
        numpy_data = [serpent.tobytes(d) for d in serpent_dicts]
        return tuple(pickle.loads(b) for b in numpy_data)

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
        return {"__class__": "_ApiElementProxy", "_api_element_id": obj._pool_id}


Pyro5.api.register_dict_to_class("ApiElementProxy", _ApiElementProxy.deserialize)
Pyro5.api.register_class_to_dict(_ApiElementProxy, _ApiElementProxy.serialize)
