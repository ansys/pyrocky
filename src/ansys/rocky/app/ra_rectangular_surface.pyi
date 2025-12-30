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

from collections.abc import Sequence

from ansys.rocky.app._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin
from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry

class RARectangularSurface(RABaseGeometry, _RAOrientationMixin, _WithMovementMixin):
    """
    Rocky API "Rectangular Surface" model.
    """

    @classmethod
    def GetWrappedClass(self) -> type[object]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def HasMotionFrame(self) -> bool:
        """
        Whether the geometry is linked to a motion frame.

        :return:
            True if geometry is linked to a motion frame False otherwise
        """

    def GetCenter(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Center".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetCenter(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Center".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetLength(self, unit: str | None = None) -> float:
        """
        Get the value of "Length".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetLength(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Length".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
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

    def GetWidth(self, unit: str | None = None) -> float:
        """
        Get the value of "Width".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetWidth(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Width".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """
