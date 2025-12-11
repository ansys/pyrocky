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

from coilib50.element_function.semantic_association import (
    SemanticAssociation as SemanticAssociation,
)
from coilib50.subject import Subject as Subject

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_mesh_coloring import (
    ColorType as ColorType,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_mesh_coloring import (
    RAMeshColoring as RAMeshColoring,
)

class RAContactsDataMeshColoring:
    def __init__(self, id: str) -> None: ...
    def GetSubject(self) -> Subject: ...
    def SetVisible(self, value: bool) -> None: ...
    def GetVisible(self) -> bool: ...
    def GetValidColoringModes(self) -> list[str]:
        """
        Get a list with all possible coloring modes names.

        :return:
            The returned values will be a combination of ['Contacts', 'Contacts Network']
        """

    def GetAvailableGridFunctionsNames(self) -> set[str]:
        """
        Get a list of all possible values for "GridFunctions" names.

        :return:
            The returned set contains the names of the available Grid Functions.
        """

    def GetAvailableGridFunctions(self) -> set[type["SemanticAssociation"]]:
        """
        Get a list of all possible values for "GridFunctions".

        :return:
            The returned set contains the SemanticAssociation of the available Grid Functions.
        """

    def SetStride(self, value: int) -> None: ...
    def GetStride(self) -> int: ...
    def SetContactsVisible(self, value: bool) -> None:
        """
        Set the value of "Contacts Visible".

        :param value:
            The value to set.
        """

    def GetContactsVisible(self) -> bool:
        """
        Get the value of "Contacts Visible".

        """

    def SetContactsColor(self, values: ColorType) -> None:
        """
        Set the values of "Contacts Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        """

    def GetContactsColor(self) -> ColorType:
        """
        Get the value of "Node Color".
        """

    def SetContactsProperty(
        self, value: type["SemanticAssociation"] | str | None
    ) -> None:
        """
        Set the values of "Contacts Property".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        """

    def GetContactsProperty(self) -> type["SemanticAssociation"] | None:
        """
        Get the value of "Contacts Property".
        """

    def SetContactsPointSize(self, value: float) -> None:
        """
        Set the value of "Contacts Point Size".

        :param value:
            The value to set. This value must be a float type.
        """

    def GetContactsPointSize(self) -> float:
        """
        Get the value of "Contacts Point Size".
        """

    def SetContactsNetworkVisible(self, value: bool) -> None:
        """
        Set the value of "Contacts Network Visible".

        :param value:
            The value to set.
        """

    def GetContactsNetworkVisible(self) -> bool:
        """
        Get the value of "Contacts Network Visible".

        """

    def SetContactsNetworkColor(self, values: ColorType) -> None:
        """
        Set the values of "Contacts Network Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        """

    def GetContactsNetworkColor(self) -> ColorType:
        """
        Get the value of "Contacts Network Color".

        """

    def SetContactsNetworkProperty(
        self, value: type["SemanticAssociation"] | str | None
    ) -> None:
        """
        Set the values of "Contacts Network GridFunction".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        """

    def GetContactsNetworkProperty(self) -> type["SemanticAssociation"] | None:
        """
        Get the value of "Contacts Network GridFunction".

        """

    def SetContactsNetworkLineWidth(self, value: float) -> None:
        """
        Set the value of "Contacts Network Line Width".

        :param value:
           The value to set. This value must be a float type.
        """

    def GetContactsNetworkLineWidth(self) -> float:
        """
        Get the value of "Contacts Network Line Width".
        """
