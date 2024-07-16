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

from collections.abc import Sequence
from typing import NamedTuple, Union

from rocky30.plugins.addins.model.addin_manager import AddinManager as AddinManager
from rocky30.plugins.addins.model.property_set import PropertyEntry as PropertyEntry
from rocky30.plugins.addins.model.property_set import PropertySet as PropertySet

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addin_list import (
    RAModulePropertyList as RAModulePropertyList,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addin_process import (
    RAModuleOutput as RAModuleOutput,
)

class ModulePropertyIdentifier(NamedTuple):
    name: str
    modules: set[str]

class ElementWithAddins:
    def GetModuleProperties(self) -> Sequence[ModulePropertyIdentifier]: ...
    def GetModuleProperty(
        self,
        property_name: Union[str, ModulePropertyIdentifier],
        unit: Union[str, None] = ...,
    ) -> Union[float, bool, str, "RAModulePropertyList"]: ...
    def SetModuleProperty(
        self,
        property_name: Union[str, ModulePropertyIdentifier],
        value: Union[float, bool, str],
        unit: Union[str, None] = ...,
    ) -> None: ...
    def GetValidOptionsForModuleProperty(self, property_name): ...

class RAModule(ApiElementItem, ElementWithAddins):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def EnableModule(self) -> None: ...
    def DisableModule(self) -> None: ...
    def SetModuleEnabled(self, enabled) -> None: ...
    def IsModuleEnabled(self): ...
    def GetName(self): ...
    def SetName(self, name) -> None: ...
    def GetOutputObject(self) -> Union[RAModuleOutput, None]: ...

class RAModuleCollection(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[AddinManager]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetModuleNames(self) -> list[str]: ...
    def GetEnabledModules(self) -> list[str]: ...
    def GetModule(self, module_name: str) -> RAModule: ...
