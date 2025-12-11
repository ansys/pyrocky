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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RARotation(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing a Rotation motion.

    Retrieve this specific wrapper after setting the correct motion type on a :class:`RAMotion`. For
    example:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType('Rotation')
        rotation = motion_1.GetTypeObject()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetAngularAcceleration(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Angular Acceleration".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "rad/s2".
        """

    def SetAngularAcceleration(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Angular Acceleration".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "rad/s2".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetInitialAngularVelocity(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Initial Angular Velocity".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "rad/s".
        """

    def SetInitialAngularVelocity(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Initial Angular Velocity".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "rad/s".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """
