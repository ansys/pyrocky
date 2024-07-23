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

from _typeshed import Incomplete
from rocky30.models.sph.sph_settings import SPHProcess as SPHProcess

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RASPHSettings(RAGridProcessElementItem):
    def __init__(self, id, model_id: Incomplete | None = ...) -> None: ...
    @classmethod
    def GetWrappedClass(self) -> type[SPHProcess]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetBackgroundPressure(self) -> float: ...
    def SetBackgroundPressure(
        self, value: Union[str, float], unit: Union[str, None] = ...
    ) -> None: ...
    def SetSolver(self, value: str) -> None: ...
    def GetSolver(self) -> str: ...
    def GetCS(self) -> float: ...
    def SetCS(self, value: Union[str, float]) -> None: ...
    def GetClearyFactor(self) -> float: ...
    def SetClearyFactor(self, value: Union[str, float]) -> None: ...
    def GetDensityDevMinus(self) -> float: ...
    def SetDensityDevMinus(self, value: Union[str, float]) -> None: ...
    def GetDensityDevPlus(self) -> float: ...
    def SetDensityDevPlus(self, value: Union[str, float]) -> None: ...
    def GetDensityRelativeErrorTolerance(self) -> float: ...
    def SetDensityRelativeErrorTolerance(self, value: Union[str, float]) -> None: ...
    def GetDissFactor(self) -> float: ...
    def SetDissFactor(self, value: Union[str, float]) -> None: ...
    def GetDistFactorNorm(self) -> float: ...
    def SetDistFactorNorm(self, value: Union[str, float]) -> None: ...
    def GetDistFactorTang(self) -> float: ...
    def SetDistFactorTang(self, value: Union[str, float]) -> None: ...
    def GetEulerianSolutionEnabled(self) -> bool: ...
    def SetEulerianSolutionEnabled(self, value: bool) -> None: ...
    def EnableEulerianSolution(self) -> None: ...
    def DisableEulerianSolution(self) -> None: ...
    def IsEulerianSolutionEnabled(self) -> bool: ...
    def GetFreeSurfaceDivergenceLimit(self) -> float: ...
    def SetFreeSurfaceDivergenceLimit(self, value: Union[str, float]) -> None: ...
    def GetKernelDistFactor(self) -> float: ...
    def SetKernelDistFactor(self, value: Union[str, float]) -> None: ...
    def GetKernelType(self) -> str: ...
    def SetKernelType(self, value: str) -> None: ...
    def GetValidKernelTypeValues(self) -> List[str]: ...
    def GetMaximumExpectedVelocity(self, unit: Optional[str] = ...) -> float: ...
    def SetMaximumExpectedVelocity(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetMaximumNumberOfIterations(self) -> int: ...
    def SetMaximumNumberOfIterations(self, value: Union[str, int]) -> None: ...
    def GetMinDistFactor(self) -> float: ...
    def SetMinDistFactor(self, value: Union[str, float]) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetNegativePressureFactor(self) -> float: ...
    def SetNegativePressureFactor(self, value: Union[str, float]) -> None: ...
    def GetNumCellSteps(self) -> int: ...
    def SetNumCellSteps(self, value: Union[str, int]) -> None: ...
    def GetNumberOfSteps(self) -> int: ...
    def SetNumberOfSteps(self, value: Union[str, int]) -> None: ...
    def GetPosCorrectionType(self) -> str: ...
    def SetPosCorrectionType(self, value: str) -> None: ...
    def GetValidPosCorrectionTypeValues(self) -> List[str]: ...
    def GetPressureDeg(self) -> int: ...
    def SetPressureDeg(self, value: Union[str, int]) -> None: ...
    def GetPressureUnderRelaxationFactor(self) -> float: ...
    def SetPressureUnderRelaxationFactor(self, value: Union[str, float]) -> None: ...
    def GetShiftingFactor(self) -> float: ...
    def SetShiftingFactor(self, value: Union[str, float]) -> None: ...
    def GetSize(self, unit: Optional[str] = ...) -> float: ...
    def SetSize(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSolverModel(self) -> str: ...
    def SetSolverModel(self, value: str) -> None: ...
    def GetValidSolverModelValues(self) -> List[str]: ...
    def GetSoundSpeed(self, unit: Optional[str] = ...) -> float: ...
    def SetSoundSpeed(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetStabilityDegree(self) -> int: ...
    def SetStabilityDegree(self, value: Union[str, int]) -> None: ...
    def GetStabilityNegFactor(self) -> float: ...
    def SetStabilityNegFactor(self, value: Union[str, float]) -> None: ...
    def GetStabilityPosFactor(self) -> float: ...
    def SetStabilityPosFactor(self, value: Union[str, float]) -> None: ...
    def GetStiffFactor(self) -> float: ...
    def SetStiffFactor(self, value: Union[str, float]) -> None: ...
    def GetSurfaceTensionBoundaryAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetSurfaceTensionBoundaryAngle(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetSurfaceTensionBoundaryFraction(self) -> float: ...
    def SetSurfaceTensionBoundaryFraction(self, value: Union[str, float]) -> None: ...
    def GetSurfaceTensionCoefficient(self, unit: Optional[str] = ...) -> float: ...
    def SetSurfaceTensionCoefficient(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetSurfaceTensionType(self) -> str: ...
    def SetSurfaceTensionType(self, value: str) -> None: ...
    def GetValidSurfaceTensionTypeValues(self) -> List[str]: ...
    def GetTimestepFactor(self) -> float: ...
    def SetTimestepFactor(self, value: Union[str, float]) -> None: ...
    def GetTurbDistanceFraction(self) -> float: ...
    def SetTurbDistanceFraction(self, value: Union[str, float]) -> None: ...
    def GetTurbulenceType(self) -> str: ...
    def SetTurbulenceType(self, value: str) -> None: ...
    def GetValidTurbulenceTypeValues(self) -> List[str]: ...
    def GetTurbulentPrandtl(self) -> float: ...
    def SetTurbulentPrandtl(self, value: Union[str, float]) -> None: ...
    def GetUpdateCoupledDensity(self) -> bool: ...
    def SetUpdateCoupledDensity(self, value: bool) -> None: ...
    def GetUseParticlesNeighborsList(self) -> bool: ...
    def SetUseParticlesNeighborsList(self, value: bool) -> None: ...
    def GetViscosityType(self) -> str: ...
    def SetViscosityType(self, value: str) -> None: ...
    def GetValidViscosityTypeValues(self) -> List[str]: ...
    def GetXsphFactor(self) -> float: ...
    def SetXsphFactor(self, value: Union[str, float]) -> None: ...
    def GetFluidMaterial(self): ...
    def SetFluidMaterial(self, value) -> None: ...
    def GetAvailableFluidMaterials(self): ...