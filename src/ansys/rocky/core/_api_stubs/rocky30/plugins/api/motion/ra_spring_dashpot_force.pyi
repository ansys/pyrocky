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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RASpringDashpotForce(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing a Spring-Dashpot Force motion.

    Retrieve this specific wrapper after setting the correct motion type on a :class:`RAMotion`. For
    example:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType('Spring-Dashpot Force')
        spring_force = motion_1.GetTypeObject()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetDashpotCoefficient(self, unit: str | None = None) -> float:
        """
        Get the value of "Dashpot Coefficient".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "N.s/m".
        """

    def SetDashpotCoefficient(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Dashpot Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "N.s/m".
        """

    def GetDirection(self) -> str:
        """
        Get "Direction" as a string.

        :return:
            The returned value will be one of [\'none\', \'x\', \'y\', \'xy\', \'z\', \'xz\', \'yz\', \'xyz\'].
        """

    def SetDirection(self, value: str) -> None:
        """
        Set the value of "Direction".

        :param value:
            The value to set. Must be one of [\'none\', \'x\', \'y\', \'xy\', \'z\', \'xz\', \'yz\', \'xyz\'].
        :raises RockyApiError:
            If `value` is not a valid "Direction" option.
        """

    def GetValidDirectionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Direction".

        :return:
            The returned list is [\'none\', \'x\', \'y\', \'xy\', \'z\', \'xz\', \'yz\', \'xyz\'].
        """

    def GetSpringCoefficient(self, unit: str | None = None) -> float:
        """
        Get the value of "Spring Coefficient".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "N/m".
        """

    def SetSpringCoefficient(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Spring Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "N/m".
        """
