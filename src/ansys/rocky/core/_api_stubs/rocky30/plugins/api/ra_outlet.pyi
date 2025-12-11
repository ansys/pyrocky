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

from rocky30.models.input.outlet import Outlet as Outlet

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RAOutlet(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a single Outlet.

    This wrapper class corresponds to an individual entry under the "Inlets and Outlets" item on
    the project\'s data tree. It can be retrieved from the :class:`RAStudy` via:

    .. code-block:: python

        input_1 = study.GetElement(\'Outlet <1>\')
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetEnabledForParticles(self) -> bool:
        """
        Get the value of "Enabled For Particles".

        """

    def SetEnabledForParticles(self, value: bool) -> None:
        """
        Set the value of "Enabled For Particles".

        :param value:
            The value to set.
        """

    def GetEnabledForSph(self) -> bool:
        """
        Get the value of "Enabled For Sph".

        """

    def SetEnabledForSph(self, value: bool) -> None:
        """
        Set the value of "Enabled For Sph".

        :param value:
            The value to set.
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

    def GetPressure(self, unit: str | None = None) -> float:
        """
        Get the value of "Pressure".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa".
        """

    def SetPressure(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Pressure".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa".
        """

    def GetPrescribedPressureEnabled(self) -> bool:
        """
        Get the value of "Prescribed Pressure Enabled".

        """

    def SetPrescribedPressureEnabled(self, value: bool) -> None:
        """
        Set the value of "Prescribed Pressure Enabled".

        :param value:
            The value to set.
        """

    def EnablePrescribedPressure(self) -> None:
        """
        Set the value of "Prescribed Pressure" to True.
        """

    def DisablePrescribedPressure(self) -> None:
        """
        Set the value of "Prescribed Pressure" to False.
        """

    def IsPrescribedPressureEnabled(self) -> bool:
        """
        Check if the "Prescribed Pressure" is enabled.

        """

    def GetExitPoint(self):
        """
        Get the "Exit Point".

        :rtype: :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`
        """

    def SetExitPoint(self, value) -> None:
        """
        Set the "Exit Point".

        :param unicode, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableExitPoints(self):
        """
        Get all available Exit Points.

        :rtype: List[:class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`]
            A list of :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`.
        """
