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
Module that defines the ``ApiElementProxy`` classes, which acts as a proxy for a
Rocky application internal objects.
"""
from collections.abc import Callable, Generator
from typing import Any

import Pyro5.api


class ApiElementProxy:
    """Provides a proxy object for an API element.

    Parameters
    ----------
    pyro_api : Pyro5.api.Proxy
        Pyro5 proxy object for interacting with the Rocky app.
    pool_id : int
        ID of the API element.
    """

    def __init__(
        self, pyro_api: Pyro5.api.Proxy, pool_id: str, session_uid: str | None = None
    ) -> None:
        self._pyro_api = pyro_api
        self._pool_id = pool_id
        self._session_uid = session_uid

    def __getattr__(self, attr_name: str) -> object:
        def CallProxy(*args: tuple, **kwargs: dict) -> Any:
            return self._pyro_api.SendToApiElement(
                self._pool_id, attr_name, *args, **kwargs
            )

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
        return {
            "__class__": obj.__class__.__name__,
            "_api_element_id": obj._pool_id,
            "_session_uid": obj._session_uid if obj._session_uid is not None else None,
        }


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
    def __init__(
        self,
        grid_pool_id: str,
        gf_name: str,
        pyro_api: Pyro5.api.Proxy,
        session_uid: str | None = None,
    ) -> None:
        self._grid_pool_id = grid_pool_id
        self._gf_name = gf_name
        self._pyro_api = pyro_api
        self._session_uid = session_uid

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
            "_session_uid": obj._session_uid if obj._session_uid is not None else None,
        }


class ApiExportToolkitProxy:
    def __init__(self, pyro_api: Pyro5.api.Proxy, session_uid: str | None = None) -> None:
        self._pyro_api = pyro_api
        self._session_uid = session_uid

    def __getattr__(self, attr_name: str) -> Callable:
        def CallProxy(*args: tuple, **kwargs: dict) -> Any:
            return self._pyro_api.SendToRAStudy(
                "GetExportToolkit", attr_name, *args, **kwargs
            )

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
        return {
            "__class__": cls.__name__,
            "_session_uid": obj._session_uid if obj._session_uid is not None else None,
        }


class ApiProjectProxy(ApiElementProxy):
    def __init__(self, pyro_api: Pyro5.api.Proxy, session_uid: str | None = None) -> None:
        super().__init__(pyro_api, "project", session_uid)

    def CloseProject(self, check_save_state: bool = True) -> None:
        if check_save_state and self.HasUnsavedChanges():
            raise RuntimeError(
                "Project has unsaved changes."
                "Save the project before closing or use check_save_state=False."
            )

        self._pyro_api.SendToApiElement(
            self._pool_id, "CloseProject", check_save_state=check_save_state
        )


class ApiTimeStatisticsProxy(ApiElementProxy):
    """Proxy of Time Statistics api objects."""

    def __getattr__(self, attr_name: str) -> Callable:
        def CallProxy(*args: tuple, **kwargs: dict) -> Any:
            return self._pyro_api.SendToRATimeStatistics(
                self._pool_id, attr_name, *args, **kwargs
            )

        return CallProxy
