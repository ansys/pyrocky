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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RAPhysics(ApiElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    @property
    def enable_thermal_model(self): ...
    def GetAdhesionModel(self) -> str: ...
    def SetAdhesionModel(self, value: str) -> None: ...
    def GetValidAdhesionModelValues(self) -> List[str]: ...
    def GetClosePackingVolumeFraction(self) -> float: ...
    def SetClosePackingVolumeFraction(self, value: Union[str, float]) -> None: ...
    def GetEnableCoarseGrainModeling(self) -> bool: ...
    def SetEnableCoarseGrainModeling(self, value: bool) -> None: ...
    def GetEnableThermalModel(self) -> bool: ...
    def SetEnableThermalModel(self, value: bool) -> None: ...
    def GetGravityStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetGravityStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetGravityStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetGravityStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetGravityXDirection(self, unit: Optional[str] = ...) -> float: ...
    def SetGravityXDirection(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetGravityYDirection(self, unit: Optional[str] = ...) -> float: ...
    def SetGravityYDirection(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetGravityZDirection(self, unit: Optional[str] = ...) -> float: ...
    def SetGravityZDirection(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetImpactEnergyModel(self) -> str: ...
    def SetImpactEnergyModel(self, value: str) -> None: ...
    def GetValidImpactEnergyModelValues(self) -> List[str]: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetNormalForceModel(self) -> str: ...
    def SetNormalForceModel(self, value: str) -> None: ...
    def GetValidNormalForceModelValues(self) -> List[str]: ...
    def GetRollingResistanceModel(self) -> str: ...
    def SetRollingResistanceModel(self, value: str) -> None: ...
    def GetValidRollingResistanceModelValues(self) -> List[str]: ...
    def GetExponentLimit(self) -> float: ...
    def SetExponentLimit(self, value: Union[str, float]) -> None: ...
    def GetVolumeFractionLimit(self) -> float: ...
    def SetVolumeFractionLimit(self, value: Union[str, float]) -> None: ...
    def GetRestitutionModel(self) -> str: ...
    def SetRestitutionModel(self, value: str) -> None: ...
    def GetValidRestitutionModelValues(self) -> List[str]: ...
    def GetSearchDistanceMultiplier(self) -> float: ...
    def SetSearchDistanceMultiplier(self, value: Union[str, float]) -> None: ...
    def GetSphThermalTransferModel(self) -> str: ...
    def SetSphThermalTransferModel(self, value: str) -> None: ...
    def GetValidSphThermalTransferModelValues(self) -> List[str]: ...
    def GetNumericalSofteningFactor(self) -> float: ...
    def SetNumericalSofteningFactor(self, value: Union[str, float]) -> None: ...
    def GetTangentialForceModel(self) -> str: ...
    def SetTangentialForceModel(self, value: str) -> None: ...
    def GetValidTangentialForceModelValues(self) -> List[str]: ...
    def GetThermalCorrectionModel(self) -> str: ...
    def SetThermalCorrectionModel(self, value: str) -> None: ...
    def GetValidThermalCorrectionModelValues(self) -> List[str]: ...
    def GetUpdateDistanceMultiplier(self) -> float: ...
    def SetUpdateDistanceMultiplier(self, value: Union[str, float]) -> None: ...
    def GetUseRadlEtAl(self) -> bool: ...
    def SetUseRadlEtAl(self, value: bool) -> None: ...
