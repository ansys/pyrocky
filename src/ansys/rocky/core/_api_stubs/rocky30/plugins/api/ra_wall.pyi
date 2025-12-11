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

from collections.abc import Sequence

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.core.geometry.rocky_document_constants import (
    UNIT_PLANE_ANGLE as UNIT_PLANE_ANGLE,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion._with_movement_mixin import (
    _WithMovementMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import (
    RABaseGeometry as RABaseGeometry,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import (
    RAProject as RAProject,
)

class RAWall(RABaseGeometry, ElementWithAddins, _WithMovementMixin):
    """
    Rocky API Geometry model.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def LoadFile(
        self, file_path: str, import_scale: float = 1.0, convert_yz: bool = False
    ) -> None:
        """
        Replace the geometry representation for a new one contained on a file.

        :param file_path:
            The file path of the STL, DXF or XGL file to import.

        :param import_scale:
            The import scale to be applied to the imported geometry.

        :param convert_yz:
            Whether the y and z axes of the imported geometry should be converted.
        """

    def HasMotionFrame(self) -> bool:
        """
        Whether the boundary is linked to a motion frame.

        :return:
            True if boundary is linked to a motion frame False otherwise
        """

    def GetOrientation(self, unit: str = ...) -> Tuple3F:
        """
        Get the orientation angles. For more specific cases, see: "GetOrientationFromAngles",
        "GetOrientationFromAngleAndVector" and "GetOrientationFromBasisVector".
        """

    def SetOrientation(self, rotation: Tuple3F, unit: str = ...) -> None:
        """
        The rotation is the angles in x, y and z of the rotation in the given unit. For more
        specific methods, see: "SetOrientationFromAngles", "SetOrientationFromAngleAndVector" and
        "SetOrientationFromBasisVector".
        """

    def SetOrientationFromAngles(
        self,
        rotation: Tuple3F,
        unit: str = ...,
        local_angles: bool = True,
        order: str = "XYZ",
    ) -> None:
        """
        The rotation is the angles in x, y and z of the rotation. The default unit is `dega`.
        Additionally, local_angles can be used as well an order of the values via kwargs.
        """

    def SetOrientationFromAngleAndVector(
        self, angle: float, vector: Tuple3F, unit: str = ...
    ) -> None:
        """
        The rotation uses the angle and a vector, using `unit` and changes the orientation mode to
        Angle and Vector.
        """

    def SetOrientationFromBasisVector(
        self, vector_x: Tuple3F, vector_y: Tuple3F, vector_z: Tuple3F
    ) -> None:
        """
        Sets the rotation using three basis vector and changes the orientation mode to Basis Vector.
        """

    def GetOrientationFromAngles(self, unit: str = ...) -> Tuple3F:
        """
        Get the current orientation in the form of angles.
        """

    def GetOrientationFromAngleAndVector(self, unit: str = ...) -> tuple[float, Tuple3F]:
        """
        Get the current orientation in the form of an angle and a vector.
        """

    def GetOrientationFromBasisVector(self) -> tuple[Tuple3F, Tuple3F, Tuple3F]:
        """
        Get the current orientation in the form of three basis vectors.
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

    def GetDisableTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Disable Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetDisableTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Disable Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetEnableTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Enable Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetEnableTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Enable Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetPivotPoint(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Pivot Point".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetPivotPoint(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Pivot Point".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
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

    def GetTranslation(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Translation".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetTranslation(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Translation".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
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

    def GetBoundaryMass(self, unit: str | None = None) -> float:
        """
        Get the value of "Boundary Mass".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg".
        """

    def SetBoundaryMass(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Boundary Mass".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg".
        """

    def GetGravityCenter(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Gravity Center".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetGravityCenter(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Gravity Center".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetMomentXDirection(self) -> list[float]:
        """
        Get the value of "Moment X Direction".

        """

    def SetMomentXDirection(self, values: list[str | float]) -> None:
        """
        Set the values of "Moment X Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetMomentYDirection(self) -> list[float]:
        """
        Get the value of "Moment Y Direction".

        """

    def SetMomentYDirection(self, values: list[str | float]) -> None:
        """
        Set the values of "Moment Y Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetMomentZDirection(self) -> list[float]:
        """
        Get the value of "Moment Z Direction".

        """

    def SetMomentZDirection(self, values: list[str | float]) -> None:
        """
        Set the values of "Moment Z Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetPrincipalMomentOfInertia(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Principal Moment of Inertia".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "kg.m2".
        """

    def SetPrincipalMomentOfInertia(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Principal Moment of Inertia".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "kg.m2".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
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

    def GetPeriodicReplication(self) -> bool:
        """
        Get the value of "Periodic Replication".

        """

    def SetPeriodicReplication(self, value: bool) -> None:
        """
        Set the value of "Periodic Replication".

        :param value:
            The value to set.
        """

    def GetNumberOfReplications(self) -> int:
        """
        Get the value of "Number of Replications".

        """

    def SetNumberOfReplications(self, value: str | int) -> None:
        """
        Set the value of "Number of Replications".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetReplicateGeometry(self) -> bool:
        """
        Get the value of "Replicate Geometry".

        """

    def SetReplicateGeometry(self, value: bool) -> None:
        """
        Set the value of "Replicate Geometry".

        :param value:
            The value to set.
        """

    def GetReplicateTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Replicate Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetReplicateTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Replicate Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
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

    def GetVolumeShearWorkRatio(self, unit: str | None = None) -> float:
        """
        Get the value of "Volume Shear Work Ratio".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m3/J".
        """

    def SetVolumeShearWorkRatio(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Volume Shear Work Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m3/J".
        """

    def GetWearModel(self) -> str:
        """
        Get "Wear Model" as a string.

        :return:
            The returned value will be one of [\'none\', \'archard\', \'custom\'].
        """

    def SetWearModel(self, value: str) -> None:
        """
        Set the value of "Wear Model".

        :param value:
            The value to set. Must be one of [\'none\', \'archard\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Wear Model" option.
        """

    def GetValidWearModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Wear Model".

        :return:
            The returned list is [\'none\', \'archard\', \'custom\'].
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
