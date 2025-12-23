# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from _typeshed import Incomplete
from ben10 import interface
from ben10.foundation.decorators import Abstract
from coilib50.subject import Subject as Subject
from plugins10.core.pluginmanager import PluginManager as PluginManager

from ansys.rocky.app.api_application import ApiApplication as ApiApplication
from ansys.rocky.app.api_application import EPApiScripting as EPApiScripting
from ansys.rocky.app.api_expose import ApiExpose as ApiExpose

class ApiError(RuntimeError):
    """
    Exception class representing an error generated in the API layer.

    ApiErrors should be raised for circumstances that are known to be user errors and not
    software bugs - things like trying to make a setup change without deleting results beforehand,
    trying to remove by name items that don't exist, etc.
    """

class IWrappedItem(interface.Interface):
    """
    Interface for wrapped items.
    """

    @classmethod
    def GetWrappedClass(cls) -> None:
        """
        :rtype: class
        :returns:
            The class that is wrapped by the object.
        """

    @classmethod
    def GetClassName(cls) -> None:
        """
        :rtype: unicode
        :returns:
            The classname that is wrapped by the object.
        """

    @classmethod
    def GetChildrenClassesToIgnore(cls) -> None:
        """
        :rtype: list of classes
        :returns:
            The children of wrapped class that should be ignored.
        """

class ApiElementItem:
    """
    Base wrapper class for all subjects.

    :ivar unicode id:
        The id of the subject

    :ivar unicode _model_id:
        The id of the input reader associated with the subject
    """

    def __init__(self, id: str, model_id: str | None = None) -> None:
        """
        .. see:: class docs
        """

    @classmethod
    @Abstract
    def GetWrappedClass(cls) -> type: ...
    @classmethod
    @Abstract
    def GetClassName(cls) -> str: ...
    @classmethod
    def GetChildrenClassesToIgnore(cls) -> list[type]:
        """
        If there are some children classes to ignore the children should override and return them
        in this method.
        """

    def GetDataId(self) -> str:
        """
        :returns:
            The element pool id
        """
    id: Incomplete
    def IsValid(self) -> bool:
        """
        :returns:
            True if the given API object is associated to a valid/existing subject
        """

    def GetSubject(self) -> Subject:
        """
        :returns:
            The element associated with the element id
        """
    subject: Incomplete
    @ApiExpose
    def GetName(self) -> str:
        """
        Get the element's name.

        :returns:
            The name of the element in the application
        """

    @ApiExpose
    def SetName(self, name: str) -> None:
        """
        Set the process name

        :param name:
            The name of the process
        """
    name: Incomplete
    def SetSelected(self) -> None:
        """
        Sets this item as the current item (selected).
        """

    def Select(self, element_names: list[str]) -> None:
        """
        Select all the elements in the application that are child of this element with the given names

        :param list(unicode) element_names:
            The list of element names
        """
