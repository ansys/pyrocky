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

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.core.geometry.rocky_document_constants import (
    UNIT_PLANE_ANGLE as UNIT_PLANE_ANGLE,
)

class _RAOrientationMixin:
    """
    Mixin class to be used by API classes whose subjects have an orientation property compliant with
    sci20.core.Orientation class.
    """

    def GetOrientation(self, unit: str = ...) -> Tuple3F:
        """
        Get the orientation angles. For more specific cases, see: "GetOrientationFromAngles",
        "GetOrientationFromAngleAndVector" and "GetOrientationFromBasisVector".
        """

    def SetOrientation(self, rotation: Tuple3F, unit: str = ...) -> None:
        """
        The rotation is the angles in x, y and z of the rotation in the given unit. For more
        specific methods, see: "SetOrientationFromAngles", "SetOrientationFromAngleAndVector" and
        "SetOrientationFromBasisVector".
        """

    def SetOrientationFromAngles(
        self,
        rotation: Tuple3F,
        unit: str = ...,
        local_angles: bool = True,
        order: str = "XYZ",
    ) -> None:
        """
        The rotation is the angles in x, y and z of the rotation. The default unit is `dega`.
        Additionally, local_angles can be used as well an order of the values via kwargs.
        """

    def SetOrientationFromAngleAndVector(
        self, angle: float, vector: Tuple3F, unit: str = ...
    ) -> None:
        """
        The rotation uses the angle and a vector, using `unit` and changes the orientation mode to
        Angle and Vector.
        """

    def SetOrientationFromBasisVector(
        self, vector_x: Tuple3F, vector_y: Tuple3F, vector_z: Tuple3F
    ) -> None:
        """
        Sets the rotation using three basis vector and changes the orientation mode to Basis Vector.
        """

    def GetOrientationFromAngles(self, unit: str = ...) -> Tuple3F:
        """
        Get the current orientation in the form of angles.
        """

    def GetOrientationFromAngleAndVector(self, unit: str = ...) -> tuple[float, Tuple3F]:
        """
        Get the current orientation in the form of an angle and a vector.
        """

    def GetOrientationFromBasisVector(self) -> tuple[Tuple3F, Tuple3F, Tuple3F]:
        """
        Get the current orientation in the form of three basis vectors.
        """
