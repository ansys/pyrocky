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

from rocky30.process.geometry.system_coupling_wall import (
    SystemCouplingWall as SystemCouplingWall,
)

from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin
from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry

class RASystemCouplingWall(RABaseGeometry, _WithMovementMixin):
    """
    Rocky API "System Coupling Wall" model.
    """

    @classmethod
    def GetWrappedClass(self) -> type[object]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def HasMotionFrame(self) -> bool:
        """
        Whether the geometry is linked to a motion frame.

        :return:
            True if geometry is linked to a motion frame False otherwise
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

    def GetStructuralCouplingTypeEnabled(self) -> bool:
        """
        Get the value of "Structural Coupling Type Enabled".

        """

    def SetStructuralCouplingTypeEnabled(self, value: bool) -> None:
        """
        Set the value of "Structural Coupling Type Enabled".

        :param value:
            The value to set.
        """

    def EnableStructuralCouplingType(self) -> None:
        """
        Set the value of "Structural Coupling Type" to True.
        """

    def DisableStructuralCouplingType(self) -> None:
        """
        Set the value of "Structural Coupling Type" to False.
        """

    def IsStructuralCouplingTypeEnabled(self) -> bool:
        """
        Check if the "Structural Coupling Type" is enabled.

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

    def GetThermalCouplingTypeEnabled(self) -> bool:
        """
        Get the value of "Thermal Coupling Type Enabled".

        """

    def SetThermalCouplingTypeEnabled(self, value: bool) -> None:
        """
        Set the value of "Thermal Coupling Type Enabled".

        :param value:
            The value to set.
        """

    def EnableThermalCouplingType(self) -> None:
        """
        Set the value of "Thermal Coupling Type" to True.
        """

    def DisableThermalCouplingType(self) -> None:
        """
        Set the value of "Thermal Coupling Type" to False.
        """

    def IsThermalCouplingTypeEnabled(self) -> bool:
        """
        Check if the "Thermal Coupling Type" is enabled.

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
