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

from collections.abc import Sequence

from rocky30.models.solver.rocky_simulator_run import (
    RockySimulatorRun as RockySimulatorRun,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToScalar as ConvertUserPassedValueToScalar,
)

class RASimulatorRun(RAGridProcessElementItem):
    """
    Rocky PrePost Scripting wrapper for solver settings.

    This wrapper corresponds to the "Solver" item on a project\'s data tree. Access it from the
    :class:`RAStudy` with:

    .. code-block:: python

        simulator_run = study.GetSimulatorRun()
    """

    @classmethod
    def GetWrappedClass(self) -> type["RockySimulatorRun"]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def RemoveProcess(self) -> None:
        """
        It is not possible to remove the item "Solver" from the project. It\'s a standard Rocky
        item in project.
        """

    def SetTimeConfiguration(self, duration: float, time_interval: float) -> None:
        """
        Shortcut to set both the simulation's duration and its time interval.

        :param duration:
            The simulation duration (in seconds).

        :param time_interval:
            The simulation time interval (in seconds).
        """

    def HasFEMForcesEnabled(self) -> bool:
        """
        Whether the simulation is configured to collect forces for FEM analysis.
        """

    def HasHtcCalculatedData(self) -> bool:
        """
        Whether the "HTC" is being calculated.
        """

    def EnableHtcCalculator(self) -> None:
        """
        Enables the "HTC" calculations.
        """

    def DisableHtcCalculator(self) -> None:
        """
        Disables the "HTC" calculations.
        """

    def EnableFEMForces(self) -> None:
        """
        Enables the "FEM Forces" calculations.
        """

    def DisableFEMForces(self) -> None:
        """
        Disables the "FEM Forces" calculations.
        """

    def HasCompressedFileEnabled(self) -> bool: ...
    def GetTargetGpus(self) -> list[int]:
        """
        :return: A list of IDs of the GPUs currently selected for Multi GPU simulation.
        """

    def SetTargetGpus(self, gpus: list[int | str]) -> None:
        """
        It will configure the IDs of GPUs that will be used in simulation based on the list of IDs or names of GPUs
        passed.

        :param gpus:
            List with IDs or names of GPUs to be used in simulation.
            For example in the name "1 - Geforce GTX 980", the ID is 1 and the name is "1 - Geforce GTX 980".
        """

    def GetFluentOutputsMultiplier(self) -> int:
        """
        Get the value of "Fluent Outputs Multiplier".
        """

    def SetFluentOutputsMultiplier(self, value: int) -> None:
        """
        Set the value of "Fluent Outputs Multiplier".

        :param value:
            The value to set.
        """

    def GetAvailableOutputRoots(self) -> Sequence[str]:
        """
        Deprecated: Use GetAvailableStandardOutputProperties instead.
        """

    def GetAvailableOutputRootProperties(self, root_key: str) -> Sequence[str]:
        """
        Deprecated: Use GetAvailableStandardOutputProperties instead.
        """

    def GetOutputRootEnabled(self, root_key: str) -> bool:
        """
        Deprecated: Use GetStandardOutputPropertyEnabled instead.
        """

    def SetOutputRootEnabled(self, root_key: str, enabled: bool) -> None:
        """
        Deprecated: Use SetStandardOutputPropertyEnabled instead.
        """

    def GetOutputPropertyEnabled(self, root_key: str, property_name: str) -> bool:
        """
        Deprecated: Use GetStandardOutputPropertyEnabled instead.
        """

    def SetOutputPropertyEnabled(
        self, root_key: str, property_name: str, enabled: bool
    ) -> None:
        """
        Deprecated: Use SetStandardOutputPropertyEnabled instead.
        """

    def GetStandardOutputPropertyEnabled(self, *output_property: str) -> bool:
        """
        Retrieve enable state of given "Standard Output Property".

        :param output_property:
            The output property name.
        """

    def SetStandardOutputPropertyEnabled(
        self, *output_property: str, enabled: bool
    ) -> None:
        """
        Set enable state of given "Standard Output Property".

        :param output_property:
            The output property name.
        :param enabled:
            The enable state of given "Standard Output Property".
        """

    def GetModulesOutputPropertyEnabled(self, *output_property: str) -> bool:
        """
        Retrieve enable state of given "Modules Output Property".

        :param output_property:
            The output property name.
        """

    def SetModulesOutputPropertyEnabled(
        self, *output_property: str, enabled: bool
    ) -> None:
        """
        Set enable state of given "Modules Output Property".

        :param output_property:
            The output property name.
        :param enabled:
            The enable state of given "Modules Output Property".
        """

    @staticmethod
    def GetAvailableStandardOutputProperties() -> dict:
        """
        :returns: The available "Standard Output Properties".
        """

    @staticmethod
    def GetAvailableModulesOutputProperties() -> dict:
        """
        :returns: The available "Modules Output Properties".
        """

    def GetStandardOutputPropertiesData(self) -> dict:
        """
        :returns: The current value of "Standard Output Properties".
        """

    def SetStandardOutputPropertiesData(self, data_dict: dict) -> None:
        """
        Set the current value of "Standard Output Properties".

        :param data_dict:
            The data dictionary to set.
        """

    def GetModulesOutputPropertiesData(self) -> dict:
        """
        :returns: The current value of "Modules Output Properties".
        """

    def SetModulesOutputPropertiesData(self, data_dict: dict) -> None:
        """
        Set the current value of "Modules Output Properties".

        :param data_dict:
            The data dictionary to set.
        """

    def RestoreOutputPropertiesDefaults(self) -> None:
        """
        Restore default values of "Output Properties".
        """

    def GetUseDpmBlockingEffectForSinglePhaseSimulations(self) -> bool:
        """
        The "Use DPM Blocking Effect For Single Phase Simulations" parameter was removed from Rocky
        since 25R2.
        """

    def SetUseDpmBlockingEffectForSinglePhaseSimulations(self, value: bool) -> None:
        """
        The "Use DPM Blocking Effect For Single Phase Simulations" parameter was removed from Rocky
        since 25R2.
        """

    def EnableDpmBlockingEffectForSinglePhaseSimulations(self) -> None:
        """
        The "Use DPM Blocking Effect For Single Phase Simulations" parameter was removed from Rocky
        since 25R2.
        """

    def DisableDpmBlockingEffectForSinglePhaseSimulations(self) -> None:
        """
        The "Use DPM Blocking Effect For Single Phase Simulations" parameter was removed from Rocky
        since 25R2.
        """

    def IsDpmBlockingEffectForSinglePhaseSimulationsEnabled(self) -> bool:
        """
        The "Use DPM Blocking Effect For Single Phase Simulations" parameter was removed from Rocky
        since 25R2.
        """

    def GetSimulationTarget(self) -> str: ...
    def SetSimulationTarget(self, value: str) -> None: ...
    def GetArraysGrowthRate(self) -> float:
        """
        Get the value of "Arrays Growth Rate".

        """

    def SetArraysGrowthRate(self, value: str | float) -> None:
        """
        Set the value of "Arrays Growth Rate".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetBreakageOverlapFactor(self) -> float:
        """
        Get the value of "Breakage Overlap Factor".

        """

    def SetBreakageOverlapFactor(self, value: str | float) -> None:
        """
        Set the value of "Breakage Overlap Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDisableTrianglesOnPeriodicBoundaries(self) -> bool:
        """
        Get the value of "Disable Triangles On Periodic Boundaries".

        """

    def SetDisableTrianglesOnPeriodicBoundaries(self, value: bool) -> None:
        """
        Set the value of "Disable Triangles On Periodic Boundaries".

        :param value:
            The value to set.
        """

    def GetDragLimiterFactor(self) -> float:
        """
        Get the value of "Drag Limiter Factor".

        """

    def SetDragLimiterFactor(self, value: str | float) -> None:
        """
        Set the value of "Drag Limiter Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMoveCfdCellsWithRockyBoundaries(self) -> bool:
        """
        Get the value of "Move Cfd Cells With Rocky Boundaries".

        """

    def SetMoveCfdCellsWithRockyBoundaries(self, value: bool) -> None:
        """
        Set the value of "Move Cfd Cells With Rocky Boundaries".

        :param value:
            The value to set.
        """

    def EnableMoveCfdCellsWithRockyBoundaries(self) -> None:
        """
        Set the value of "Move Cfd Cells With Rocky Boundaries" to True.
        """

    def DisableMoveCfdCellsWithRockyBoundaries(self) -> None:
        """
        Set the value of "Move Cfd Cells With Rocky Boundaries" to False.
        """

    def IsMoveCfdCellsWithRockyBoundariesEnabled(self) -> bool:
        """
        Check if the "Move Cfd Cells With Rocky Boundaries" is enabled.

        """

    def GetFixedTimestep(self, unit: str | None = None) -> float:
        """
        Get the value of "Fixed Timestep".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetFixedTimestep(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Fixed Timestep".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetSuccessiveOverRelaxationTolerance(self) -> float:
        """
        Get the value of "Successive Over Relaxation Tolerance".

        """

    def SetSuccessiveOverRelaxationTolerance(self, value: str | float) -> None:
        """
        Set the value of "Successive Over Relaxation Tolerance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetJointElasticRatio(self) -> float:
        """
        Get the value of "Joint Elastic Ratio".

        """

    def SetJointElasticRatio(self, value: str | float) -> None:
        """
        Set the value of "Joint Elastic Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMinimumLengthDeformationTolerance(self) -> float:
        """
        Get the value of "Minimum Length Deformation Tolerance".

        """

    def SetMinimumLengthDeformationTolerance(self, value: str | float) -> None:
        """
        Set the value of "Minimum Length Deformation Tolerance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetLinearHystDamp(self) -> float:
        """
        Get the value of "Linear Hyst Damp".

        """

    def SetLinearHystDamp(self, value: str | float) -> None:
        """
        Set the value of "Linear Hyst Damp".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetLoadingNSteps(self) -> int:
        """
        Get the value of "Loading N Steps".

        """

    def SetLoadingNSteps(self, value: str | int) -> None:
        """
        Set the value of "Loading N Steps".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetDeformableMassMatrixType(self) -> str:
        """
        Get "Deformable Mass Matrix Type" as a string.

        :return:
            The returned value will be one of [\'lumped\', \'consistent\'].
        """

    def SetDeformableMassMatrixType(self, value: str) -> None:
        """
        Set the value of "Deformable Mass Matrix Type".

        :param value:
            The value to set. Must be one of [\'lumped\', \'consistent\'].
        :raises RockyApiError:
            If `value` is not a valid "Deformable Mass Matrix Type" option.
        """

    def GetValidDeformableMassMatrixTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Deformable Mass Matrix Type".

        :return:
            The returned list is [\'lumped\', \'consistent\'].
        """

    def GetMinimumVolumeTolerance(self) -> float:
        """
        Get the value of "Minimum Volume Tolerance".

        """

    def SetMinimumVolumeTolerance(self, value: str | float) -> None:
        """
        Set the value of "Minimum Volume Tolerance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSolverCurvesFrequency(self) -> int:
        """
        Get the value of "Solver Curves Frequency".

        """

    def SetSolverCurvesFrequency(self, value: str | int) -> None:
        """
        Set the value of "Solver Curves Frequency".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetContactNeighboringDistanceBetweenParticles(
        self, unit: str | None = None
    ) -> float:
        """
        Get the value of "Contact Neighboring Distance Between Particles".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetContactNeighboringDistanceBetweenParticles(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Contact Neighboring Distance Between Particles".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetContactNeighboringDistanceBetweenParticlesAndTriangles(
        self, unit: str | None = None
    ) -> float:
        """
        Get the value of "Contact Neighboring Distance Between Particles And Triangles".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetContactNeighboringDistanceBetweenParticlesAndTriangles(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Contact Neighboring Distance Between Particles And Triangles".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetNegateInitialOverlaps(self) -> bool:
        """
        Get the value of "Negate Initial Overlaps".

        """

    def SetNegateInitialOverlaps(self, value: bool) -> None:
        """
        Set the value of "Negate Initial Overlaps".

        :param value:
            The value to set.
        """

    def EnableNegateInitialOverlaps(self) -> None:
        """
        Set the value of "Negate Initial Overlaps" to True.
        """

    def DisableNegateInitialOverlaps(self) -> None:
        """
        Set the value of "Negate Initial Overlaps" to False.
        """

    def IsNegateInitialOverlapsEnabled(self) -> bool:
        """
        Check if the "Negate Initial Overlaps" is enabled.

        """

    def GetNeighborSearchModel(self) -> str:
        """
        Get "Neighbor Search Model" as a string.

        :return:
            The returned value will be one of [\'BVH\', \'RegularGrid\', \'SparseGrid\'].
        """

    def SetNeighborSearchModel(self, value: str) -> None:
        """
        Set the value of "Neighbor Search Model".

        :param value:
            The value to set. Must be one of [\'BVH\', \'RegularGrid\', \'SparseGrid\'].
        :raises RockyApiError:
            If `value` is not a valid "Neighbor Search Model" option.
        """

    def GetValidNeighborSearchModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Neighbor Search Model".

        :return:
            The returned list is [\'BVH\', \'RegularGrid\', \'SparseGrid\'].
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

    def GetOverRelaxationCoefficient(self) -> float:
        """
        Get the value of "Over Relaxation Coefficient".

        """

    def SetOverRelaxationCoefficient(self, value: str | float) -> None:
        """
        Set the value of "Over Relaxation Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetRefineConcaveSearch(self) -> bool:
        """
        Get the value of "Refine Concave Search".

        """

    def SetRefineConcaveSearch(self, value: bool) -> None:
        """
        Set the value of "Refine Concave Search".

        :param value:
            The value to set.
        """

    def GetParticleSizeLimitForReordering(self, unit: str | None = None) -> float:
        """
        Get the value of "Particle Size Limit For Reordering".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetParticleSizeLimitForReordering(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Particle Size Limit For Reordering".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetSpecialReorderingForWidePsd(self) -> bool:
        """
        Get the value of "Special Reordering For Wide Psd".

        """

    def SetSpecialReorderingForWidePsd(self, value: bool) -> None:
        """
        Set the value of "Special Reordering For Wide Psd".

        :param value:
            The value to set.
        """

    def GetResetOnlyPhysicalContactsData(self) -> bool:
        """
        Get the value of "Reset Only Physical Contacts Data".

        """

    def SetResetOnlyPhysicalContactsData(self, value: bool) -> None:
        """
        Set the value of "Reset Only Physical Contacts Data".

        :param value:
            The value to set.
        """

    def GetSortingDistanceFactor(self) -> float:
        """
        Get the value of "Sorting Distance Factor".

        """

    def SetSortingDistanceFactor(self, value: str | float) -> None:
        """
        Set the value of "Sorting Distance Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTimestepModel(self) -> str:
        """
        Get "Timestep Model" as a string.

        :return:
            The returned value will be one of [\'constant\', \'variable\'].
        """

    def SetTimestepModel(self, value: str) -> None:
        """
        Set the value of "Timestep Model".

        :param value:
            The value to set. Must be one of [\'constant\', \'variable\'].
        :raises RockyApiError:
            If `value` is not a valid "Timestep Model" option.
        """

    def GetValidTimestepModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Timestep Model".

        :return:
            The returned list is [\'constant\', \'variable\'].
        """

    def GetUse2023R2SourceTermsApproach(self) -> bool:
        """
        Get the value of "Use 2023 R2 Source Terms Approach".

        """

    def SetUse2023R2SourceTermsApproach(self, value: bool) -> None:
        """
        Set the value of "Use 2023 R2 Source Terms Approach".

        :param value:
            The value to set.
        """

    def GetUse2023R2CellVolumeFractionUpdateApproach(self) -> bool:
        """
        Get the value of "Use 2023 R2 Cell Volume Fraction Update Approach".

        """

    def SetUse2023R2CellVolumeFractionUpdateApproach(self, value: bool) -> None:
        """
        Set the value of "Use 2023 R2 Cell Volume Fraction Update Approach".

        :param value:
            The value to set.
        """

    def GetUseArraysGrowthRate(self) -> bool:
        """
        Get the value of "Use Arrays Growth Rate".

        """

    def SetUseArraysGrowthRate(self, value: bool) -> None:
        """
        Set the value of "Use Arrays Growth Rate".

        :param value:
            The value to set.
        """

    def GetUseBreakageOverlapFactor(self) -> bool:
        """
        Get the value of "Use Breakage Overlap Factor".

        """

    def SetUseBreakageOverlapFactor(self, value: bool) -> None:
        """
        Set the value of "Use Breakage Overlap Factor".

        :param value:
            The value to set.
        """

    def GetUse3RdPowerForCfdCgm(self) -> bool:
        """
        Get the value of "Use 3Rd Power For Cfd Cgm".

        """

    def SetUse3RdPowerForCfdCgm(self, value: bool) -> None:
        """
        Set the value of "Use 3Rd Power For Cfd Cgm".

        :param value:
            The value to set.
        """

    def EnableUse3RdPowerForCfdCgm(self) -> None:
        """
        Set the value of "Use 3Rd Power For Cfd Cgm" to True.
        """

    def DisableUse3RdPowerForCfdCgm(self) -> None:
        """
        Set the value of "Use 3Rd Power For Cfd Cgm" to False.
        """

    def IsUse3RdPowerForCfdCgmEnabled(self) -> bool:
        """
        Check if the "Use 3Rd Power For Cfd Cgm" is enabled.

        """

    def GetUseDragLimiterFactor(self) -> bool:
        """
        Get the value of "Use Drag Limiter Factor".

        """

    def SetUseDragLimiterFactor(self, value: bool) -> None:
        """
        Set the value of "Use Drag Limiter Factor".

        :param value:
            The value to set.
        """

    def GetUseFixedTimestep(self) -> bool:
        """
        Get the value of "Use Fixed Timestep".

        """

    def SetUseFixedTimestep(self, value: bool) -> None:
        """
        Set the value of "Use Fixed Timestep".

        :param value:
            The value to set.
        """

    def GetUseContactNeighboringDistanceBetweenParticles(self) -> bool:
        """
        Get the value of "Use Contact Neighboring Distance Between Particles".

        """

    def SetUseContactNeighboringDistanceBetweenParticles(self, value: bool) -> None:
        """
        Set the value of "Use Contact Neighboring Distance Between Particles".

        :param value:
            The value to set.
        """

    def GetUseContactNeighboringDistanceBetweenParticlesAndTriangles(self) -> bool:
        """
        Get the value of "Use Contact Neighboring Distance Between Particles And Triangles".

        """

    def SetUseContactNeighboringDistanceBetweenParticlesAndTriangles(
        self, value: bool
    ) -> None:
        """
        Set the value of "Use Contact Neighboring Distance Between Particles And Triangles".

        :param value:
            The value to set.
        """

    def GetUseNonRoundTorqueCorrection(self) -> bool:
        """
        Get the value of "Use Non Round Torque Correction".

        """

    def SetUseNonRoundTorqueCorrection(self, value: bool) -> None:
        """
        Set the value of "Use Non Round Torque Correction".

        :param value:
            The value to set.
        """

    def GetUseSortingDistanceFactor(self) -> bool:
        """
        Get the value of "Use Sorting Distance Factor".

        """

    def SetUseSortingDistanceFactor(self, value: bool) -> None:
        """
        Set the value of "Use Sorting Distance Factor".

        :param value:
            The value to set.
        """

    def EnableSortingDistanceFactor(self) -> None:
        """
        Set the value of "Sorting Distance Factor" to True.
        """

    def DisableSortingDistanceFactor(self) -> None:
        """
        Set the value of "Sorting Distance Factor" to False.
        """

    def IsSortingDistanceFactorEnabled(self) -> bool:
        """
        Check if the "Sorting Distance Factor" is enabled.

        """

    def GetUseCompressedFiles(self) -> bool:
        """
        Get the value of "Use Compressed Files".

        """

    def SetUseCompressedFiles(self, value: bool) -> None:
        """
        Set the value of "Use Compressed Files".

        :param value:
            The value to set.
        """

    def EnableCompressedFile(self) -> None:
        """
        Set the value of "Compressed File" to True.
        """

    def DisableCompressedFile(self) -> None:
        """
        Set the value of "Compressed File" to False.
        """

    def IsCompressedFileEnabled(self) -> bool:
        """
        Check if the "Compressed File" is enabled.

        """

    def GetMpiHeterogeneous(self) -> bool:
        """
        Get the value of "Mpi Heterogeneous".

        """

    def SetMpiHeterogeneous(self, value: bool) -> None:
        """
        Set the value of "Mpi Heterogeneous".

        :param value:
            The value to set.
        """

    def GetMpiHostfile(self) -> str:
        """
        Get the value of "Mpi Hostfile".

        """

    def SetMpiHostfile(self, value: str) -> None:
        """
        Set the value of "Mpi Hostfile".

        :param value:
            The value to set.
        """

    def GetMpiHosts(self) -> str:
        """
        Get the value of "Mpi Hosts".

        """

    def SetMpiHosts(self, value: str) -> None:
        """
        Set the value of "Mpi Hosts".

        :param value:
            The value to set.
        """

    def GetMpiNumberOfProcesses(self) -> int:
        """
        Get the value of "Mpi Number of Processes".

        """

    def SetMpiNumberOfProcesses(self, value: str | int) -> None:
        """
        Set the value of "Mpi Number of Processes".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetMpiNumberOfThreads(self) -> int:
        """
        Get the value of "Mpi Number of Threads".

        """

    def SetMpiNumberOfThreads(self, value: str | int) -> None:
        """
        Set the value of "Mpi Number of Threads".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetMpiWithinScheduler(self) -> bool:
        """
        Get the value of "Mpi Within Scheduler".

        """

    def SetMpiWithinScheduler(self, value: bool) -> None:
        """
        Set the value of "Mpi Within Scheduler".

        :param value:
            The value to set.
        """

    def GetMultiGpuSlicingDirection(self) -> str:
        """
        Get "Multi Gpu Slicing Direction" as a string.

        :return:
            The returned value will be one of [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        """

    def SetMultiGpuSlicingDirection(self, value: str) -> None:
        """
        Set the value of "Multi Gpu Slicing Direction".

        :param value:
            The value to set. Must be one of [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        :raises RockyApiError:
            If `value` is not a valid "Multi Gpu Slicing Direction" option.
        """

    def GetValidMultiGpuSlicingDirectionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Multi Gpu Slicing Direction".

        :return:
            The returned list is [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        """

    def GetNumberOfProcessors(self) -> int:
        """
        Get the value of "Number of Processors".

        """

    def SetNumberOfProcessors(self, value: str | int) -> None:
        """
        Set the value of "Number of Processors".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetProcessingUnit(self) -> str:
        """
        Get "Processing Unit" as a string.

        :return:
            The returned value will be one of [\'CPU\', \'GPU\', \'MULTI_GPU\'].
        """

    def SetProcessingUnit(self, value: str) -> None:
        """
        Set the value of "Processing Unit".

        :param value:
            The value to set. Must be one of [\'CPU\', \'GPU\', \'MULTI_GPU\'].
        :raises RockyApiError:
            If `value` is not a valid "Processing Unit" option.
        """

    def GetValidProcessingUnitValues(self) -> list[str]:
        """
        Get a list of all possible values for "Processing Unit".

        :return:
            The returned list is [\'CPU\', \'GPU\', \'MULTI_GPU\'].
        """

    def GetReleaseParticlesWithoutOverlapCheck(self) -> bool:
        """
        Get the value of "Release Particles Without Overlap Check".

        """

    def SetReleaseParticlesWithoutOverlapCheck(self, value: bool) -> None:
        """
        Set the value of "Release Particles Without Overlap Check".

        :param value:
            The value to set.
        """

    def GetTargetGpu(self) -> int:
        """
        Get the value of "Target Gpu".

        """

    def SetTargetGpu(self, value: str | int) -> None:
        """
        Set the value of "Target Gpu".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetUseMpi(self) -> bool:
        """
        Get the value of "Use Mpi".

        """

    def SetUseMpi(self, value: bool) -> None:
        """
        Set the value of "Use Mpi".

        :param value:
            The value to set.
        """

    def GetResumeDataFrequency(self) -> int:
        """
        Get the value of "Resume Data Frequency".

        """

    def SetResumeDataFrequency(self, value: str | int) -> None:
        """
        Set the value of "Resume Data Frequency".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetBreakageDelayAfterRelease(self, unit: str | None = None) -> float:
        """
        Get the value of "Breakage Delay After Release".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetBreakageDelayAfterRelease(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Breakage Delay After Release".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetBreakageStart(self, unit: str | None = None) -> float:
        """
        Get the value of "Breakage Start".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetBreakageStart(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Breakage Start".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetTimeInterval(self, unit: str | None = None) -> float:
        """
        Get the value of "Time Interval".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetTimeInterval(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Time Interval".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetOverlapParticlesDelay(self, unit: str | None = None) -> float:
        """
        Get the value of "Overlap Particles Delay".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetOverlapParticlesDelay(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Overlap Particles Delay".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetSimulationDuration(self, unit: str | None = None) -> float:
        """
        Get the value of "Simulation Duration".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetSimulationDuration(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Simulation Duration".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetWearGeometryUpdateInterval(self, unit: str | None = None) -> float:
        """
        Get the value of "Wear Geometry Update Interval".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetWearGeometryUpdateInterval(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Wear Geometry Update Interval".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetWearStart(self, unit: str | None = None) -> float:
        """
        Get the value of "Wear Start".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetWearStart(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Wear Start".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """
