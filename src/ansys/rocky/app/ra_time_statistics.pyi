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

from coilib50.units import Scalar
from rocky30.plugins.time_statistics.time_statistics_calculation import (
    TimeStatisticsCalculator as TimeStatisticsCalculator,
)
from rocky30.plugins.time_statistics.time_statistics_container import (
    ITimeStatisticsContainer as ITimeStatisticsContainer,
)
from rocky30.plugins.time_statistics.time_statistics_container import (
    TimeStatisticsContainer as TimeStatisticsContainer,
)
from rocky30.plugins.time_statistics.time_statistics_operations import (
    TimeStatisticsOperations as TimeStatisticsOperations,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

class RATimeStatisticsCalculator(ApiElementItem):
    """
    PrePost Scripting wrapper for TimeStatisticsCalculators.

    Supports getting/setting the start and stop times, and retrieving the name of the grid function
    generated (for use with the rest of the API).
    """

    @classmethod
    def GetWrappedClass(cls) -> type[TimeStatisticsCalculator]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetGridFunctionName(self) -> str:
        """
        Get the name of this time statistics grid function, usable on the rest of the API.
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

class RATimeStatistics(ApiElementItem):
    """
    PrePost Scripting wrapper for TimeStatisticsContainer.
    """

    def AddGridFunction(
        self,
        start_time: float | int | tuple[float | int, str] | Scalar,
        stop_time: float | int | tuple[float | int, str] | Scalar,
        operation: str,
        grid_function_name: str,
        location: str | None = None,
    ) -> RATimeStatisticsCalculator:
        """
        Add a new time statistics grid function.

            * For both time parameters (`start_time` and `stop_time`), three kinds of values can be passed:
                - A float or int, which will be assumed to be a value in seconds;
                - A tuple with a float or int and a string. The first element is the value, and the second
                  is the value\'s unit.
                - A time Scalar.
            * `operation` must be the string representing one of the operations that the time
               statistics grid functions support. Currently, these are limited to "average", "min", "max" and
               "sum".
            * `grid_function_name` must be the string of the name of the input grid function over
               which the `operation` will be performed.
            * `location` is optional and must be one of \'cell\' or \'node\'. If no location is passed, the
               time statistics grid function will be created on the cell.

        :return RATimeStatisticsCalculator:
            An object representing the newly-created time statistics grid function. This object can
            be used to change the start and stop times, and to retrieve the grid function name.
        """

    def RemoveGridFunction(
        self, name_or_calculator: str | RATimeStatisticsCalculator
    ) -> None:
        """
        Remove a previously-generated grid function.

        The passed value can be either the name of the grid function to be removed, or a
        RATimeStatisticsCalculator object previously returned by AddGridFunction().
        """

    @classmethod
    def GetWrappedClass(cls) -> type: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    @classmethod
    def CreateFor(cls, ra_process: ApiElementItem) -> RATimeStatistics | None: ...
