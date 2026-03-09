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

from rocky30.plugins.particles_calculations.selection_residence_time_calculation import (
    ParticlesSelectionResidenceTimeCalculator as ParticlesSelectionResidenceTimeCalculator,
)

from ansys.rocky.app.api_element_item import ApiElementItem

class RAResidenceTime(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper to manipulate Residence Time Calculators in a project.

    The class corresponds to an individual "Residence Time" calculation under the
    "Particles Calculation" item on the project\'s data tree. To create the
    :class:`RAResidenceTime` from a :class:`RACalculations`, use:

    .. code-block:: python

        selection_process = study.GetElement(\'Particles\')
        particles_calculations = study.GetCalculations()
        residence_time = particles_calculations.CreateSelectionResidenceTime(selection_process)
    """

    @classmethod
    def GetWrappedClass(self) -> type[ParticlesSelectionResidenceTimeCalculator]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetGridFunctionName(self) -> str:
        """
        Get the grid function name. This name can be used to access the grid
        function on a particle-based process.
        """

    def GetCalculatorName(self) -> str:
        """
        Get the grid function name. This name can be used to access the grid
        function on a particle-based process.
        """

    def GetNameMask(self) -> str:
        """
        Get the value of "Name Mask".

        """

    def SetNameMask(self, value: str) -> None:
        """
        Set the value of "Name Mask".

        :param value:
            The value to set.
        """

    def GetStopTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Stop Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetStopTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Stop Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetStartTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """
