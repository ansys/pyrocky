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
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import (
    RAProject as RAProject,
)

class RAPendulum(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing a Pendulum motion.

    Retrieve this specific wrapper after setting the correct motion type on a :class:`RAMotion`. For
    example:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType('Pendulum')
        pendulum = motion_1.GetTypeObject()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetAmplitudeVariation(self, unit: str | None = None) -> float:
        """
        Get the value of "Amplitude Variation".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "rad/s".
        """

    def SetAmplitudeVariation(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Amplitude Variation".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "rad/s".
        """

    def GetInitialAmplitude(self, unit: str | None = None) -> float:
        """
        Get the value of "Initial Amplitude".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "rad".
        """

    def SetInitialAmplitude(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Initial Amplitude".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "rad".
        """

    def GetInitialPhase(self, unit: str | None = None) -> float:
        """
        Get the value of "Initial Phase".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "rad".
        """

    def SetInitialPhase(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Initial Phase".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "rad".
        """

    def GetDirection(self) -> list[float]:
        """
        Get the value of "Direction".

        """

    def SetDirection(self, values: list[str | float]) -> None:
        """
        Set the values of "Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetFrequencyVariation(self, unit: str | None = None) -> float:
        """
        Get the value of "Frequency Variation".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Hz/s".
        """

    def SetFrequencyVariation(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Frequency Variation".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Hz/s".
        """

    def GetInitialFrequency(self, unit: str | None = None) -> float:
        """
        Get the value of "Initial Frequency".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Hz".
        """

    def SetInitialFrequency(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Initial Frequency".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Hz".
        """
