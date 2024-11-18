from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import RAGridProcessElementItem as RAGridProcessElementItem
from typing import List, Optional, Union

class RAAirFlow(RAGridProcessElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def SetPartIdIfValid(self) -> None: ...
    def GetAirDensity(self, unit: Optional[str] = ...) -> float: ...
    def SetAirDensity(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetAirKinematicViscosity(self, unit: Optional[str] = ...) -> float: ...
    def SetAirKinematicViscosity(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetBoundaryConditionType(self) -> str: ...
    def SetBoundaryConditionType(self, value: str) -> None: ...
    def GetValidBoundaryConditionTypeValues(self) -> List[str]: ...
    def GetCellSize(self, unit: Optional[str] = ...) -> float: ...
    def SetCellSize(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetInteractionScale(self, unit: Optional[str] = ...) -> float: ...
    def SetInteractionScale(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMaxX(self, unit: Optional[str] = ...) -> float: ...
    def SetMaxX(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMaxY(self, unit: Optional[str] = ...) -> float: ...
    def SetMaxY(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMaxZ(self, unit: Optional[str] = ...) -> float: ...
    def SetMaxZ(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMinX(self, unit: Optional[str] = ...) -> float: ...
    def SetMinX(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMinY(self, unit: Optional[str] = ...) -> float: ...
    def SetMinY(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMinZ(self, unit: Optional[str] = ...) -> float: ...
    def SetMinZ(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetSpeedOfSound(self, unit: Optional[str] = ...) -> float: ...
    def SetSpeedOfSound(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetStartWhenParticlesEnter(self) -> bool: ...
    def SetStartWhenParticlesEnter(self, value: bool) -> None: ...
    def GetStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStartTime(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetUseAirflow(self) -> bool: ...
    def SetUseAirflow(self, value: bool) -> None: ...
