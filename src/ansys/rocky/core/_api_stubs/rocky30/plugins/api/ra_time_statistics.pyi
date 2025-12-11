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
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_subject_element import (
    BaseSubjectApiElement as BaseSubjectApiElement,
)

class RATimeStatisticsCalculator(BaseSubjectApiElement):
    """
    PrePost Scripting wrapper for TimeStatisticsCalculators.

    Supports getting/setting the start and stop times, and retrieving the name of the grid function
    generated (for use with the rest of the API).
    """

    def GetStartTime(self):
        """
        Get the start time of this time statistics grid function.

        :rtype: Scalar
        """

    def SetStartTime(self, time_value) -> None:
        """
        Set the start time of this time statistics grid function.

        :type time_value: float or tuple(float, unicode) or Scalar
        """

    def GetStopTime(self):
        """
        Get the stop time of this time statistics grid function.

        :rtype: Scalar
        """

    def SetStopTime(self, time_value) -> None:
        """
        Get the stop time of this time statistics grid function.

        :type time_value: float or tuple(float, unicode) or Scalar
        """

    def GetGridFunctionName(self):
        """
        Get the name of this time statistics grid function, usable on the rest of the API.

        :rtype: unicode
        """

class RATimeStatistics(ApiElementItem):
    """
    PrePost Scripting wrapper for TimeStatisticsContainer.

    Prefer using RATimeStatistics.CreateFor() to create objects of this class, as not all source
    processes accept time statistics grid functions.
    """

    def __init__(self, id, ra_process, model_id=None) -> None:
        """
        :param RAGridProcessElementItem ra_process:
            The input process on which the time statistics grid functions will be created.
        """

    def AddGridFunction(
        self, start_time, stop_time, operation, grid_function_name, location=None
    ):
        """
        Add a new time statistics grid function.

        * For both time parameters (`start_time` and `stop_time`), three kinds of values can be passed:
            - A float or int, which will be assumed to be a value in seconds;
            - A tuple with a float or int and an unicode. The first element is the value, and the second
            is the value\'s unit.
            - A time Scalar.
        * `operation` must be the unicode string representing one of the operations that the time
        statistics grid functions support. Currently these are limited to "average", "min", "max" and
        "sum".
        * `grid_function_name` must be the unicode string of the name of the input grid function over
        which the `operation` will be performed.
        * `location` is optional and must be one of \'cell\' or \'node\'. If no location is passed, the
        time statistics grid function will be created on the cell.

        :rtype: RATimeStatistics
        :return:
            An object representing the newly-created time statistics grid function. This object can
            be used to change the start and stop times, and to retrieve the grid function name.
        """

    def RemoveGridFunction(self, name_or_calculator) -> None:
        """
        Remove a previously-generated grid function.

        The passed value can be either the name of the grid function to be removed, or a
        RATimeStatisticsCalculator object previously returned by AddGridFunction().

        :param unicode or RATimeStatisticsCalculator name_or_calculator:
        """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    @classmethod
    def CreateFor(self, ra_process): ...
