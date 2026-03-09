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

from collections.abc import Iterator

from barril.units import FixedArray as FixedArray
from coilib50.subject import Subject as Subject
from coilib50.time.time_step_interface import ITimeStep as ITimeStep
from rocky30.models.geometry.geometry_collection import (
    GeometryCollection as GeometryCollection,
)

from ansys.rocky.app.ra_api import CheckResults as CheckResults
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry
from ansys.rocky.app.ra_list import RAList as RAList

class RAGeometryCollection(RAList):
    """
    Rocky PrePost Scripting wrapper for the collection of geometries in a project.

    The class represents the "Geometries" item on the project data tree. To get the :class:`RAGeometryCollection`
    from a :class:`RAStudy`, use:

    .. code-block:: python

        geometry_collection = study.GetGeometryCollection()

    This class contains methods to iterate and retrieve the geometries in a given project, manipulating
    the collection as a regular Python list, e.g.:

    .. code-block:: python

        for geometry in geometry_collection:
            print(geometry.GetName())

        feed_conveyor = geometry_collection[1]
        inlet = geometry_collection.GetGeometry(\'Inlet <01>\')

    To create the different kind of geometries (conveyors, inlets and custom geometries), see
    :class:`RAStudy`.
    """

    @classmethod
    def GetWrappedClass(cls) -> type[GeometryCollection]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetGeometryNames(self) -> list[str]:
        """
        Get the names of the geometries in this collection.
        """

    def GetGeometry(self, geometry_name):
        """
        Get a geometry from its name.

        :param unicode geometry_name:
        """

    def IterInletGeometries(self) -> Iterator[RABaseGeometry]:
        """
        Iterate over the inlet geometries.

        """

    def IterSurfaces(self) -> Iterator[RABaseGeometry]:
        """
        Iterate over the surface geometries.
        """

    def IterWalls(self) -> Iterator[RABaseGeometry]:
        """
        Iterate over the walls geometries.
        """

    def IterSystemCouplingWalls(self) -> Iterator[RABaseGeometry]:
        """
        Iterate over the System Coupling walls geometries.
        """

    def GetBoundingBox(
        self,
        time_step: ITimeStep | None,
        force_load: bool = False,
        force_orthogonal: bool = True,
    ) -> tuple[FixedArray, FixedArray]:
        """
        Get the bounding box containing all geometries in this collection, at the given time.

        :param time_step:
            The time step for which the bounding box should be computed.

        :param force_load:
            If True, the bounding box will be computed by loading the geometries from the project.
            If False, the bounding box will only be returned if it was already computed.

        :param force_orthogonal:
            If True, the bounding box will be computed in an orthogonal coordinate system.
            If False, the bounding box will be computed in the original coordinate system of the geometries.

        :return:
            The bounding box of all the geometries in the passed time step, or None if the box
            could not be computed.
        """

    def RemoveGeometry(self, geometry: RABaseGeometry | str | None) -> None:
        """
        Remove the given geometry from the project.
        """
