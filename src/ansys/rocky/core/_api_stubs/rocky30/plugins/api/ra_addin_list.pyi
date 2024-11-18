from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import ApiElementItem
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import ElementWithAddins as ElementWithAddins
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAModulePropertyListItem(ApiElementItem, ElementWithAddins):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...

class RAModulePropertyList(RAList[RAModulePropertyListItem]): ...
