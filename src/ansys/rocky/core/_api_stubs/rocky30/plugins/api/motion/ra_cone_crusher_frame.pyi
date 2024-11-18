from collections.abc import Sequence
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_base_motion import RABaseMotionFrame as RABaseMotionFrame
from typing import List, Optional, Union

class RAConeCrusherFrame(RABaseMotionFrame):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetInitialOrientation(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetInitialOrientation(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetPivotPoint(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetPivotPoint(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetRotationAxis(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetRotationAxis(self, values: Sequence[Union[str, float]], unit: Optional[str] = ...) -> None: ...
    def GetRotationalVelocity(self, unit: Optional[str] = ...) -> float: ...
    def SetRotationalVelocity(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStartTime(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStopTime(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
