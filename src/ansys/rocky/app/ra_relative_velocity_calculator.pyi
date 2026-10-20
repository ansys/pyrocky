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

from rocky30.plugins.particles_calculations.relative_velocity.relative_velocity_calculator import (
    FrameBasedRelativeVelocityCalculator as FrameBasedRelativeVelocityCalculator,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin

class RARelativeVelocityCalculator(ApiElementItem, _WithMovementMixin):
    """
    Rocky PrePost Scripting wrapper to manipulate Relative Velocity Calculators in a project.

    The class corresponds to an individual "Frame-Based Results" calculation under the
    "Calculation" item on the project\'s data tree. To create the
    :class:`RARelativeVelocityCalculator` from a :class:`RACalculations`, use:

    .. code-block:: python

        selection_process = study.GetElement(\'Particles\')
        calculations = study.GetCalculations()
        relative_velocity_calculator = calculations.CreateFrameBasedResultsCalculator(selection_process)
    """

    @classmethod
    def GetWrappedClass(self) -> type[FrameBasedRelativeVelocityCalculator]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetGridFunctionName(self) -> str:
        """
        Get the grid function name. This name can be used to access the grid function on a process.
        """

    def GetCoordinateSystem(self) -> str:
        """
        Get "Coordinate System" as a string.

        :return:
            The returned value will be one of [\'Cartesian\', \'Cylindrical\', \'Spherical\'].
        """

    def SetCoordinateSystem(self, value: str) -> None:
        """
        Set the value of "Coordinate System".

        :param value:
            The value to set. Must be one of [\'Cartesian\', \'Cylindrical\', \'Spherical\'].
        :raises RockyApiError:
            If `value` is not a valid "Coordinate System" option.
        """

    def GetValidCoordinateSystemValues(self) -> list[str]:
        """
        Get a list of all possible values for "Coordinate System".

        :return:
            The returned list is [\'Cartesian\', \'Cylindrical\', \'Spherical\'].
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

    def GetReferenceAxis(self) -> str:
        """
        Get "Reference Axis" as a string.

        :return:
            The returned value will be one of [\'X\', \'Y\', \'Z\'].
        """

    def SetReferenceAxis(self, value: str) -> None:
        """
        Set the value of "Reference Axis".

        :param value:
            The value to set. Must be one of [\'X\', \'Y\', \'Z\'].
        :raises RockyApiError:
            If `value` is not a valid "Reference Axis" option.
        """

    def GetValidReferenceAxisValues(self) -> list[str]:
        """
        Get a list of all possible values for "Reference Axis".

        :return:
            The returned list is [\'X\', \'Y\', \'Z\'].
        """
