from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import ApiElementItem

class RAMacroHooks(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type: ...
    @classmethod
    def GetClassName(self) -> str: ...
