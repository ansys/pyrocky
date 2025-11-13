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

from _typeshed import Incomplete
from ben10 import interface
from ben10.foundation.decorators import Abstract
from coilib50.subject import Subject as Subject
from plugins10.core.pluginmanager import PluginManager as PluginManager

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_application import (
    ApiApplication as ApiApplication,
)
from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_application import (
    EPApiScripting as EPApiScripting,
)
from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_expose import (
    ApiExpose as ApiExpose,
)

class ApiError(RuntimeError): ...

class IWrappedItem(interface.Interface):
    @classmethod
    def GetWrappedClass(cls) -> None: ...
    @classmethod
    def GetClassName(cls) -> None: ...
    @classmethod
    def GetChildrenClassesToIgnore(cls) -> None: ...

class ApiElementItem:
    def __init__(self, id: str, model_id: str | None = None) -> None: ...
    @classmethod
    @Abstract
    def GetWrappedClass(cls) -> type: ...
    @classmethod
    @Abstract
    def GetClassName(cls) -> str: ...
    @classmethod
    def GetChildrenClassesToIgnore(cls) -> list[type]: ...
    def GetDataId(self) -> str: ...
    id: Incomplete
    def IsValid(self) -> bool: ...
    def GetSubject(self) -> Subject: ...
    subject: Incomplete
    @ApiExpose
    def GetName(self) -> str: ...
    @ApiExpose
    def SetName(self, name: str) -> None: ...
    name: Incomplete
    def SetSelected(self) -> None: ...
    def Select(self, element_names: list[str]) -> None: ...
