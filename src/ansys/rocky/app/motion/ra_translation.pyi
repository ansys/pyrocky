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

class RATranslation(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing a Translation motion.

    Retrieve this specific wrapper after setting the correct motion type on a :class:`RAMotion`. For
    example:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType('Translation')
        translation = motion_1.GetTypeObject()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetAcceleration(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Acceleration".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m/s2".
        """

    def SetAcceleration(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Acceleration".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m/s2".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetInput(self) -> str:
        """
        Get "Input" as a string.

        :return:
            The returned value will be one of [\'fixed_velocity\', \'initial_and_final_velocity\', \'initial_velocity_and_acceleration\'].
        """

    def SetInput(self, value: str) -> None:
        """
        Set the value of "Input".

        :param value:
            The value to set. Must be one of [\'fixed_velocity\', \'initial_and_final_velocity\', \'initial_velocity_and_acceleration\'].
        :raises RockyApiError:
            If `value` is not a valid "Input" option.
        """

    def GetValidInputValues(self) -> list[str]:
        """
        Get a list of all possible values for "Input".

        :return:
            The returned list is [\'fixed_velocity\', \'initial_and_final_velocity\', \'initial_velocity_and_acceleration\'].
        """

    def GetFinalVelocity(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Final Velocity".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m/s".
        """

    def SetFinalVelocity(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Final Velocity".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m/s".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetVelocity(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Velocity".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m/s".
        """

    def SetVelocity(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Velocity".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m/s".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """
