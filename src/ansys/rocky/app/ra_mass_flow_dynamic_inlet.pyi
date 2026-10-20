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

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_mass_flow_dynamic_inlet_properties import (
    RAMassFlowDynamicInletPropertiesList as RAMassFlowDynamicInletPropertiesList,
)
from ansys.rocky.app.ra_particle import RAParticle as RAParticle

class RAMassFlowDynamicInlet(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a single Mass Flow Dynamic Inlet input.

    This wrapper class corresponds to an individual entry under the "Inputs" item on the project\'s
    data tree. Mass Flow Dynamic Inlets can be retrieved from the :class:`RAStudy` or the
    :class:`RAInletsOutletsCollection` via:

    .. code-block:: python

        inlet = study.GetElement(\'Mass Flow Dynamic Inlet <1>\')
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetInputPropertiesList(self) -> RAMassFlowDynamicInletPropertiesList:
        """
        Return a list of input properties
        """

    def AddParticle(
        self, particle: RAParticle | str
    ) -> RAMassFlowDynamicInletPropertiesList:
        """
        Add a new particle to the Mass Flow Dynamic Inlet input properties list.

        :return: A new :class:`RAMassFlowDynamicInletPropertiesList` object.
        """

    def RemoveParticle(self, particle: RAParticle | str) -> None:
        """
        Remove a particle from the Mass Flow Dynamic Inlet input properties list.

        :param particle: The particle to remove, either as an :class:`RAParticle` object or by name.
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

    def GetInjectionVelocity(self, unit: str | None = None) -> float:
        """
        Get the value of "Injection Velocity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetInjectionVelocity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Injection Velocity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetMaximumInjectionTries(self) -> int:
        """
        Get the value of "Maximum Injection Tries".

        """

    def SetMaximumInjectionTries(self, value: str | int) -> None:
        """
        Set the value of "Maximum Injection Tries".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
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

    def GetRandomTravelExponent(self) -> float:
        """
        Get the value of "Random Travel Exponent".

        """

    def SetRandomTravelExponent(self, value: str | float) -> None:
        """
        Set the value of "Random Travel Exponent".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSizeScaling(self) -> float:
        """
        Get the value of "Size Scaling".

        """

    def SetSizeScaling(self, value: str | float) -> None:
        """
        Set the value of "Size Scaling".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
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

    def GetVoidFraction(self) -> float:
        """
        Get the value of "Void Fraction".

        """

    def SetVoidFraction(self, value: str | float) -> None:
        """
        Set the value of "Void Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """
