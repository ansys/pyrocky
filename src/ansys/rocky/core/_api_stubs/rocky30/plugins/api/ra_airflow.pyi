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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RAAirFlow(RAGridProcessElementItem):
    """
    Rocky PrePost Scripting wrapper for Lattice Boltzmann Air Flow.

    This wrapper can be accessed via the project's :class:`RACFDCoupling`:

    .. code-block:: python

        cfd_coupling = study.GetCFDCoupling()
        cfd_coupling.SetupAirFlow()
        airflow = cfd_coupling.GetAirFlow()

    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def SetPartIdIfValid(self) -> None:
        """
        Set the AirFlow's part_id, but only if AirFlow is enabled in the simulation.
        """

    def GetAirDensity(self, unit: str | None = None) -> float:
        """
        Get the value of "Air Density".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg/m3".
        """

    def SetAirDensity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Air Density".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg/m3".
        """

    def GetAirKinematicViscosity(self, unit: str | None = None) -> float:
        """
        Get the value of "Air Kinematic Viscosity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m2/s".
        """

    def SetAirKinematicViscosity(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Air Kinematic Viscosity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m2/s".
        """

    def GetBoundaryConditionType(self) -> str:
        """
        Get "Boundary Condition Type" as a string.

        :return:
            The returned value will be one of [\'first_derivative\', \'second_derivative\'].
        """

    def SetBoundaryConditionType(self, value: str) -> None:
        """
        Set the value of "Boundary Condition Type".

        :param value:
            The value to set. Must be one of [\'first_derivative\', \'second_derivative\'].
        :raises RockyApiError:
            If `value` is not a valid "Boundary Condition Type" option.
        """

    def GetValidBoundaryConditionTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Boundary Condition Type".

        :return:
            The returned list is [\'first_derivative\', \'second_derivative\'].
        """

    def GetCellSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Cell Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetCellSize(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Cell Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetInteractionScale(self, unit: str | None = None) -> float:
        """
        Get the value of "Interaction Scale".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetInteractionScale(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Interaction Scale".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetMaxX(self, unit: str | None = None) -> float:
        """
        Get the value of "Max X".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMaxX(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Max X".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMaxY(self, unit: str | None = None) -> float:
        """
        Get the value of "Max Y".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMaxY(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Max Y".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMaxZ(self, unit: str | None = None) -> float:
        """
        Get the value of "Max Z".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMaxZ(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Max Z".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMinX(self, unit: str | None = None) -> float:
        """
        Get the value of "Min X".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMinX(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Min X".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMinY(self, unit: str | None = None) -> float:
        """
        Get the value of "Min Y".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMinY(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Min Y".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMinZ(self, unit: str | None = None) -> float:
        """
        Get the value of "Min Z".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMinZ(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Min Z".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetSpeedOfSound(self, unit: str | None = None) -> float:
        """
        Get the value of "Speed of Sound".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetSpeedOfSound(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Speed of Sound".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetStartWhenParticlesEnter(self) -> bool:
        """
        Get the value of "Start When Particles Enter".

        """

    def SetStartWhenParticlesEnter(self, value: bool) -> None:
        """
        Set the value of "Start When Particles Enter".

        :param value:
            The value to set.
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

    def GetUseAirflow(self) -> bool:
        """
        Get the value of "Use Airflow".

        """

    def SetUseAirflow(self, value: bool) -> None:
        """
        Set the value of "Use Airflow".

        :param value:
            The value to set.
        """
