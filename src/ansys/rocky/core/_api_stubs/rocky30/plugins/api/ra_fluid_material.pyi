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

from typing import Optional, Union

from rocky30.models.material.fluid_material import FluidMaterial as FluidMaterial

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAFluidMaterial(ApiElementItem, ElementWithAddins):
    @classmethod
    def GetWrappedClass(self) -> type[FluidMaterial]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetSoundSpeed(self, unit: Union[str, None] = ...) -> None: ...
    def SetSoundSpeed(
        self, value: Union[str, float], unit: Union[str, None] = ...
    ) -> None: ...
    def GetDensity(self, unit: Optional[str] = ...) -> float: ...
    def SetDensity(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetSpecificHeat(self, unit: Optional[str] = ...) -> float: ...
    def SetSpecificHeat(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetThermalConductivity(self, unit: Optional[str] = ...) -> float: ...
    def SetThermalConductivity(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetViscosity(self, unit: Optional[str] = ...) -> float: ...
    def SetViscosity(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
