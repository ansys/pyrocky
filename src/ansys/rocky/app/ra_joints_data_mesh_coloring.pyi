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

from ansys.rocky.app.ra_mesh_coloring import ColorType as ColorType
from ansys.rocky.app.ra_mesh_coloring import RAMeshColoring as RAMeshColoring

class RAJointsDataMeshColoring:
    def __init__(self, id: str) -> None: ...
    def GetSubject(self) -> Subject: ...
    def SetVisible(self, value: bool) -> None: ...
    def GetVisible(self) -> bool: ...
    def GetValidColoringModes(self) -> list[str]:
        """
        Get a list with all possible coloring modes names.

        :return:
            The returned values will be a combination of ['Joints', 'Joints Connectivity']
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
    def SetJointsVisible(self, value: bool) -> None:
        """
        Set the value of "Joints Visible".

        :param value:
            The value to set.
        """

    def GetJointsVisible(self) -> bool:
        """
        Get the value of "Joints Visible".

        """

    def SetJointsColor(self, values: ColorType) -> None:
        """
        Set the values of "Joints Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        """

    def GetJointsColor(self) -> ColorType:
        """
        Get the value of "Node Color".

        """

    def SetJointsProperty(self, value: type["SemanticAssociation"] | str | None) -> None:
        """
        Set the values of "Joints Property".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        """

    def GetJointsProperty(self) -> type["SemanticAssociation"] | None:
        """
        Get the value of "Joints Property".
        """

    def SetJointsPointSize(self, value: float) -> None:
        """
        Set the value of "Joints Point Size".

        :param value:
            The value to set. This value must be a float type.
        """

    def GetJointsPointSize(self) -> float:
        """
        Get the value of "Joints Point Size".
        """

    def SetJointsConnectivityVisible(self, value: bool) -> None:
        """
        Set the value of "Joints Connectivity Visible".

        :param value:
            The value to set.
        """

    def GetJointsConnectivityVisible(self) -> bool:
        """
        Get the value of "Joints Connectivity Visible".

        """

    def SetJointsConnectivityColor(self, values: ColorType) -> None:
        """
        Set the values of "Joints Connectivity Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        """

    def GetJointsConnectivityColor(self) -> ColorType:
        """
        Get the value of "Joints Connectivity Color".

        """

    def SetJointsConnectivityProperty(
        self, value: type["SemanticAssociation"] | str | None
    ) -> None:
        """
        Set the values of "Joints Connectivity GridFunction".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        """

    def GetJointsConnectivityProperty(self) -> type["SemanticAssociation"] | None:
        """
        Get the value of "Joints Connectivity GridFunction".

        """

    def SetJointsConnectivityLineWidth(self, value: float) -> None:
        """
        Set the value of "Joints Connectivity Line Width".

        :param value:
           The value to set. This value must be a float type.
        """

    def GetJointsConnectivityLineWidth(self) -> float:
        """
        Get the value of "Joints Connectivity Line Width".
        """
