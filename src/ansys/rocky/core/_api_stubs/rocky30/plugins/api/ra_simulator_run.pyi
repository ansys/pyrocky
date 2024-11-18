from collections.abc import Sequence
from rocky30.models.solver.rocky_simulator_run import RockySimulatorRun as RockySimulatorRun
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import RAGridProcessElementItem as RAGridProcessElementItem
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import ConvertUserPassedValueToScalar as ConvertUserPassedValueToScalar
from typing import List, Optional, Union

class RASimulatorRun(RAGridProcessElementItem):
    @classmethod
    def GetWrappedClass(self) -> type['RockySimulatorRun']: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def RemoveProcess(self) -> None: ...
    def SetTimeConfiguration(self, duration: float, time_interval: float) -> None: ...
    def GetWearGeometryUpdateFrequency(self, unit: Union[str, None] = ...) -> float: ...
    def SetWearGeometryUpdateFrequency(self, value: Union[str, float], unit: Union[str, None] = ...) -> None: ...
    def HasFEMForcesEnabled(self) -> bool: ...
    def HasHtcCalculatedData(self) -> bool: ...
    def EnableHtcCalculator(self) -> None: ...
    def DisableHtcCalculator(self) -> None: ...
    def EnableFEMForces(self) -> None: ...
    def DisableFEMForces(self) -> None: ...
    def SetCollectForcesForFemAnalysis(self, value: bool) -> None: ...
    def GetCollectForcesForFemAnalysis(self) -> bool: ...
    def HasCompressedFileEnabled(self) -> bool: ...
    def GetTargetGpus(self) -> list[int]: ...
    def SetTargetGpus(self, gpus: list[Union[int, str]]) -> None: ...
    def GetWearEnergySpectraBreakageStart(self, unit: Union[str, None] = ...) -> float: ...
    def SetWearEnergySpectraBreakageStart(self, value: Union[str, float], unit: Union[str, None] = ...) -> None: ...
    def GetWearEnergySpectraBreakageDelayAfterRelease(self, unit: Union[str, None] = ...) -> float: ...
    def SetWearEnergySpectraBreakageDelayAfterRelease(self, value: Union[str, float], unit: Union[str, None] = ...) -> None: ...
    def GetSimulationOutputFrequency(self, unit: Union[str, None] = ...) -> float: ...
    def SetSimulationOutputFrequency(self, value: Union[str, float], unit: Union[str, None] = ...) -> None: ...
    def GetSolverCurvesOutputFrequency(self) -> int: ...
    def SetSolverCurvesOutputFrequency(self, value: Union[str, int]) -> None: ...
    def GetFluentOutputsMultiplier(self) -> int: ...
    def SetFluentOutputsMultiplier(self, value: int) -> None: ...
    def GetAvailableOutputRoots(self) -> Sequence[str]: ...
    def GetAvailableOutputRootProperties(self, root_key: str) -> Sequence[str]: ...
    def GetOutputRootEnabled(self, root_key: str) -> bool: ...
    def SetOutputRootEnabled(self, root_key: str, enabled: bool) -> None: ...
    def GetOutputPropertyEnabled(self, root_key: str, property_name: str) -> bool: ...
    def SetOutputPropertyEnabled(self, root_key: str, property_name: str, enabled: bool) -> None: ...
    def GetStandardOutputPropertyEnabled(self, *output_property: str) -> bool: ...
    def SetStandardOutputPropertyEnabled(self, *output_property: str, enabled: bool) -> None: ...
    def GetModulesOutputPropertyEnabled(self, *output_property: str) -> bool: ...
    def SetModulesOutputPropertyEnabled(self, *output_property: str, enabled: bool) -> None: ...
    @staticmethod
    def GetAvailableStandardOutputProperties() -> dict: ...
    @staticmethod
    def GetAvailableModulesOutputProperties() -> dict: ...
    def GetStandardOutputPropertiesData(self) -> dict: ...
    def SetStandardOutputPropertiesData(self, data_dict: dict) -> None: ...
    def GetModulesOutputPropertiesData(self) -> dict: ...
    def SetModulesOutputPropertiesData(self, data_dict: dict) -> None: ...
    def RestoreOutputPropertiesDefaults(self) -> None: ...
    def GetArraysGrowthRate(self) -> float: ...
    def SetArraysGrowthRate(self, value: Union[str, float]) -> None: ...
    def GetBreakageOverlapFactor(self) -> float: ...
    def SetBreakageOverlapFactor(self, value: Union[str, float]) -> None: ...
    def GetDisableTrianglesOnPeriodicBoundaries(self) -> bool: ...
    def SetDisableTrianglesOnPeriodicBoundaries(self, value: bool) -> None: ...
    def GetDragLimiterFactor(self) -> float: ...
    def SetDragLimiterFactor(self, value: Union[str, float]) -> None: ...
    def GetMoveCfdCellsWithRockyBoundaries(self) -> bool: ...
    def SetMoveCfdCellsWithRockyBoundaries(self, value: bool) -> None: ...
    def EnableMoveCfdCellsWithRockyBoundaries(self) -> None: ...
    def DisableMoveCfdCellsWithRockyBoundaries(self) -> None: ...
    def IsMoveCfdCellsWithRockyBoundariesEnabled(self) -> bool: ...
    def GetFixedTimestep(self, unit: Optional[str] = ...) -> float: ...
    def SetFixedTimestep(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetLinearHystDamp(self) -> float: ...
    def SetLinearHystDamp(self, value: Union[str, float]) -> None: ...
    def GetLoadingNSteps(self) -> int: ...
    def SetLoadingNSteps(self, value: Union[str, int]) -> None: ...
    def GetSolverCurvesFrequency(self) -> int: ...
    def SetSolverCurvesFrequency(self, value: Union[str, int]) -> None: ...
    def GetContactNeighboringDistanceBetweenParticles(self, unit: Optional[str] = ...) -> float: ...
    def SetContactNeighboringDistanceBetweenParticles(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetContactNeighboringDistanceBetweenParticlesAndTriangles(self, unit: Optional[str] = ...) -> float: ...
    def SetContactNeighboringDistanceBetweenParticlesAndTriangles(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetNegateInitialOverlaps(self) -> bool: ...
    def SetNegateInitialOverlaps(self, value: bool) -> None: ...
    def EnableNegateInitialOverlaps(self) -> None: ...
    def DisableNegateInitialOverlaps(self) -> None: ...
    def IsNegateInitialOverlapsEnabled(self) -> bool: ...
    def GetNeighborSearchModel(self) -> str: ...
    def SetNeighborSearchModel(self, value: str) -> None: ...
    def GetValidNeighborSearchModelValues(self) -> List[str]: ...
    def GetRefineConcaveSearch(self) -> bool: ...
    def SetRefineConcaveSearch(self, value: bool) -> None: ...
    def GetParticleSizeLimitForReordering(self, unit: Optional[str] = ...) -> float: ...
    def SetParticleSizeLimitForReordering(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSpecialReorderingForWidePsd(self) -> bool: ...
    def SetSpecialReorderingForWidePsd(self, value: bool) -> None: ...
    def GetResetOnlyPhysicalContactsData(self) -> bool: ...
    def SetResetOnlyPhysicalContactsData(self, value: bool) -> None: ...
    def GetSortingDistanceFactor(self) -> float: ...
    def SetSortingDistanceFactor(self, value: Union[str, float]) -> None: ...
    def GetTimestepModel(self) -> str: ...
    def SetTimestepModel(self, value: str) -> None: ...
    def GetValidTimestepModelValues(self) -> List[str]: ...
    def GetUse2023R2SourceTermsApproach(self) -> bool: ...
    def SetUse2023R2SourceTermsApproach(self, value: bool) -> None: ...
    def GetUse2023R2CellVolumeFractionUpdateApproach(self) -> bool: ...
    def SetUse2023R2CellVolumeFractionUpdateApproach(self, value: bool) -> None: ...
    def GetUseArraysGrowthRate(self) -> bool: ...
    def SetUseArraysGrowthRate(self, value: bool) -> None: ...
    def GetUseBreakageOverlapFactor(self) -> bool: ...
    def SetUseBreakageOverlapFactor(self, value: bool) -> None: ...
    def GetUse3RdPowerForCfdCgm(self) -> bool: ...
    def SetUse3RdPowerForCfdCgm(self, value: bool) -> None: ...
    def EnableUse3RdPowerForCfdCgm(self) -> None: ...
    def DisableUse3RdPowerForCfdCgm(self) -> None: ...
    def IsUse3RdPowerForCfdCgmEnabled(self) -> bool: ...
    def GetUseDpmBlockingEffectForSinglePhaseSimulations(self) -> bool: ...
    def SetUseDpmBlockingEffectForSinglePhaseSimulations(self, value: bool) -> None: ...
    def EnableDpmBlockingEffectForSinglePhaseSimulations(self) -> None: ...
    def DisableDpmBlockingEffectForSinglePhaseSimulations(self) -> None: ...
    def IsDpmBlockingEffectForSinglePhaseSimulationsEnabled(self) -> bool: ...
    def GetUseDragLimiterFactor(self) -> bool: ...
    def SetUseDragLimiterFactor(self, value: bool) -> None: ...
    def GetUseFixedTimestep(self) -> bool: ...
    def SetUseFixedTimestep(self, value: bool) -> None: ...
    def GetUseContactNeighboringDistanceBetweenParticles(self) -> bool: ...
    def SetUseContactNeighboringDistanceBetweenParticles(self, value: bool) -> None: ...
    def GetUseContactNeighboringDistanceBetweenParticlesAndTriangles(self) -> bool: ...
    def SetUseContactNeighboringDistanceBetweenParticlesAndTriangles(self, value: bool) -> None: ...
    def GetUseNonRoundTorqueCorrection(self) -> bool: ...
    def SetUseNonRoundTorqueCorrection(self, value: bool) -> None: ...
    def GetUseSortingDistanceFactor(self) -> bool: ...
    def SetUseSortingDistanceFactor(self, value: bool) -> None: ...
    def EnableSortingDistanceFactor(self) -> None: ...
    def DisableSortingDistanceFactor(self) -> None: ...
    def IsSortingDistanceFactorEnabled(self) -> bool: ...
    def GetUseCompressedFiles(self) -> bool: ...
    def SetUseCompressedFiles(self, value: bool) -> None: ...
    def EnableCompressedFile(self) -> None: ...
    def DisableCompressedFile(self) -> None: ...
    def IsCompressedFileEnabled(self) -> bool: ...
    def GetMultiGpuSlicingDirection(self) -> str: ...
    def SetMultiGpuSlicingDirection(self, value: str) -> None: ...
    def GetValidMultiGpuSlicingDirectionValues(self) -> List[str]: ...
    def GetNumberOfProcessors(self) -> int: ...
    def SetNumberOfProcessors(self, value: Union[str, int]) -> None: ...
    def GetReleaseParticlesWithoutOverlapCheck(self) -> bool: ...
    def SetReleaseParticlesWithoutOverlapCheck(self, value: bool) -> None: ...
    def GetSimulationTarget(self) -> str: ...
    def SetSimulationTarget(self, value: str) -> None: ...
    def GetValidSimulationTargetValues(self) -> List[str]: ...
    def GetTargetGpu(self) -> int: ...
    def SetTargetGpu(self, value: Union[str, int]) -> None: ...
    def GetResumeDataFrequency(self) -> int: ...
    def SetResumeDataFrequency(self, value: Union[str, int]) -> None: ...
    def GetBreakageDelayAfterRelease(self, unit: Optional[str] = ...) -> float: ...
    def SetBreakageDelayAfterRelease(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBreakageStart(self, unit: Optional[str] = ...) -> float: ...
    def SetBreakageStart(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTimeInterval(self, unit: Optional[str] = ...) -> float: ...
    def SetTimeInterval(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetOverlapParticlesDelay(self, unit: Optional[str] = ...) -> float: ...
    def SetOverlapParticlesDelay(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSimulationDuration(self, unit: Optional[str] = ...) -> float: ...
    def SetSimulationDuration(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetWearGeometryUpdateInterval(self, unit: Optional[str] = ...) -> float: ...
    def SetWearGeometryUpdateInterval(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetWearStart(self, unit: Optional[str] = ...) -> float: ...
    def SetWearStart(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
