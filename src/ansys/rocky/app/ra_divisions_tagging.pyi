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

from ansys.rocky.app.ra_base_tagging import RABaseTagging as RABaseTagging

class RADivisionsTagging(RABaseTagging):
    """
    Rocky PrePost Scripting wrapper to manipulate Divisions Tagging Calculators in a project.

    The class corresponds to an individual "Divisions Tagging" calculation under
    the "Particles Calculation" item on the project\'s data tree. To create the
    :class:`RADivisionsTagging` from a :class:`RACalculations`, use:

    .. code-block:: python

        selection_process = study.GetElement(\'Cube <01>)
        particles_calculations = study.GetCalculations()
        divisions_tagging = particles_calculations.CreateDivisionsTagging(selection_process)
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetDivisionsI(self) -> int:
        """
        Get the value of "Divisions I".

        """

    def SetDivisionsI(self, value: str | int) -> None:
        """
        Set the value of "Divisions I".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetDivisionsJ(self) -> int:
        """
        Get the value of "Divisions J".

        """

    def SetDivisionsJ(self, value: str | int) -> None:
        """
        Set the value of "Divisions J".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetDivisionsK(self) -> int:
        """
        Get the value of "Divisions K".

        """

    def SetDivisionsK(self, value: str | int) -> None:
        """
        Set the value of "Divisions K".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
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

    def GetTagStride(self) -> int:
        """
        Get the value of "Tag Stride".

        """

    def SetTagStride(self, value: str | int) -> None:
        """
        Set the value of "Tag Stride".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetTagValue(self) -> int:
        """
        Get the value of "Tag Value".

        """

    def SetTagValue(self, value: str | int) -> None:
        """
        Set the value of "Tag Value".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """
