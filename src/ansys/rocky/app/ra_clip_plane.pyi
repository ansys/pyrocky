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

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.vizu_clip_plane.vizu_clip_plane_subject import (
    VizuClipPlaneSubject as VizuClipPlaneSubject,
)

from ansys.rocky.app._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin

class RAClipPlane(ApiElementItem, _RAOrientationMixin, _WithMovementMixin):
    """
    Rocky PrePost Scripting wrapper for a single Clip Plane.

    This wrapper class corresponds to an individual entry under the "3D Clip Planes" item on the project\'s
    data tree. Clip Planes can be retrieved from the :class:`RAClipPlaneCollection` via:

    .. code-block:: python

        clip_plane = clip_plane_collection.GetClipPlane(\'Clip Plane <1>\')
    """

    @classmethod
    def GetWrappedClass(cls) -> type[VizuClipPlaneSubject]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetOrigin(self, unit: str | None = None) -> Tuple3F:
        """
        Returns the X, Y and Z plane origin
        """

    def SetOrigin(self, x: float, y: float, z: float, unit: str | None = None) -> None:
        """
        Set the X, Y and Z parameters of the plane origin
        """

    def SetRelativeRotationVector(self, x: float, y: float, z: float) -> None:
        """
        Set the X, Y and Z parameters of the plane normal
        """

    def GetRelativeRotationVector(self) -> Tuple3F:
        """
        Returns the X, Y and Z parameters of the plane normal
        """

    def GetName(self) -> str:
        """
        Get the value of "Name".

        """

    def SetName(self, value: str) -> None:
        """
        Set the value of "Name".

        :param value:
            The value to set.
        """

    def GetPlaneOrigin(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Plane Origin".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetPlaneOrigin(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Plane Origin".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetShowTool(self) -> bool:
        """
        Get the value of "Show Tool".

        """

    def SetShowTool(self, value: bool) -> None:
        """
        Set the value of "Show Tool".

        :param value:
            The value to set.
        """

    def EnableTool(self) -> None:
        """
        Set the value of "Tool" to True.
        """

    def DisableTool(self) -> None:
        """
        Set the value of "Tool" to False.
        """

    def IsToolEnabled(self) -> bool:
        """
        Check if the "Tool" is enabled.

        """
