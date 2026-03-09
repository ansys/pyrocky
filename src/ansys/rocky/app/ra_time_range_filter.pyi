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

from ansys.rocky.app.api_element_item import ApiElementItem

class RATimeRangeFilter(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper to manipulate Time Range Filter.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetDomainRange(self) -> str:
        """
        Get the value of "Domain Range".
        """

    def SetDomainRange(self, value: str):
        """
        Set the value of "Domain Range".

        :param value:
            The value to set.
        """

    def GetValidDomainRangeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Domain Range".

        :return:
              The returned list is [\'Application Time Filter\', \'All\', \'Last Output\', \'Time Range\',
              \'Specific Time\', \'After Time\', \'Time Range Relative to Simulation End\'].
        """

    def GetFinal(self, unit: str | None = None) -> float:
        """
        Get the value of "Final".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetFinal(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Final".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetInitial(self, unit: str | None = None) -> float:
        """
        Get the value of "Initial".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetInitial(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Initial".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """
