from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import ApiElementItem
from rocky30.plugins.addins.model.property_list import AddinPropertiesList as AddinPropertiesList
from rocky30.plugins.addins.model.property_set import PropertySet as PropertySet
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import ElementWithAddins as ElementWithAddins
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAModulePropertyListItem(ApiElementItem, ElementWithAddins):
    @classmethod
    def GetWrappedClass(self) -> type[PropertySet]: ...
    @classmethod
    def GetClassName(self) -> str: ...

class RAModulePropertyList(RAList[RAModulePropertyListItem]):
    @classmethod
    def GetWrappedClass(self) -> type[AddinPropertiesList]: ...
    @classmethod
    def GetClassName(self) -> str: ...
