from _typeshed import Incomplete
from ben10 import interface
from coilib50.subject import Subject as Subject
from plugins10.core.pluginmanager import PluginManager as PluginManager
from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_application import ApiApplication as ApiApplication, EPApiScripting as EPApiScripting
from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_expose import ApiExpose as ApiExpose
from typing import List, Optional, Type

class ApiError(RuntimeError): ...

class IWrappedItem(interface.Interface):
    @classmethod
    def GetWrappedClass(cls) -> None: ...
    @classmethod
    def GetClassName(cls) -> None: ...
    @classmethod
    def GetChildrenClassesToIgnore(cls) -> None: ...

class ApiElementItem:
    def __init__(self, id: str, model_id: Optional[str] = ...) -> None: ...
    @classmethod
    def GetWrappedClass(cls) -> Type: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    @classmethod
    def GetChildrenClassesToIgnore(cls) -> List[Type]: ...
    def GetDataId(self) -> str: ...
    id: Incomplete
    def IsValid(self) -> bool: ...
    def GetSubject(self) -> Subject: ...
    subject: Incomplete
    def GetName(self) -> str: ...
    def SetName(self, name: str) -> None: ...
    name: Incomplete
    def SetSelected(self) -> None: ...
    def Select(self, element_names: List[str]) -> None: ...
