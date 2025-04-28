from coilib50.process import IProcess as IProcess
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import RAGridProcessElementItem as RAGridProcessElementItem

class RAModuleOutput(RAGridProcessElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[IProcess]: ...
    @classmethod
    def GetClassName(self) -> str: ...
