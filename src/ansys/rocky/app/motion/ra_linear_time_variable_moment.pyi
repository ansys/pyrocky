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

from ansys.rocky.app.api_element_item import ApiElementItem

class RALinearTimeVariableMoment(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing an Linear Time Variable Moment motion.

    Retrieve this specific wrapper after setting the correct motion type on a :class:`RAMotion`. For
    example:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType('Linear Time Variable Moment')
        additional_force = motion_1.GetTypeObject()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetInitialMomentValue(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Initial Moment Value".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "N.m".
        """

    def SetInitialMomentValue(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Initial Moment Value".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "N.m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetTimeCoefficients(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Time Coefficients".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "N.m/s".
        """

    def SetTimeCoefficients(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Time Coefficients".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "N.m/s".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """
