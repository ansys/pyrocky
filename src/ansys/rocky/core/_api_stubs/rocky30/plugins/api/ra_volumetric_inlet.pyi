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
from typing import List, Optional, Union

from rocky30.models.input.volume_fill import VolumeFill as VolumeFill

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_volumetric_inlet_properties import (
    RAVolumetricInletPropertiesList as RAVolumetricInletPropertiesList,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAVolumetricInlet(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[VolumeFill]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetInputPropertiesList(self) -> RAVolumetricInletPropertiesList: ...
    def GetCustomGeometries(self): ...
    def SetCustomGeometries(self, values) -> None: ...
    def GetUseCustomGeometriesToCompute(self): ...
    def SetUseCustomGeometriesToCompute(self, value) -> None: ...
    def GetBoxCenter(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetBoxCenter(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetBoxDimensions(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetBoxDimensions(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetUseGeometriesToCompute(self) -> bool: ...
    def SetUseGeometriesToCompute(self, value: bool) -> None: ...
    def GetGapScaleFactor(self) -> float: ...
    def SetGapScaleFactor(self, value: Union[str, float]) -> None: ...
    def GetInitialVelocity(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetInitialVelocity(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetSeedCoordinates(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetSeedCoordinates(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetSphMass(self, unit: Optional[str] = ...) -> float: ...
    def SetSphMass(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSphTemperature(self, unit: Optional[str] = ...) -> float: ...
    def SetSphTemperature(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetGeometries(self): ...
    def SetGeometries(self, values) -> None: ...
    def GetAvailableGeometries(self): ...
