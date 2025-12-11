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

class RATimeFilter(ApiElementItem):
    """
    Rocky api time filter model.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetFinalTime(self, unit: str | None = None) -> float: ...
    def SetFinalTime(self, value: str | float, unit: str | None = None) -> None: ...
    def GetInitialTime(self, unit: str | None = None) -> float: ...
    def SetInitialTime(self, value: str | float, unit: str | None = None) -> None: ...
    def GetEnabled(self) -> bool:
        """
        Get the value of "Enabled".

        """

    def SetEnabled(self, value: bool) -> None:
        """
        Set the value of "Enabled".

        :param value:
            The value to set.
        """

    def EnableTimeFilter(self) -> None:
        """
        Set the value of "Time Filter" to True.
        """

    def DisableTimeFilter(self) -> None:
        """
        Set the value of "Time Filter" to False.
        """

    def IsTimeFilterEnabled(self) -> bool:
        """
        Check if the "Time Filter" is enabled.

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
