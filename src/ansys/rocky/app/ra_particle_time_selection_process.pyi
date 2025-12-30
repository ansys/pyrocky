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

from ansys.rocky.app.ra_process_element import RAUserProcess as RAUserProcess

class RAParticleTimeSelectionProcess(RAUserProcess):
    """
    Select particles over a time range.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetAbsoluteTimeRange(self, initial_time, final_time, unit: str = "s") -> None:
        """
        Configure this process to use an absolute time range.

        :param float initial_time:
            The initial time for the particle time selection to consider particles.

        :param float final_time:
            The final time for the particle time selection to consider particles.

        :param unicode unit:
            The unit for the range given (by default seconds).
        """

    def SetTimeRange(
        self, range_definition=None, initial=None, final=None, unit: str = "s"
    ) -> None:
        """
        Set the values for this process' time range.

        :param range_definition:
            One of:
            'app_time_filter', 'all', 'last_output', 'absolute', 'single', 'absolute_only_start', 'relative_to_end'.

        :param float initial:
            The initial value for the particle time selection to consider particles. May be ignored
            depending on the range definition.

        :param float final:
            The final time for the particle time selection to consider particles. May be ignored
            depending on the range definition.

        :param unit:
            The unit for the initial/final values passed.
        """

    def GetTimeRange(self):
        """
        Get a dictionary with the current time range configuration.

        :return {'range_definition': unicode, 'initial': int, 'final': int, 'unit': unicode}:
            Returns a dict with the details currently set as the time range.
        """
