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

class RATwoRollsBeltProfile(ApiElementItem):
    """
    Rocky API for a Two Rolls Belt Profile model.
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetLowerCornerRadius(self, unit: str | None = None) -> float:
        """
        Get the value of "Lower Corner Radius".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetLowerCornerRadius(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Lower Corner Radius".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetTroughingAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Troughing Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetTroughingAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Troughing Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetMaterial(self):
        """
        Get the "Material".

        :rtype: :class:`RASolidMaterial`
        """

    def SetMaterial(self, value) -> None:
        """
        Set the "Material".

        :param unicode, :class:`RASolidMaterial` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableMaterials(self):
        """
        Get all available Materials.

        :rtype: List[:class:`RASolidMaterial`]
            A list of :class:`RASolidMaterial`.
        """
