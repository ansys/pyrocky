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

from typing import Optional, Union

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle_inlet_properties import (
    RAParticleInletPropertiesList as RAParticleInletPropertiesList,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAParticleInlet(ApiElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetTonnageList(self): ...
    def GetInputPropertiesList(self) -> RAParticleInletPropertiesList: ...
    def EnablePeriodicDischarge(self) -> None: ...
    def DisablePeriodicDischarge(self) -> None: ...
    def IsPeriodicDischargeEnabled(self) -> bool: ...
    def GetPeriodicDischarge(self) -> bool: ...
    def SetPeriodicDischarge(self, value): ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetInjectionDuration(self, unit: Optional[str] = ...) -> float: ...
    def SetInjectionDuration(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetDischargeTime(self, unit: Optional[str] = ...) -> float: ...
    def SetDischargeTime(self, value: float, unit: Optional[str] = ...) -> None: ...
    def GetForcePacking(self) -> bool: ...
    def SetForcePacking(self, value: bool) -> None: ...
    def EnableForcePacking(self) -> None: ...
    def DisableForcePacking(self) -> None: ...
    def IsForcePackingEnabled(self) -> bool: ...
    def GetPeriod(self, unit: Optional[str] = ...) -> float: ...
    def SetPeriod(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetPeriodic(self) -> bool: ...
    def SetPeriodic(self, value: bool) -> None: ...
    def EnablePeriodic(self) -> None: ...
    def DisablePeriodic(self) -> None: ...
    def IsPeriodicEnabled(self) -> bool: ...
    def GetStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetStopAllAtStopTime(self) -> bool: ...
    def SetStopAllAtStopTime(self, value: bool) -> None: ...
    def EnableStopAllAtStopTime(self) -> None: ...
    def DisableStopAllAtStopTime(self) -> None: ...
    def IsStopAllAtStopTimeEnabled(self) -> bool: ...
    def GetStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetTargetNormalVelocity(self, unit: Optional[str] = ...) -> float: ...
    def SetTargetNormalVelocity(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetUseTargetNormalVelocity(self) -> bool: ...
    def SetUseTargetNormalVelocity(self, value: bool) -> None: ...
    def EnableUseTargetNormalVelocity(self) -> None: ...
    def DisableUseTargetNormalVelocity(self) -> None: ...
    def IsUseTargetNormalVelocityEnabled(self) -> bool: ...
    def GetUxLocal(self, unit: Optional[str] = ...) -> float: ...
    def SetUxLocal(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetUzLocal(self, unit: Optional[str] = ...) -> float: ...
    def SetUzLocal(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSphInjectionEnabled(self) -> bool: ...
    def SetSphInjectionEnabled(self, value: bool) -> None: ...
    def GetSphTemperature(self, unit: Optional[str] = ...) -> float: ...
    def SetSphTemperature(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetEntryPoint(self): ...
    def SetEntryPoint(self, value) -> None: ...
    def GetAvailableEntryPoints(self): ...