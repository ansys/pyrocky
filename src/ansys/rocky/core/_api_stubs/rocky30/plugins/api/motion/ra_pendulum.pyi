from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import ApiElementItem
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import RAProject as RAProject
from typing import List, Optional, Union

class RAPendulum(ApiElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetAmplitudeVariation(self, unit: Optional[str] = ...) -> float: ...
    def SetAmplitudeVariation(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetInitialAmplitude(self, unit: Optional[str] = ...) -> float: ...
    def SetInitialAmplitude(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetInitialPhase(self, unit: Optional[str] = ...) -> float: ...
    def SetInitialPhase(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetDirection(self) -> List[float]: ...
    def SetDirection(self, values: List[Union[str, float]]) -> None: ...
    def GetFrequencyVariation(self, unit: Optional[str] = ...) -> float: ...
    def SetFrequencyVariation(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetInitialFrequency(self, unit: Optional[str] = ...) -> float: ...
    def SetInitialFrequency(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
