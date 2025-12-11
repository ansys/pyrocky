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

from rocky30.plugins.addins.model.property_list import (
    AddinPropertiesList as AddinPropertiesList,
)
from rocky30.plugins.addins.model.property_set import PropertySet as PropertySet

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAModulePropertyListItem(ApiElementItem, ElementWithAddins):
    """
    Rocky PrePost Scripting wrapper for an item inside a :class:`RAModulePropertyList`.

    The wrapper corresponds to a single row in a table of module properties inside the editor of
    an individual Module or simulation entity. It is retrieved from its containing list, via:

    .. code-block:: python

        my_module = study.GetElement('My Module')
        module_list = my_module.GetModuleProperty('List of Items')
        module_item = module_list.New()
    """

    @classmethod
    def GetWrappedClass(self) -> type[PropertySet]: ...
    @classmethod
    def GetClassName(self) -> str: ...

class RAModulePropertyList(RAList[RAModulePropertyListItem]):
    """
    Rocky PrePost Scripting wrapper for a Module property that is a list of other Modules properties.

    The wrapper corresponds to a table of module properties inside the editor of an individual
    Module or a simulation entity. Such a list can be obtained via the PrePost Scripting wrapper for the object
    that contains it (that is, a Module or simulation entity), via:

    .. code-block:: python

        my_module = study.GetElement('My Module')
        module_list = my_module.GetModuleProperty('List of Items')

    The RAModulePropertyList supports iteration like regular lists and item manipulation via
    :meth:`New()`, :meth:`Remove()` and :meth:`Clear()`. It contains items of type
    :class:`RAModulePropertyListItem`.
    """

    @classmethod
    def GetWrappedClass(self) -> type[AddinPropertiesList]: ...
    @classmethod
    def GetClassName(self) -> str: ...
