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

from ansys.rocky.app.api_element_item import ApiElementItem

class RADomainSettings(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for Domain Setings properties.

    This wrapper corresponds to the "Domain Settings" item on a project\'s data tree. Access it from
    the :class:`RAStudy` with:

    .. code-block:: python

        domain_settings = study.GetDomainSettings()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def CoordinateLimitsAtBoundaryLimits(self) -> bool: ...
    def GetCoordinateLimitsMinMax(self): ...
    def ResetDomainToGeometriesLimits(self) -> None:
        """
        Reset the domain settings coordinate limits based on the geometry bounding box.
        """

    def GetCoordinateLimitsMaxValues(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Coordinate Limits Max Values".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetCoordinateLimitsMaxValues(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Coordinate Limits Max Values".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetCoordinateLimitsMinValues(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Coordinate Limits Min Values".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetCoordinateLimitsMinValues(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Coordinate Limits Min Values".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetUseBoundaryLimits(self) -> bool:
        """
        Get the value of "Use Boundary Limits".

        """

    def SetUseBoundaryLimits(self, value: bool) -> None:
        """
        Set the value of "Use Boundary Limits".

        :param value:
            The value to set.
        """

    def EnableUseBoundaryLimits(self) -> None:
        """
        Set the value of "Use Boundary Limits" to True.
        """

    def DisableUseBoundaryLimits(self) -> None:
        """
        Set the value of "Use Boundary Limits" to False.
        """

    def IsUseBoundaryLimitsEnabled(self) -> bool:
        """
        Check if the "Use Boundary Limits" is enabled.

        """

    def GetPeriodicLimitsMaxCoordinates(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Periodic Limits Max Coordinates".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetPeriodicLimitsMaxCoordinates(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Periodic Limits Max Coordinates".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetPeriodicLimitsMinCoordinates(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Periodic Limits Min Coordinates".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetPeriodicLimitsMinCoordinates(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Periodic Limits Min Coordinates".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetPeriodicAtGeometryLimits(self) -> bool:
        """
        Get the value of "Periodic At Geometry Limits".

        """

    def SetPeriodicAtGeometryLimits(self, value: bool) -> None:
        """
        Set the value of "Periodic At Geometry Limits".

        :param value:
            The value to set.
        """

    def EnablePeriodicAtGeometryLimits(self) -> None:
        """
        Set the value of "Periodic At Geometry Limits" to True.
        """

    def DisablePeriodicAtGeometryLimits(self) -> None:
        """
        Set the value of "Periodic At Geometry Limits" to False.
        """

    def IsPeriodicAtGeometryLimitsEnabled(self) -> bool:
        """
        Check if the "Periodic At Geometry Limits" is enabled.

        """

    def GetCartesianPeriodicDirections(self) -> str:
        """
        Get "Cartesian Periodic Directions" as a string.

        :return:
            The returned value will be one of [\'NONE\', \'X\', \'Y\', \'XY\', \'Z\', \'XZ\', \'YZ\', \'XYZ\'].
        """

    def SetCartesianPeriodicDirections(self, value: str) -> None:
        """
        Set the value of "Cartesian Periodic Directions".

        :param value:
            The value to set. Must be one of [\'NONE\', \'X\', \'Y\', \'XY\', \'Z\', \'XZ\', \'YZ\', \'XYZ\'].
        :raises RockyApiError:
            If `value` is not a valid "Cartesian Periodic Directions" option.
        """

    def GetValidCartesianPeriodicDirectionsValues(self) -> list[str]:
        """
        Get a list of all possible values for "Cartesian Periodic Directions".

        :return:
            The returned list is [\'NONE\', \'X\', \'Y\', \'XY\', \'Z\', \'XZ\', \'YZ\', \'XYZ\'].
        """

    def GetInitialAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Initial Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetInitialAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Initial Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetNumberOfDivisions(self) -> int:
        """
        Get the value of "Number of Divisions".

        """

    def SetNumberOfDivisions(self, value: str | int) -> None:
        """
        Set the value of "Number of Divisions".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetCylindricalPeriodicDirections(self) -> str:
        """
        Get "Cylindrical Periodic Directions" as a string.

        :return:
            The returned value will be one of [\'X\', \'Y\', \'Z\'].
        """

    def SetCylindricalPeriodicDirections(self, value: str) -> None:
        """
        Set the value of "Cylindrical Periodic Directions".

        :param value:
            The value to set. Must be one of [\'X\', \'Y\', \'Z\'].
        :raises RockyApiError:
            If `value` is not a valid "Cylindrical Periodic Directions" option.
        """

    def GetValidCylindricalPeriodicDirectionsValues(self) -> list[str]:
        """
        Get a list of all possible values for "Cylindrical Periodic Directions".

        :return:
            The returned list is [\'X\', \'Y\', \'Z\'].
        """

    def GetDomainType(self) -> str:
        """
        Get "Domain Type" as a string.

        :return:
            The returned value will be one of [\'NONE\', \'CARTESIAN\', \'CYLINDRICAL\'].
        """

    def SetDomainType(self, value: str) -> None:
        """
        Set the value of "Domain Type".

        :param value:
            The value to set. Must be one of [\'NONE\', \'CARTESIAN\', \'CYLINDRICAL\'].
        :raises RockyApiError:
            If `value` is not a valid "Domain Type" option.
        """

    def GetValidDomainTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Domain Type".

        :return:
            The returned list is [\'NONE\', \'CARTESIAN\', \'CYLINDRICAL\'].
        """
