from collections.abc import Sequence
from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import ElementWithAddins as ElementWithAddins
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import RAGridProcessElementItem as RAGridProcessElementItem
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle_assembly import RAParticleAssemblyCustom as RAParticleAssemblyCustom, RAParticleAssemblyPartList as RAParticleAssemblyPartList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_size_distribution import RASizeDistributionList as RASizeDistributionList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated
from typing import List, Optional, Union

class RAParticle(RAGridProcessElementItem, ElementWithAddins, _RAOrientationMixin):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def ImportFromSTL(self, stl_filename: str, as_concave: bool, is_open: bool = ...) -> bool: ...
    def ImportFiberFromTXT(self, stl_filename): ...
    def ImportCustomFiber(self, filename: str) -> bool: ...
    def GetSizeDistributionList(self) -> RASizeDistributionList: ...
    def GetUseMultipleElements(self) -> bool: ...
    def SetUseMultipleElements(self, value) -> None: ...
    def IsConcave(self): ...
    def GetBreakageModel(self) -> str: ...
    def GetValidBreakageModelValues(self) -> list[str]: ...
    def SetBreakageModel(self, value: str) -> None: ...
    def GetAssemblyParts(self) -> RAParticleAssemblyPartList: ...
    def GetAssemblyCustom(self) -> RAParticleAssemblyCustom: ...
    def GetRotationAngle(self, unit: str = ...) -> float: ...
    def SetRotationAngle(self, value: Union[str, float], unit: str = ...) -> None: ...
    def GetRotationVector(self, unit: str = ...) -> list[float]: ...
    def SetRotationVector(self, values: Sequence[Union[str, float]], unit: str = ...) -> None: ...
    def GetAbt10MaximumT10Value(self, unit: Optional[str] = ...) -> float: ...
    def SetAbt10MaximumT10Value(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetAbt10ReferenceMinimumSpecificEnergy(self, unit: Optional[str] = ...) -> float: ...
    def SetAbt10ReferenceMinimumSpecificEnergy(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetAbt10MinimumSpecificEnergy(self, unit: Optional[str] = ...) -> float: ...
    def SetAbt10MinimumSpecificEnergy(self, value: float, unit: Optional[str] = ...) -> None: ...
    def GetAbt10ReferenceSize(self, unit: Optional[str] = ...) -> float: ...
    def SetAbt10ReferenceSize(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetAbt10SelectFunctionCoefficient(self, unit: Optional[str] = ...) -> float: ...
    def SetAbt10SelectFunctionCoefficient(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDistributionModel(self) -> str: ...
    def SetDistributionModel(self, value: str) -> None: ...
    def GetValidDistributionModelValues(self) -> List[str]: ...
    def GetSurfaceEnergy(self, unit: Optional[str] = ...) -> float: ...
    def SetSurfaceEnergy(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetIncludeRotationalDeformations(self) -> bool: ...
    def SetIncludeRotationalDeformations(self, value: bool) -> None: ...
    def EnableIncludeRotationalDeformations(self) -> None: ...
    def DisableIncludeRotationalDeformations(self) -> None: ...
    def IsIncludeRotationalDeformationsEnabled(self) -> bool: ...
    def GetMinimumSize(self, unit: Optional[str] = ...) -> float: ...
    def SetMinimumSize(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMinimumSizeRatio(self) -> float: ...
    def SetMinimumSizeRatio(self, value: Union[str, float]) -> None: ...
    def GetMinimumVolumeFractionForFragmentDisabling(self) -> float: ...
    def SetMinimumVolumeFractionForFragmentDisabling(self, value: Union[str, float]) -> None: ...
    def GetTavaresA(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresA(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresB(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresB(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresD0(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresD0(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresEInf(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresEInf(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresGamma(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresGamma(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresMinimumEnergy(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresMinimumEnergy(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresPhi(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresPhi(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresRatioEmax(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresRatioEmax(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetRatioEnergyAfterBreakage(self, unit: Optional[str] = ...) -> float: ...
    def SetRatioEnergyAfterBreakage(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTavaresSigmaSquared(self, unit: Optional[str] = ...) -> float: ...
    def SetTavaresSigmaSquared(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetT10Formula(self) -> str: ...
    def SetT10Formula(self, value: str) -> None: ...
    def GetValidT10FormulaValues(self) -> List[str]: ...
    def GetShearStressLimit(self, unit: Optional[str] = ...) -> float: ...
    def SetShearStressLimit(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTensileStressLimit(self, unit: Optional[str] = ...) -> float: ...
    def SetTensileStressLimit(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetEnableBreakage(self) -> bool: ...
    def SetEnableBreakage(self, value: bool) -> None: ...
    def EnableBreakage(self) -> None: ...
    def DisableBreakage(self) -> None: ...
    def IsBreakageEnabled(self) -> bool: ...
    def GetVonMisesStressLimit(self, unit: Optional[str] = ...) -> float: ...
    def SetVonMisesStressLimit(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetFlexible(self) -> bool: ...
    def SetFlexible(self, value: bool) -> None: ...
    def GetCenterOfMassOffset(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetCenterOfMassOffset(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetChangeMassProperties(self) -> bool: ...
    def SetChangeMassProperties(self, value: bool) -> None: ...
    def GetEnableRotations(self) -> bool: ...
    def SetEnableRotations(self, value: bool) -> None: ...
    def GetHorizontalAspectRatio(self) -> float: ...
    def SetHorizontalAspectRatio(self, value: Union[str, float]) -> None: ...
    def GetPrincipalMomentOfInertia(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetPrincipalMomentOfInertia(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetNumberOfCorners(self) -> int: ...
    def SetNumberOfCorners(self, value: Union[str, int]) -> None: ...
    def GetXDirection(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetXDirection(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetYDirection(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetYDirection(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetZDirection(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetZDirection(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetRollingResistance(self) -> float: ...
    def SetRollingResistance(self, value: Union[str, float]) -> None: ...
    def GetSideAngle(self) -> float: ...
    def SetSideAngle(self, value: Union[str, float]) -> None: ...
    def GetSmoothness(self) -> float: ...
    def SetSmoothness(self, value: Union[str, float]) -> None: ...
    def GetSuperquadricDegree(self) -> float: ...
    def SetSuperquadricDegree(self, value: Union[str, float]) -> None: ...
    def GetThickness(self, unit: Optional[str] = ...) -> float: ...
    def SetThickness(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetVerticalAspectRatio(self) -> float: ...
    def SetVerticalAspectRatio(self, value: Union[str, float]) -> None: ...
    def GetBendingAngleLimit(self, unit: Optional[str] = ...) -> float: ...
    def SetBendingAngleLimit(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetWithFailure(self) -> bool: ...
    def SetWithFailure(self, value: bool) -> None: ...
    def GetEdgeAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetEdgeAngle(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetElasticRatioBending(self) -> float: ...
    def SetElasticRatioBending(self, value: Union[str, float]) -> None: ...
    def GetElasticRatioNormal(self) -> float: ...
    def SetElasticRatioNormal(self, value: Union[str, float]) -> None: ...
    def GetElasticRatioTangential(self) -> float: ...
    def SetElasticRatioTangential(self, value: Union[str, float]) -> None: ...
    def GetElasticRatioTorsion(self) -> float: ...
    def SetElasticRatioTorsion(self, value: Union[str, float]) -> None: ...
    def GetElasticity(self) -> str: ...
    def SetElasticity(self, value: str) -> None: ...
    def GetValidElasticityValues(self) -> List[str]: ...
    def GetTargetNumberOfElements(self) -> int: ...
    def SetTargetNumberOfElements(self, value: Union[str, int]) -> None: ...
    def GetElementDampingRatio(self) -> float: ...
    def SetElementDampingRatio(self, value: Union[str, float]) -> None: ...
    def GetFailureRatio(self) -> float: ...
    def SetFailureRatio(self, value: Union[str, float]) -> None: ...
    def GetJointDampingRatio(self) -> float: ...
    def SetJointDampingRatio(self, value: Union[str, float]) -> None: ...
    def GetJointElasticRatio(self) -> float: ...
    def SetJointElasticRatio(self, value: Union[str, float]) -> None: ...
    def GetJointThermalRatio(self) -> float: ...
    def SetJointThermalRatio(self, value: Union[str, float]) -> None: ...
    def GetPlasticRatio(self) -> float: ...
    def SetPlasticRatio(self, value: Union[str, float]) -> None: ...
    def GetPlasticityModel(self) -> str: ...
    def SetPlasticityModel(self, value: str) -> None: ...
    def GetValidPlasticityModelValues(self) -> List[str]: ...
    def GetRemeshToTarget(self) -> bool: ...
    def SetRemeshToTarget(self, value: bool) -> None: ...
    def GetSecondBendingAngleLimit(self, unit: Optional[str] = ...) -> float: ...
    def SetSecondBendingAngleLimit(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTorsionAngleLimit(self, unit: Optional[str] = ...) -> float: ...
    def SetTorsionAngleLimit(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetPorosity(self, unit: Optional[str] = ...) -> float: ...
    def SetPorosity(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetRandomAnglesHalfRange(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetRandomAnglesHalfRange(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetShape(self) -> str: ...
    def SetShape(self, value: str) -> None: ...
    def GetValidShapeValues(self) -> List[str]: ...
    def GetCgmScaleFactor(self) -> float: ...
    def SetCgmScaleFactor(self, value: Union[str, float]) -> None: ...
    def GetSizeType(self) -> str: ...
    def SetSizeType(self, value: str) -> None: ...
    def GetValidSizeTypeValues(self) -> List[str]: ...
    def GetEnableRandomAngle(self) -> bool: ...
    def SetEnableRandomAngle(self, value: bool) -> None: ...
    def EnableRandomOrientation(self) -> None: ...
    def DisableRandomOrientation(self) -> None: ...
    def IsRandomOrientationEnabled(self) -> bool: ...
    def GetMaterial(self): ...
    def SetMaterial(self, value) -> None: ...
    def GetAvailableMaterials(self): ...
    def GetAnisotropic(self) -> bool: ...
    def SetAnisotropic(self, value: bool) -> None: ...
