from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion import RAMotion as RAMotion
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAMotionList(RAList[RAMotion]):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
