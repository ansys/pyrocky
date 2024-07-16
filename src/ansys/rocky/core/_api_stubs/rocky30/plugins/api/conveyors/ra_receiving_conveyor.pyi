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

from typing import List, Optional, Union

from ansys.rocky.core._api_stubs.rocky30.plugins.api.conveyors.ra_base_conveyor import (
    RABaseConveyor as RABaseConveyor,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)

class RAReceivingConveyor(RABaseConveyor, ElementWithAddins):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetAccelerationPeriod(self, unit: Optional[str] = ...) -> float: ...
    def SetAccelerationPeriod(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBeginningStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetBeginningStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBeltSpeed(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltSpeed(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetDecelerationPeriod(self, unit: Optional[str] = ...) -> float: ...
    def SetDecelerationPeriod(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBeginningStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetBeginningStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBeltThickness(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltThickness(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBeltWidth(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltWidth(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetLength(self, unit: Optional[str] = ...) -> float: ...
    def SetLength(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTemperature(self, unit: Optional[str] = ...) -> float: ...
    def SetTemperature(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetThermalBoundaryConditionType(self) -> str: ...
    def SetThermalBoundaryConditionType(self, value: str) -> None: ...
    def GetValidThermalBoundaryConditionTypeValues(self) -> List[str]: ...
    def GetTriangleSize(self, unit: Optional[str] = ...) -> float: ...
    def SetTriangleSize(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetAlignmentAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetAlignmentAngle(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBeltInclineAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltInclineAngle(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetHorizontalOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetHorizontalOffset(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetOutOfPlaneOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetOutOfPlaneOffset(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetReturnBeltAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetReturnBeltAngle(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetVerticalOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetVerticalOffset(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetSkirtboardHeight(self, unit: Optional[str] = ...) -> float: ...
    def SetSkirtboardHeight(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetHeightOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetHeightOffset(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetSkirtboardLength(self, unit: Optional[str] = ...) -> float: ...
    def SetSkirtboardLength(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetLengthOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetLengthOffset(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetWidth(self, unit: Optional[str] = ...) -> float: ...
    def SetWidth(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSphBoundaryType(self) -> str: ...
    def SetSphBoundaryType(self, value: str) -> None: ...
    def GetValidSphBoundaryTypeValues(self) -> List[str]: ...
    def GetMaterial(self): ...
    def SetMaterial(self, value) -> None: ...
    def GetAvailableMaterials(self): ...
