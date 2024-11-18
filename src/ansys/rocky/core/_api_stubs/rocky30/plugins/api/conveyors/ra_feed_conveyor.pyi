from ansys.rocky.core._api_stubs.rocky30.plugins.api.conveyors.ra_base_conveyor import RABaseConveyor as RABaseConveyor
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import ElementWithAddins as ElementWithAddins
from typing import List, Optional, Union

class RAFeedConveyor(RABaseConveyor, ElementWithAddins):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetAccelerationPeriod(self, unit: Optional[str] = ...) -> float: ...
    def SetAccelerationPeriod(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBeginningStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetBeginningStopTime(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBeltSpeed(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltSpeed(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDecelerationPeriod(self, unit: Optional[str] = ...) -> float: ...
    def SetDecelerationPeriod(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBeginningStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetBeginningStartTime(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDropBoxHeight(self, unit: Optional[str] = ...) -> float: ...
    def SetDropBoxHeight(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDropBoxLength(self, unit: Optional[str] = ...) -> float: ...
    def SetDropBoxLength(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDropBoxWidth(self, unit: Optional[str] = ...) -> float: ...
    def SetDropBoxWidth(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetFrontPlateOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetFrontPlateOffset(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetWallThickness(self, unit: Optional[str] = ...) -> float: ...
    def SetWallThickness(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBeltThickness(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltThickness(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBeltWidth(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltWidth(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetLoadingLength(self, unit: Optional[str] = ...) -> float: ...
    def SetLoadingLength(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTemperature(self, unit: Optional[str] = ...) -> float: ...
    def SetTemperature(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetThermalBoundaryConditionType(self) -> str: ...
    def SetThermalBoundaryConditionType(self, value: str) -> None: ...
    def GetValidThermalBoundaryConditionTypeValues(self) -> List[str]: ...
    def GetTransitionLength(self, unit: Optional[str] = ...) -> float: ...
    def SetTransitionLength(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetTriangleSize(self, unit: Optional[str] = ...) -> float: ...
    def SetTriangleSize(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDiameter(self, unit: Optional[str] = ...) -> float: ...
    def SetDiameter(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetFaceWidth(self, unit: Optional[str] = ...) -> float: ...
    def SetFaceWidth(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetOffsetToIdlers(self, unit: Optional[str] = ...) -> float: ...
    def SetOffsetToIdlers(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetAlignmentAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetAlignmentAngle(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBeltInclineAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetBeltInclineAngle(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetHorizontalOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetHorizontalOffset(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetOutOfPlaneOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetOutOfPlaneOffset(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetReturnBeltAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetReturnBeltAngle(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetVerticalOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetVerticalOffset(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSkirtboardHeight(self, unit: Optional[str] = ...) -> float: ...
    def SetSkirtboardHeight(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetHeightOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetHeightOffset(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSkirtboardLength(self, unit: Optional[str] = ...) -> float: ...
    def SetSkirtboardLength(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetLengthOffset(self, unit: Optional[str] = ...) -> float: ...
    def SetLengthOffset(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetWidth(self, unit: Optional[str] = ...) -> float: ...
    def SetWidth(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSphBoundaryType(self) -> str: ...
    def SetSphBoundaryType(self, value: str) -> None: ...
    def GetValidSphBoundaryTypeValues(self) -> List[str]: ...
    def GetSurfaceTensionContactAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetSurfaceTensionContactAngle(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMaterial(self): ...
    def SetMaterial(self, value) -> None: ...
    def GetAvailableMaterials(self): ...
