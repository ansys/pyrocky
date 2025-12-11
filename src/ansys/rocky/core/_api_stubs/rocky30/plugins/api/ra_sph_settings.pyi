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

from rocky30.models.sph.sph_settings import SPHProcess as SPHProcess

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RASPHSettings(RAGridProcessElementItem):
    """
    Rocky PrePost Scripting wrapper for SPH Settings properties.

    This wrapper corresponds to the "SPH" item on a project\'s data tree. Access it from
    the :class:`RAStudy` with:

    .. code-block:: python

        sph_settings = study.GetSphSettings()
        sph_settings = study.GetElement(\'SPH\')
    """

    def __init__(self, id, model_id=None) -> None: ...
    @classmethod
    def GetWrappedClass(self) -> type[SPHProcess]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def SetSolver(self, value: str) -> None:
        """
        Set the value of "Solver Model".

        :param value:
            The value to set. Must be one of [\'WCSPH\', \'IISPH\'].
        :raises RockyApiError:
            If `value` is not a valid "Solver Model" option.
        """

    def GetSolver(self) -> str:
        """
        Get "Solver Model" as a string.

        :return:
            The returned value will be one of [\'WCSPH\', \'IISPH\'].
        """

    def GetCS(self) -> float:
        """
        Get the value of "C S".

        """

    def SetCS(self, value: str | float) -> None:
        """
        Set the value of "C S".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetClearyFactor(self) -> float:
        """
        Get the value of "Cleary Factor".

        """

    def SetClearyFactor(self, value: str | float) -> None:
        """
        Set the value of "Cleary Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDensityDevMinus(self) -> float:
        """
        Get the value of "Density Dev Minus".

        """

    def SetDensityDevMinus(self, value: str | float) -> None:
        """
        Set the value of "Density Dev Minus".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDensityDevPlus(self) -> float:
        """
        Get the value of "Density Dev Plus".

        """

    def SetDensityDevPlus(self, value: str | float) -> None:
        """
        Set the value of "Density Dev Plus".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDensityRelativeErrorTolerance(self) -> float:
        """
        Get the value of "Density Relative Error Tolerance".

        """

    def SetDensityRelativeErrorTolerance(self, value: str | float) -> None:
        """
        Set the value of "Density Relative Error Tolerance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDissFactor(self) -> float:
        """
        Get the value of "Diss Factor".

        """

    def SetDissFactor(self, value: str | float) -> None:
        """
        Set the value of "Diss Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDistFactorNorm(self) -> float:
        """
        Get the value of "Dist Factor Norm".

        """

    def SetDistFactorNorm(self, value: str | float) -> None:
        """
        Set the value of "Dist Factor Norm".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDistFactorTang(self) -> float:
        """
        Get the value of "Dist Factor Tang".

        """

    def SetDistFactorTang(self, value: str | float) -> None:
        """
        Set the value of "Dist Factor Tang".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetEnabled(self) -> bool:
        """
        Get the value of "Enabled".

        """

    def SetEnabled(self, value: bool) -> None:
        """
        Set the value of "Enabled".

        :param value:
            The value to set.
        """

    def GetEulerianSolutionEnabled(self) -> bool:
        """
        Get the value of "Eulerian Solution Enabled".

        """

    def SetEulerianSolutionEnabled(self, value: bool) -> None:
        """
        Set the value of "Eulerian Solution Enabled".

        :param value:
            The value to set.
        """

    def EnableEulerianSolution(self) -> None:
        """
        Set the value of "Eulerian Solution" to True.
        """

    def DisableEulerianSolution(self) -> None:
        """
        Set the value of "Eulerian Solution" to False.
        """

    def IsEulerianSolutionEnabled(self) -> bool:
        """
        Check if the "Eulerian Solution" is enabled.

        """

    def GetFreeSurfaceDivergenceLimit(self) -> float:
        """
        Get the value of "Free Surface Divergence Limit".

        """

    def SetFreeSurfaceDivergenceLimit(self, value: str | float) -> None:
        """
        Set the value of "Free Surface Divergence Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetIncompressibilityRelaxationFactor(self) -> float:
        """
        Get the value of "Incompressibility Relaxation Factor".

        """

    def SetIncompressibilityRelaxationFactor(self, value: str | float) -> None:
        """
        Set the value of "Incompressibility Relaxation Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetKernelDistFactor(self) -> float:
        """
        Get the value of "Kernel Dist Factor".

        """

    def SetKernelDistFactor(self, value: str | float) -> None:
        """
        Set the value of "Kernel Dist Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetKernelType(self) -> str:
        """
        Get "Kernel Type" as a string.

        :return:
            The returned value will be one of [\'cubic\', \'quintic\', \'wendland\'].
        """

    def SetKernelType(self, value: str) -> None:
        """
        Set the value of "Kernel Type".

        :param value:
            The value to set. Must be one of [\'cubic\', \'quintic\', \'wendland\'].
        :raises RockyApiError:
            If `value` is not a valid "Kernel Type" option.
        """

    def GetValidKernelTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Kernel Type".

        :return:
            The returned list is [\'cubic\', \'quintic\', \'wendland\'].
        """

    def GetLimitTurbulentViscosity(self) -> bool:
        """
        Get the value of "Limit Turbulent Viscosity".

        """

    def SetLimitTurbulentViscosity(self, value: bool) -> None:
        """
        Set the value of "Limit Turbulent Viscosity".

        :param value:
            The value to set.
        """

    def GetMaximumExpectedVelocity(self, unit: str | None = None) -> float:
        """
        Get the value of "Maximum Expected Velocity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetMaximumExpectedVelocity(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Maximum Expected Velocity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetMaximumNumberOfIterations(self) -> int:
        """
        Get the value of "Maximum Number of Iterations".

        """

    def SetMaximumNumberOfIterations(self, value: str | int) -> None:
        """
        Set the value of "Maximum Number of Iterations".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetMinDistFactor(self) -> float:
        """
        Get the value of "Min Dist Factor".

        """

    def SetMinDistFactor(self, value: str | float) -> None:
        """
        Set the value of "Min Dist Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetName(self) -> str:
        """
        Get the value of "Name".

        """

    def SetName(self, value: str) -> None:
        """
        Set the value of "Name".

        :param value:
            The value to set.
        """

    def GetNegativePressureFactor(self) -> float:
        """
        Get the value of "Negative Pressure Factor".

        """

    def SetNegativePressureFactor(self, value: str | float) -> None:
        """
        Set the value of "Negative Pressure Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetNumCellSteps(self) -> int:
        """
        Get the value of "Num Cell Steps".

        """

    def SetNumCellSteps(self, value: str | int) -> None:
        """
        Set the value of "Num Cell Steps".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetNumberOfSteps(self) -> int:
        """
        Get the value of "Number of Steps".

        """

    def SetNumberOfSteps(self, value: str | int) -> None:
        """
        Set the value of "Number of Steps".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetPosCorrectionType(self) -> str:
        """
        Get "Pos Correction Type" as a string.

        :return:
            The returned value will be one of [\'none\', \'xsph\', \'shift\'].
        """

    def SetPosCorrectionType(self, value: str) -> None:
        """
        Set the value of "Pos Correction Type".

        :param value:
            The value to set. Must be one of [\'none\', \'xsph\', \'shift\'].
        :raises RockyApiError:
            If `value` is not a valid "Pos Correction Type" option.
        """

    def GetValidPosCorrectionTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Pos Correction Type".

        :return:
            The returned list is [\'none\', \'xsph\', \'shift\'].
        """

    def GetPressureDeg(self) -> int:
        """
        Get the value of "Pressure Deg".

        """

    def SetPressureDeg(self, value: str | int) -> None:
        """
        Set the value of "Pressure Deg".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetPressureUnderRelaxationFactor(self) -> float:
        """
        Get the value of "Pressure Under Relaxation Factor".

        """

    def SetPressureUnderRelaxationFactor(self, value: str | float) -> None:
        """
        Set the value of "Pressure Under Relaxation Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetRelaxedIncompressibilityConstraintEnabled(self) -> bool:
        """
        Get the value of "Relaxed Incompressibility Constraint Enabled".

        """

    def SetRelaxedIncompressibilityConstraintEnabled(self, value: bool) -> None:
        """
        Set the value of "Relaxed Incompressibility Constraint Enabled".

        :param value:
            The value to set.
        """

    def EnableRelaxedIncompressibilityConstraint(self) -> None:
        """
        Set the value of "Relaxed Incompressibility Constraint" to True.
        """

    def DisableRelaxedIncompressibilityConstraint(self) -> None:
        """
        Set the value of "Relaxed Incompressibility Constraint" to False.
        """

    def IsRelaxedIncompressibilityConstraintEnabled(self) -> bool:
        """
        Check if the "Relaxed Incompressibility Constraint" is enabled.

        """

    def GetShepardFilterOnDensityEnabled(self) -> bool:
        """
        Get the value of "Shepard Filter On Density Enabled".

        """

    def SetShepardFilterOnDensityEnabled(self, value: bool) -> None:
        """
        Set the value of "Shepard Filter On Density Enabled".

        :param value:
            The value to set.
        """

    def EnableShepardFilterOnDensity(self) -> None:
        """
        Set the value of "Shepard Filter On Density" to True.
        """

    def DisableShepardFilterOnDensity(self) -> None:
        """
        Set the value of "Shepard Filter On Density" to False.
        """

    def IsShepardFilterOnDensityEnabled(self) -> bool:
        """
        Check if the "Shepard Filter On Density" is enabled.

        """

    def GetShepardFilterOnPressureEnabled(self) -> bool:
        """
        Get the value of "Shepard Filter On Pressure Enabled".

        """

    def SetShepardFilterOnPressureEnabled(self, value: bool) -> None:
        """
        Set the value of "Shepard Filter On Pressure Enabled".

        :param value:
            The value to set.
        """

    def EnableShepardFilterOnPressure(self) -> None:
        """
        Set the value of "Shepard Filter On Pressure" to True.
        """

    def DisableShepardFilterOnPressure(self) -> None:
        """
        Set the value of "Shepard Filter On Pressure" to False.
        """

    def IsShepardFilterOnPressureEnabled(self) -> bool:
        """
        Check if the "Shepard Filter On Pressure" is enabled.

        """

    def GetShiftingFactor(self) -> float:
        """
        Get the value of "Shifting Factor".

        """

    def SetShiftingFactor(self, value: str | float) -> None:
        """
        Set the value of "Shifting Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetSize(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetSolverModel(self) -> str:
        """
        Get "Solver Model" as a string.

        :return:
            The returned value will be one of [\'WCSPH\', \'IISPH\', \'DFSPH\'].
        """

    def SetSolverModel(self, value: str) -> None:
        """
        Set the value of "Solver Model".

        :param value:
            The value to set. Must be one of [\'WCSPH\', \'IISPH\', \'DFSPH\'].
        :raises RockyApiError:
            If `value` is not a valid "Solver Model" option.
        """

    def GetValidSolverModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Solver Model".

        :return:
            The returned list is [\'WCSPH\', \'IISPH\', \'DFSPH\'].
        """

    def GetSoundSpeed(self, unit: str | None = None) -> float:
        """
        Get the value of "Sound Speed".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetSoundSpeed(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Sound Speed".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetStabilityDegree(self) -> int:
        """
        Get the value of "Stability Degree".

        """

    def SetStabilityDegree(self, value: str | int) -> None:
        """
        Set the value of "Stability Degree".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetStabilityNegFactor(self) -> float:
        """
        Get the value of "Stability Neg Factor".

        """

    def SetStabilityNegFactor(self, value: str | float) -> None:
        """
        Set the value of "Stability Neg Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetStabilityPosFactor(self) -> float:
        """
        Get the value of "Stability Pos Factor".

        """

    def SetStabilityPosFactor(self, value: str | float) -> None:
        """
        Set the value of "Stability Pos Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetStiffFactor(self) -> float:
        """
        Get the value of "Stiff Factor".

        """

    def SetStiffFactor(self, value: str | float) -> None:
        """
        Set the value of "Stiff Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSurfaceTensionBoundaryAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Surface Tension Boundary Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetSurfaceTensionBoundaryAngle(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Surface Tension Boundary Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetSurfaceTensionBoundaryFraction(self) -> float:
        """
        Get the value of "Surface Tension Boundary Fraction".

        """

    def SetSurfaceTensionBoundaryFraction(self, value: str | float) -> None:
        """
        Set the value of "Surface Tension Boundary Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSurfaceTensionCoefficient(self, unit: str | None = None) -> float:
        """
        Get the value of "Surface Tension Coefficient".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "N/m".
        """

    def SetSurfaceTensionCoefficient(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Surface Tension Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "N/m".
        """

    def GetSurfaceTensionType(self) -> str:
        """
        Get "Surface Tension Type" as a string.

        :return:
            The returned value will be one of [\'none\', \'CSF\', \'CSS\', \'custom\', \'pairwise_potential\'].
        """

    def SetSurfaceTensionType(self, value: str) -> None:
        """
        Set the value of "Surface Tension Type".

        :param value:
            The value to set. Must be one of [\'none\', \'CSF\', \'CSS\', \'custom\', \'pairwise_potential\'].
        :raises RockyApiError:
            If `value` is not a valid "Surface Tension Type" option.
        """

    def GetValidSurfaceTensionTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Surface Tension Type".

        :return:
            The returned list is [\'none\', \'CSF\', \'CSS\', \'custom\', \'pairwise_potential\'].
        """

    def GetTimestepFactor(self) -> float:
        """
        Get the value of "Timestep Factor".

        """

    def SetTimestepFactor(self, value: str | float) -> None:
        """
        Set the value of "Timestep Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTurbDistanceFraction(self) -> float:
        """
        Get the value of "Turb Distance Fraction".

        """

    def SetTurbDistanceFraction(self, value: str | float) -> None:
        """
        Set the value of "Turb Distance Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTurbulenceType(self) -> str:
        """
        Get "Turbulence Type" as a string.

        :return:
            The returned value will be one of [\'laminar\', \'les\'].
        """

    def SetTurbulenceType(self, value: str) -> None:
        """
        Set the value of "Turbulence Type".

        :param value:
            The value to set. Must be one of [\'laminar\', \'les\'].
        :raises RockyApiError:
            If `value` is not a valid "Turbulence Type" option.
        """

    def GetValidTurbulenceTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Turbulence Type".

        :return:
            The returned list is [\'laminar\', \'les\'].
        """

    def GetTurbulentPrandtl(self) -> float:
        """
        Get the value of "Turbulent Prandtl".

        """

    def SetTurbulentPrandtl(self, value: str | float) -> None:
        """
        Set the value of "Turbulent Prandtl".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTurbulentViscosityMaximumRatio(self) -> float:
        """
        Get the value of "Turbulent Viscosity Maximum Ratio".

        """

    def SetTurbulentViscosityMaximumRatio(self, value: str | float) -> None:
        """
        Set the value of "Turbulent Viscosity Maximum Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetUpdateCoupledDensity(self) -> bool:
        """
        Get the value of "Update Coupled Density".

        """

    def SetUpdateCoupledDensity(self, value: bool) -> None:
        """
        Set the value of "Update Coupled Density".

        :param value:
            The value to set.
        """

    def GetUseParticlesNeighborsList(self) -> bool:
        """
        Get the value of "Use Particles Neighbors List".

        """

    def SetUseParticlesNeighborsList(self, value: bool) -> None:
        """
        Set the value of "Use Particles Neighbors List".

        :param value:
            The value to set.
        """

    def GetViscosityType(self) -> str:
        """
        Get "Viscosity Type" as a string.

        :return:
            The returned value will be one of [\'cleary\', \'morris\', \'custom\'].
        """

    def SetViscosityType(self, value: str) -> None:
        """
        Set the value of "Viscosity Type".

        :param value:
            The value to set. Must be one of [\'cleary\', \'morris\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Viscosity Type" option.
        """

    def GetValidViscosityTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Viscosity Type".

        :return:
            The returned list is [\'cleary\', \'morris\', \'custom\'].
        """

    def GetViscousForceIntegration(self) -> str:
        """
        Get "Viscous Force Integration" as a string.

        :return:
            The returned value will be one of [\'explicit\', \'implicit\'].
        """

    def SetViscousForceIntegration(self, value: str) -> None:
        """
        Set the value of "Viscous Force Integration".

        :param value:
            The value to set. Must be one of [\'explicit\', \'implicit\'].
        :raises RockyApiError:
            If `value` is not a valid "Viscous Force Integration" option.
        """

    def GetValidViscousForceIntegrationValues(self) -> list[str]:
        """
        Get a list of all possible values for "Viscous Force Integration".

        :return:
            The returned list is [\'explicit\', \'implicit\'].
        """

    def GetViscousForceMaximumNumberOfIterations(self) -> int:
        """
        Get the value of "Viscous Force Maximum Number of Iterations".

        """

    def SetViscousForceMaximumNumberOfIterations(self, value: str | int) -> None:
        """
        Set the value of "Viscous Force Maximum Number of Iterations".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetViscousForceRelativeErrorTolerance(self) -> float:
        """
        Get the value of "Viscous Force Relative Error Tolerance".

        """

    def SetViscousForceRelativeErrorTolerance(self, value: str | float) -> None:
        """
        Set the value of "Viscous Force Relative Error Tolerance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetViscousForceUnderRelaxationFactor(self) -> float:
        """
        Get the value of "Viscous Force Under Relaxation Factor".

        """

    def SetViscousForceUnderRelaxationFactor(self, value: str | float) -> None:
        """
        Set the value of "Viscous Force Under Relaxation Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetXsphFactor(self) -> float:
        """
        Get the value of "Xsph Factor".

        """

    def SetXsphFactor(self, value: str | float) -> None:
        """
        Set the value of "Xsph Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetFluidMaterial(self):
        """
        Get the "Fluid Material".

        :rtype: :class:`RAFluidMaterial`
        """

    def SetFluidMaterial(self, value) -> None:
        """
        Set the "Fluid Material".

        :param unicode, :class:`RAFluidMaterial` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableFluidMaterials(self):
        """
        Get all available Fluid Materials.

        :rtype: List[:class:`RAFluidMaterial`]
            A list of :class:`RAFluidMaterial`.
        """
