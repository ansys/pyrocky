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

from rocky30.models.input.sph_inlet import SPHInlet as SPHInlet

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RAFluidInlet(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a single Fluid Inlet input.

    This wrapper class corresponds to an individual entry under the "Inputs" item on the project\'s
    data tree. Particle inputs can be retrieved from the :class:`RAStudy` or the
    :class:`RAInletsOutletsCollection` via:

    .. code-block:: python

        input_1 = study.GetElement(\'Fluid Inlet <1>\')
        input_2 = input_collection.GetParticleInput(\'Fluid Inlet <2>\')

    Instances of :class:`RAFluidInlet` has properties that can be manipulated
    directly, such as the input\'s name and the particle entry point.
    """

    @classmethod
    def GetWrappedClass(self) -> type[SPHInlet]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetBoundaryCondition(self) -> str:
        """
        Get "Boundary Condition" as a string.

        :return:
            The returned value will be one of [\'mass_flow_rate\', \'velocity\'].
        """

    def SetBoundaryCondition(self, value: str) -> None:
        """
        Set the value of "Boundary Condition".

        :param value:
            The value to set. Must be one of [\'mass_flow_rate\', \'velocity\'].
        :raises RockyApiError:
            If `value` is not a valid "Boundary Condition" option.
        """

    def GetValidBoundaryConditionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Boundary Condition".

        :return:
            The returned list is [\'mass_flow_rate\', \'velocity\'].
        """

    def GetMassFlowRate(self, unit: str | None = None) -> float:
        """
        Get the value of "Mass Flow Rate".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "t/h".
        """

    def SetMassFlowRate(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Mass Flow Rate".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "t/h".
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

    def GetInjectionDuration(self, unit: str | None = None) -> float:
        """
        Get the value of "Injection Duration".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetInjectionDuration(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Injection Duration".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetPeriodic(self) -> bool:
        """
        Get the value of "Periodic".

        """

    def SetPeriodic(self, value: bool) -> None:
        """
        Set the value of "Periodic".

        :param value:
            The value to set.
        """

    def EnablePeriodic(self) -> None:
        """
        Set the value of "Periodic" to True.
        """

    def DisablePeriodic(self) -> None:
        """
        Set the value of "Periodic" to False.
        """

    def IsPeriodicEnabled(self) -> bool:
        """
        Check if the "Periodic" is enabled.

        """

    def GetPeriod(self, unit: str | None = None) -> float:
        """
        Get the value of "Period".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetPeriod(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Period".

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

    def GetTemperature(self, unit: str | None = None) -> float:
        """
        Get the value of "Temperature".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "K".
        """

    def SetTemperature(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Temperature".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "K".
        """

    def GetVelocity(self, unit: str | None = None) -> float:
        """
        Get the value of "Velocity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetVelocity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Velocity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetEntryPoint(self):
        """
        Get the "Entry Point".

        :rtype: :class:`RAInletGeometry`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`
        """

    def SetEntryPoint(self, value) -> None:
        """
        Set the "Entry Point".

        :param unicode, :class:`RAInletGeometry`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableEntryPoints(self):
        """
        Get all available Entry Points.

        :rtype: List[:class:`RAInletGeometry`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`]
            A list of :class:`RAInletGeometry`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`.
        """
