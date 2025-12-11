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

from ben10.element_function.semantic_association import SemanticAssociation
from sci20.plugins.process.coloring_process import MeshAssemblyColoringProcessSubject

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

ColorType = tuple[float, float, float]

class RAMeshColoring(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper to manipulate Mesh Colorings.

    This wrapper can be accessed via the project's classes :class:`GetMeshColoring` that allow
    coloring:

    .. code-block:: python

        window = app.Create3DWindow('Win 01')
        particles = study.GetParticles()
        particles_coloring = particles.GetMeshColoring('Win 01')
        particles_coloring.SetNodeVisible(True)

    Valid coloring modes, i.e. Node, Edges, Faces or Vectors can be accessed via
    :class:`GetValidColoringModes`. The property being shown can be additionally modified:

    .. code-block:: python

        particles_coloring.SetNodeGridFunction(None)  # for solid colors
        particles_coloring.SetNodeColor((1.0, 1.0, 1.0))
        particles_coloring.SetNodeGridFunction('Absolute Rotational Velocity')  # for properties
    """

    @classmethod
    def GetWrappedClass(cls) -> type["MeshAssemblyColoringProcessSubject"]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def SetVisible(self, value: bool) -> None:
        """
        Set the value of "Visible".

        :param value:
            The value to set.
        """

    def GetVisible(self) -> bool:
        """
        Get the value of "Visible".

        """

    def SetLevelOfDetail(self, value: str) -> None:
        """
        Set the value of "Level of Detail".

        :param value:
            The value to set. Must be one of [\'Rich\', \'Automatic\', \'Simple\'].
        :raises RockyApiError:
            If `value` is not a valid "Level of Detail" option.
        """

    def GetValidLevelOfDetailValues(self) -> list[str]:
        """
        Get a list of all possible values for "Level of Detail".

        :return:
            The returned list is [\'Rich\', \'Automatic\', \'Simple\'].
        """

    def GetLevelOfDetail(self) -> str:
        """
        Get "Level of Detail" as a string.

        :return:
            The returned value will be one of [\'Rich\', \'Automatic\', \'Simple\'].
        """

    def SetStride(self, value: int) -> None:
        """
        Set the value of "Stride".

        :param value:
            The value to set. This value must be an int type.
        """

    def GetStride(self) -> int:
        """
        Get the value of "Stride".

        """

    def GetAvailableGridFunctions(self) -> set["SemanticAssociation"]:
        """
        Get a list of all possible values for "GridFunctions".

        :return:
            The returned set contains the SemanticAssociation of the available Grid Functions.
        """

    def GetAvailableGridFunctionsNames(self) -> set[str]:
        """
        Get a list of all possible values for "GridFunctions" names.

        :return:
            The returned set contains the names of the available Grid Functions.
        """

    def GetAvailableVectorGridFunctions(self) -> set["SemanticAssociation"]:
        """
        Get a list of all possible values for Vector "GridFunctions".

        :return:
            The returned set contains the SemanticAssociation of the available Vector Grid
            Functions.
        """

    def GetAvailableVectorGridFunctionsNames(self) -> set[str]:
        """
        Get a list of all possible values for Vector "GridFunctions" names.

        :return:
            The returned set contains the names of the available Vector Grid Functions.
        """

    def GetValidColoringModes(self) -> list[str]:
        """
        Get a list with all possible coloring modes names.

        :return:
            The returned values will be a combination of ['Node', 'Edge', 'Face', 'Vector']
        """

    def SetTransparencyEnabled(self, value: bool) -> None:
        """
        Set the value of "Transparency".

        :param value:
            The value to set.
        """

    def GetTransparencyEnabled(self) -> bool:
        """
        Get the value of "Transparency".

        """

    def SetTransparency(self, value: float) -> None:
        """
        Set the value of "Transparency".

        :param value:
           The value to set. This value must be a float type between 0 and 100.

        """

    def GetTransparency(self) -> float:
        """
        Get the value of "Transparency".

        """

    def SetNodeVisible(self, value: bool) -> None:
        """
        Set the value of "Node Visible".

        :param value:
            The value to set.
        """

    def GetNodeVisible(self) -> bool:
        """
        Get the value of "Node Visible".

        """

    def SetNodeColor(self, values: ColorType) -> None:
        """
        Set the values of "Node Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements or `values` is not a tuple.
        """

    def GetNodeColor(self) -> ColorType:
        """
        Get the value of "Node Color".

        """

    def SetNodeGridFunction(self, value: SemanticAssociation | str | None) -> None:
        """
        Set the values of "Node GridFunction".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        :raises RockyApiError:
            If `value` is not a valid type or is not available for the current coloring.
        """

    def GetNodeGridFunction(self) -> SemanticAssociation | None:
        """
        Get the value of "Node GridFunction".

        """

    def SetNodePointSize(self, value: float) -> None:
        """
        Set the value of "Node Point Size".

        :param value:
            The value to set. This value must be a float type.
        """

    def GetNodePointSize(self) -> float:
        """
        Get the value of "Node Point Size".

        """

    def SetEdgeVisible(self, value: bool) -> None:
        """
        Set the value of "Edge Visible".

        :param value:
            The value to set.
        """

    def GetEdgeVisible(self) -> bool:
        """
        Get the value of "Edge Visible".

        """

    def SetEdgeColor(self, values: ColorType) -> None:
        """
        Set the values of "Edge Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements or `values` is not a tuple.
        """

    def GetEdgeColor(self) -> ColorType:
        """
        Get the value of "Edge Color".

        """

    def SetEdgeGridFunction(self, value: SemanticAssociation | str | None) -> None:
        """
        Set the values of "Edge GridFunction".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        :raises RockyApiError:
            If `value` is not a valid type or is not available for the current coloring.
        """

    def GetEdgeGridFunction(self) -> SemanticAssociation | None:
        """
        Get the value of "Edge GridFunction".

        """

    def SetEdgeLineWidth(self, value: float) -> None:
        """
        Set the value of "Edge Line Width".

        :param value:
           The value to set. This value must be a float type.
        """

    def GetEdgeLineWidth(self) -> float:
        """
        Get the value of "Edge Line Width".

        """

    def SetFaceVisible(self, value: bool) -> None:
        """
        Set the value of "Face Visible".

        :param value:
            The value to set.
        """

    def GetFaceVisible(self) -> bool:
        """
        Get the value of "Face Visible".

        """

    def SetFaceColor(self, values: ColorType) -> None:
        """
        Set the values of "Face Color".

        :param values:
            The values to set. The values must be a tuple of floats. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements or `values` is not a tuple.
        """

    def GetFaceColor(self) -> ColorType:
        """
        Get the value of "Face Color".

        """

    def SetFaceGridFunction(self, value: SemanticAssociation | str | None) -> None:
        """
        Set the values of "Face GridFunction".

        :param value:
            The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
            of its name or `None` for solid colors.
        :raises RockyApiError:
            If `value` is not a valid type or is not available for the current coloring.
        """

    def GetFaceGridFunction(self) -> SemanticAssociation | None:
        """
        Get the value of "Face GridFunction".

        """

    def GetValidFaceScopes(self) -> list[str]:
        """
        Get a list of all possible values for "Face Scope".

        :return:
            The returned list with the valid scope options.
        """

    def SetFaceScope(self, value: str) -> None:
        """
        Set the value of "Face Scope".

        :param value:
            The value to set.
        :raises RockyApiError:
            If `value` is not a valid "Face Scope" option.
        """

    def GetFaceScope(self) -> str:
        """
        Get "Face Scope" as a string.

        :return:
            The return will be one of the "GetValidFaceScopes" values.
        """

    def GetValidFaceStructuredPartitionsValues(self) -> list[str]:
        """
        Get a list of all possible values for "Face Structured Partitions".

        :return:
            The returned list is [\'All\', \'Custom...\'].
        """

    def SetFaceStructuredPartitions(self, value: str) -> None:
        """
        Set the value of "Face Structured Partitions".

        :param value:
            The value to set.
        :raises RockyApiError:
            If `value` is not a valid "Face Structured Partitions" option.
        """

    def GetFaceStructuredPartitions(self) -> str:
        """
        Get "Face Structured Partitions" as a string.

        :return:
            The returned value will be one of [\'All\', \'Custom...\'].
        """

    def GetValidFaceCustomStructuredPartitions(self) -> list[str]:
        """
        Get a list of all possible values for "Face Custom Structured Partitions".

         :return:
             The returned list is [\'Top\', \'Bottom\', \'North\', \'South\', \'East\', \'West\'].
        """

    def SetFaceCustomStructuredPartitions(self, values: list[str]) -> None:
        """
        Set the value of "Face Custom Structured Partitions".

        :param values:
            A list containing all the custom partitions.
        :raises RockyApiError:
            If any of `values` is not a valid "Face Custom Structured Partitions" option.
        """

    def GetFaceCustomStructuredPartitions(self) -> list[str]:
        """
         Get the value of "Face Custom Structured Partitions".

        :return:
            The returned value will be a combination of [\'Top\', \'Bottom\', \'North\', \'South\', \'East\',
            \'West\'].
        """

    def SetFaceShowOnNode(self, value: bool) -> None:
        """
        Set the value of "Show On Node".

        :param value:
            The value to set.
        """

    def GetFaceShowOnNode(self) -> bool:
        """
        Get the value of "Show On Node".

        """

    def SetVectorVisible(self, value: bool) -> None:
        """
        Set the value of "Vector Visible".

        :param value:
            The value to set.
        """

    def GetVectorVisible(self) -> bool:
        """
        Get the value of "Vector Visible".

        """

    def SetVectorGridFunction(self, value: SemanticAssociation | str | None) -> None:
        """
        Set the values of "Vector GridFunction".

        :param value:
           The value to set. The value can be heterogeneous, it can be a SemanticAssociation, a str
           of its name or `None` for solid colors.
        :raises RockyApiError:
           If `value` is not a valid type or is not available for the current coloring.
        """

    def GetVectorGridFunction(self) -> SemanticAssociation | None:
        """
        Get the value of "Vector GridFunction".

        """

    def SetVectorScale(self, value: float) -> None:
        """
        Set the value of "Vector Scale".

        :param value:
           The value to set. This value must be a float type.
        """

    def GetVectorScale(self) -> float:
        """
        Get the value of "Vector Scale".

        """

    def SetNormalizedVectorsEnabled(self, value: bool) -> None:
        """
        Set the value of "Normalized Vectors".

        :param value:
            The value to set.
        """

    def GetNormalizedVectorsEnabled(self) -> bool:
        """
        Get the value of "Normalized Vector".

        """
