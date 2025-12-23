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

from ansys.rocky.app.conveyors.ra_base_conveyor import RABaseConveyor as RABaseConveyor
from ansys.rocky.app.ra_addins import ElementWithAddins as ElementWithAddins

class RAFeedConveyor(RABaseConveyor, ElementWithAddins):
    """
    Rocky api Feed Conveyor model.
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetAccelerationPeriod(self, unit: str | None = None) -> float:
        """
        Get the value of "Acceleration Period".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetAccelerationPeriod(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Acceleration Period".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetBeginningStopTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Beginning Stop Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetBeginningStopTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Beginning Stop Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetBeltSpeed(self, unit: str | None = None) -> float:
        """
        Get the value of "Belt Speed".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetBeltSpeed(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Belt Speed".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetDecelerationPeriod(self, unit: str | None = None) -> float:
        """
        Get the value of "Deceleration Period".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetDecelerationPeriod(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Deceleration Period".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetBeginningStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Beginning Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetBeginningStartTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Beginning Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetCapillaryFrictionCoefficient(self) -> float:
        """
        Get the value of "Capillary Friction Coefficient".

        """

    def SetCapillaryFrictionCoefficient(self, value: str | float) -> None:
        """
        Set the value of "Capillary Friction Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDropBoxHeight(self, unit: str | None = None) -> float:
        """
        Get the value of "Drop Box Height".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetDropBoxHeight(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Drop Box Height".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetDropBoxLength(self, unit: str | None = None) -> float:
        """
        Get the value of "Drop Box Length".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetDropBoxLength(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Drop Box Length".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetDropBoxWidth(self, unit: str | None = None) -> float:
        """
        Get the value of "Drop Box Width".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetDropBoxWidth(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Drop Box Width".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetFrontPlateOffset(self, unit: str | None = None) -> float:
        """
        Get the value of "Front Plate Offset".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetFrontPlateOffset(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Front Plate Offset".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetWallThickness(self, unit: str | None = None) -> float:
        """
        Get the value of "Wall Thickness".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetWallThickness(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Wall Thickness".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetBeltThickness(self, unit: str | None = None) -> float:
        """
        Get the value of "Belt Thickness".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetBeltThickness(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Belt Thickness".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetBeltWidth(self, unit: str | None = None) -> float:
        """
        Get the value of "Belt Width".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetBeltWidth(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Belt Width".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetLoadingLength(self, unit: str | None = None) -> float:
        """
        Get the value of "Loading Length".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetLoadingLength(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Loading Length".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
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

    def GetThermalBoundaryConditionType(self) -> str:
        """
        Get "Thermal Boundary Condition Type" as a string.

        :return:
            The returned value will be one of [\'adiabatic\', \'prescribed_temperature\', \'cfd_coupled_temperature\'].
        """

    def SetThermalBoundaryConditionType(self, value: str) -> None:
        """
        Set the value of "Thermal Boundary Condition Type".

        :param value:
            The value to set. Must be one of [\'adiabatic\', \'prescribed_temperature\', \'cfd_coupled_temperature\'].
        :raises RockyApiError:
            If `value` is not a valid "Thermal Boundary Condition Type" option.
        """

    def GetValidThermalBoundaryConditionTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Thermal Boundary Condition Type".

        :return:
            The returned list is [\'adiabatic\', \'prescribed_temperature\', \'cfd_coupled_temperature\'].
        """

    def GetTransitionLength(self, unit: str | None = None) -> float:
        """
        Get the value of "Transition Length".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetTransitionLength(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Transition Length".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetTriangleSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Triangle Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetTriangleSize(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Triangle Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetDiameter(self, unit: str | None = None) -> float:
        """
        Get the value of "Diameter".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetDiameter(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Diameter".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetFaceWidth(self, unit: str | None = None) -> float:
        """
        Get the value of "Face Width".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetFaceWidth(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Face Width".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetOffsetToIdlers(self, unit: str | None = None) -> float:
        """
        Get the value of "Offset To Idlers".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetOffsetToIdlers(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Offset To Idlers".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
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

    def GetAlignmentAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Alignment Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetAlignmentAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Alignment Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetBeltInclineAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Belt Incline Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "rad".
        """

    def SetBeltInclineAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Belt Incline Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "rad".
        """

    def GetHorizontalOffset(self, unit: str | None = None) -> float:
        """
        Get the value of "Horizontal Offset".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetHorizontalOffset(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Horizontal Offset".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetOutOfPlaneOffset(self, unit: str | None = None) -> float:
        """
        Get the value of "Out of Plane Offset".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetOutOfPlaneOffset(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Out of Plane Offset".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetReturnBeltAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Return Belt Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "rad".
        """

    def SetReturnBeltAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Return Belt Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "rad".
        """

    def GetVerticalOffset(self, unit: str | None = None) -> float:
        """
        Get the value of "Vertical Offset".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetVerticalOffset(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Vertical Offset".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetSkirtboardHeight(self, unit: str | None = None) -> float:
        """
        Get the value of "Skirtboard Height".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetSkirtboardHeight(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Skirtboard Height".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetHeightOffset(self, unit: str | None = None) -> float:
        """
        Get the value of "Height Offset".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetHeightOffset(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Height Offset".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetSkirtboardLength(self, unit: str | None = None) -> float:
        """
        Get the value of "Skirtboard Length".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetSkirtboardLength(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Skirtboard Length".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetLengthOffset(self, unit: str | None = None) -> float:
        """
        Get the value of "Length Offset".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetLengthOffset(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Length Offset".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetWidth(self, unit: str | None = None) -> float:
        """
        Get the value of "Width".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetWidth(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Width".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetSphBoundaryType(self) -> str:
        """
        Get "Sph Boundary Type" as a string.

        :return:
            The returned value will be one of [\'free_slip\', \'no_slip_laminar\', \'no_slip_turbulent\'].
        """

    def SetSphBoundaryType(self, value: str) -> None:
        """
        Set the value of "Sph Boundary Type".

        :param value:
            The value to set. Must be one of [\'free_slip\', \'no_slip_laminar\', \'no_slip_turbulent\'].
        :raises RockyApiError:
            If `value` is not a valid "Sph Boundary Type" option.
        """

    def GetValidSphBoundaryTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Sph Boundary Type".

        :return:
            The returned list is [\'free_slip\', \'no_slip_laminar\', \'no_slip_turbulent\'].
        """

    def GetSurfaceTensionContactAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Surface Tension Contact Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetSurfaceTensionContactAngle(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Surface Tension Contact Angle".

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
