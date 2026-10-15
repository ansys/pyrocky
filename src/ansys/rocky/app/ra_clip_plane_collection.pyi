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

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.vizu_clip_plane.vizu_clip_plane_collection import (
    VizuClipPlaneCollection as VizuClipPlaneCollection,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_clip_plane import RAClipPlane as RAClipPlane

class RAClipPlaneCollection(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for the collection of Clip Planes in a project.

    This wrapper corresponds to the "3D Clip Planes" item in the project\'s data tree. To retrieve the
    :class:`RAClipPlaneCollection` from a :class:`RAProject`, use:

    .. code-block:: python

        clip_planes_collection = project.Get3DClipPlanesCollection()

    """

    @classmethod
    def GetWrappedClass(self) -> type[VizuClipPlaneCollection]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetClipPlaneNames(self) -> list[str]:
        """
        Get a list with the name of the clip planes.
        """

    def GetClipPlaneByName(self, name: str) -> RAClipPlane:
        """
        Get the clip plane with the given name.
        """

    def CreateClipPlane(
        self,
        name: str | None = None,
        origin: Tuple3F | None = None,
        normal: Tuple3F | None = None,
    ) -> RAClipPlane:
        """
        Create a new clip plane with the (optionally) given name, origin and normal.
        Returns the newly created clip plane.
        """

    def RemoveClipPlane(self, clip_plane: RAClipPlane | str) -> None:
        """
        Removes the given clip plane from the project.

        :param clip_plane:
            a RAClipPlane or its name
        """
