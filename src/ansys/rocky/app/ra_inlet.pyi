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

from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry
from ansys.rocky.app.rocky_api_utils import (
    ConvertUserPassedValueToScalar as ConvertUserPassedValueToScalar,
)

class RAInletGeometry(RABaseGeometry):
    """
    Rocky API Inlet model.
    """

    @classmethod
    def GetWrappedClass(self): ...
    def SetGeometryType(self, geometry_type: str) -> None:
        """
        Sets Inlet geometry type, rectangular or circular

        :param geometry_type:
            Inlet geometry's type, 'rectangular' or 'circular'.
        """

    def GetGeometryType(self) -> str:
        """
        Get the Inlet geometry type, which is either 'rectangular' or 'circular'.
        """

    def GetRectangularSize(self, unit: str | None = None) -> tuple[float, float]:
        """
        Get the rectangular length and width of the inlet.

        :param unit:
            The optional unit of the returned values. If no unit is passed, the values will be in 'm'.
        :return:
            A (length, width) tuple.
        """

    def SetRectangularSize(
        self, length: float, width: float, unit: str | None = None
    ) -> None:
        """
        Sets inlet rectangular size.

        :param width: Inlet width
        :param length: Inlet length
        :param unit:
            The optional unit. If no unit is passed, 'm' is used.
        """

    @classmethod
    def GetClassName(self) -> str: ...
    def GetCircularMinMaxRadius(self, unit: str | None = None) -> tuple[float, float]:
        """
        Get the minimum and maximum radiuses for circular inlets.

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        :return:
            A tuple with (minimum_radius, maximum_radius)
        """

    def SetCircularMinMaxRadius(
        self, min_radius: float, max_radius: float, unit: str | None = None
    ) -> None:
        """
        Set the minimum and maximum radiuses for circular inlets.

        :param unit:
            The unit for the radiuses. If no unit is provided, the radiuses will be assumed to be
            in "m".
        """

    def GetAlignmentAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Alignment Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetAlignmentAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Alignment Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
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

    def GetInclineAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Incline Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetInclineAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Incline Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
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
