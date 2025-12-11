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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_tagging import (
    RABaseTagging as RABaseTagging,
)

class RATagging(RABaseTagging):
    """
    Rocky PrePost Scripting wrapper to manipulate Tagging Calculators in a project.

    The class corresponds to an individual "Tagging" calculation under the
    "Particles Calculation" item on the project\'s data tree. To create the
    :class:`RATagging` from a :class:`RACalculations`, use:

    .. code-block:: python

        selection_process = study.GetElement(\'Particles\')
        particles_calculations = study.GetCalculations()
        tagging = particles_calculations.CreateTagging(selection_process)
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
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
