# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

from collections.abc import Sequence
from typing import Any

import attr
from rocky30.plugins.addins.model.addin_manager import AddinManager as AddinManager
from rocky30.plugins.addins.model.property_set import PropertyEntry as PropertyEntry
from rocky30.plugins.addins.model.property_set import PropertySet as PropertySet

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_addin_list import RAModulePropertyList as RAModulePropertyList
from ansys.rocky.app.ra_addin_process import RAModuleOutput as RAModuleOutput
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError

@attr.frozen
class AddinPropertyIdentifier:
    name: str
    modules: set[str] = ...
    all_captions: dict[str, str] = ...

@attr.frozen
class AddinCommandIdentifier:
    caption: str
    name: str
    module: str

class ElementWithAddins:
    """
    Rocky PrePost Scripting wrapper for properties in a module or elements with module properties
    like in material interaction and particle input.
    """

    def GetModuleProperties(self) -> Sequence[AddinPropertyIdentifier]:
        """
        Get the names of the module properties.

        :rtype: tuple(AddinPropertyIdentifier)
        """

    def GetModuleProperty(
        self, property_name: str | AddinPropertyIdentifier, unit: str | None = None
    ) -> float | bool | str | RAModulePropertyList:
        """
        Get the value of a module property.

        :param Union[str, AddinPropertyIdentifier] property_name:
            The name of the module property to get.
        :param str unit:
            The unit for `value`, just for scalar properties. If no unit is provided,
            the returned value will be in the unit that was set before (via `SetModuleProperty()`).
        :rtype: float, bool, str or :class:`RAModulePropertyList`
        :return:
            - For basic module properties like numbers and booleans, the returned value is a basic
              Python type (float, bool, or string)
            - For input files, the returned value is the string of the full path to the file
            - For properties that are lists of other properties, the returned value is a
                :class:`RAModulePropertyList`.
        """

    def SetModuleProperty(
        self,
        property_name: str | AddinPropertyIdentifier,
        value: float | bool | str | ApiElementItem | None,
        unit: str | None = None,
    ) -> None:
        """
        Set the value of a module property.

        :param Union[str, AddinPropertyIdentifier] property_name:
            The name of the module property to set.
        :param float, bool, str or ApiElementItem value:
            The value to set.
            If the property_name references to an enum property then value must be an str value.
            If the property_name references to an element reference (point cloud, particles, ...) then
            the value can be either the name of the element (str) or an ApiElementItem representing it.
        :param str unit:
            The unit for `value`, just for scalar properties. If no unit is provided,
            `value` is assumed to be the unit was set before.
        """

    def GetValidOptionsForModuleProperty(
        self, property_name: str
    ) -> Sequence[str | None]:
        """
        Get all valid options only for properties that have a list of possible options.

        :param str property_name:
            The name of the module property.
        :rtype: list[str]
        """

    def ListAddinCommands(self) -> Sequence[AddinCommandIdentifier]:
        """
        Get the names of the active module commands.

        :rtype: tuple(AddinCommandIdentifier)
        """

    def ExecuteCommand(self, command: str | AddinCommandIdentifier) -> None:
        """
        Execute a command related to the module.

        :param str | AddinCommandIdentifier command:
            The name or the AddinCommandIdentifier to be executed. Use `ListAddinCommands` to obtain a sequence of
            active commands.
        """

class RAModule(ApiElementItem, ElementWithAddins):
    """
    Rocky PrePost Scripting wrapper for an individual module in a project, below the "Modules"
    item. Retrieve individual module from the :class:`RAModuleCollection` via:

    .. code-block:: python

        module_collection = study.GetModuleCollection()
        module = module_collection.GetModule(\'Module Name\')
    """

    @classmethod
    def GetWrappedClass(self) -> type: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def EnableModule(self) -> None:
        """
        Enable the module.
        """

    def DisableModule(self) -> None:
        """
        Disable the module.
        """

    def SetModuleEnabled(self, enabled: bool) -> None:
        """
        Enable or disable the module.

        :param bool enabled:
            Whether the module should be enabled (True) or disabled (False).
        """

    def IsModuleEnabled(self) -> bool:
        """
        Check if the module is enabled.

        :rtype: bool
        """

    def GetName(self) -> str:
        """
        Get the element's name.

        :rtype: unicode
        :returns:
            The name of the element in the application
        """

    def SetName(self, name: str) -> None:
        """
        Modules cannot have its name set.

        :param name: str
            The name of the process
        :raises RockyApiError:
            Modules do not support changing its name.
        """

    def GetOutputObject(self) -> RAModuleOutput | None:
        """
        Get the API object that represents this module\'s unique simulation results, if it exists.

        Note that only modules that declare that they generate "unique" results (as opposed to new
        properties/curves on existing items) will have an output object.
        """

    def GetAllModuleProperties(self) -> dict[str, Any]:
        """
        Get a dictionary of all module properties values.

        :rtype: dict(str, Any)
        :returns:
            A dictionary with defined spec properties ('model', 'geometries', 'particle_input', ...) as keys. For the
            entities keys, the value is another dictionary with the entity name or a tuple of names as keys and their
            module properties as values. For scalar properties, the returned value will be a tuple of (value, unit).
        """

class RAModuleCollection(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for the collection of module in a project.

    This wrapper corresponds to the "Modules" item on the project\'s data tree. Retrieve the
    :class:`RAModuleCollection` from a :class:`RAStudy` via:

    .. code-block:: python

        module_collection = study.GetModuleCollection()
    """

    @classmethod
    def GetWrappedClass(self) -> type[AddinManager]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetModuleNames(self) -> list[str]:
        """
        Get the names of the modules in project.
        """

    def GetEnabledModules(self) -> list[str]:
        """
        Get the names of the enabled modules in project.
        """

    def GetModule(self, module_name: str) -> RAModule:
        """
        Get a module given its name.

        :param module_name:
            The name of the module to get.
        """
