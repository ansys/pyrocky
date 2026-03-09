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

from rocky30.models.input.volume_fill import VolumeFill as VolumeFill

from ansys.rocky.app._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_particle import RAParticle as RAParticle
from ansys.rocky.app.ra_volumetric_inlet_properties import (
    RAVolumetricInletProperties as RAVolumetricInletProperties,
)
from ansys.rocky.app.ra_volumetric_inlet_properties import (
    RAVolumetricInletPropertiesList as RAVolumetricInletPropertiesList,
)
from ansys.rocky.app.ra_wall import RAWall as RAWall

class RAVolumetricInlet(ApiElementItem, _RAOrientationMixin):
    """
    Rocky PrePost Scripting wrapper for a single Volume Fill input.

    This wrapper class corresponds to an individual entry under the "Inputs" item on the project\'s
    data tree. Particle inputs can be retrieved from the :class:`RAStudy` or the
    :class:`RAInletsOutletsCollection` via:

    .. code-block:: python

        input_1 = study.GetElement(\'Volume Fill <1>\')
        input_2 = input_collection.GetParticleInput(\'Volume Fill <2>\')

    Instances of :class:`RAVolumetricInlet` comprise two parts: Properties that can be manipulated
    directly, such as the input\'s name and the seed point, and the input properties list
    that describe which particles enter via this input and with its mass, temperature, etc.
    This list must be manipulated via the :class:`RAParticleInputPropertiesList` returned by
    :meth:`GetInputPropertiesList()`.
    """

    @classmethod
    def GetWrappedClass(self) -> type[VolumeFill]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetInputPropertiesList(self) -> RAVolumetricInletPropertiesList:
        """
        Return a list of input properties
        """

    def AddParticle(self, particle: RAParticle | str) -> RAVolumetricInletProperties:
        """
        Add a new particle to the Volumetric Inlet input properties list.

        : return: A new :class:`RAVolumetricInletProperties` object that can be used to set
        """

    def RemoveParticle(self, particle: RAParticle | str) -> None:
        """
        Remove a particle from the Particle Inlet input properties list.

        :param particle: The particle to remove, either as an :class:`RAParticle` object or by name.
        """

    def GetBoxCenter(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Box Center".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetBoxCenter(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Box Center".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetBoxDimensions(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Box Dimensions".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetBoxDimensions(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Box Dimensions".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetUseGeometriesToCompute(self) -> bool:
        """
        Get the value of "Use Geometries To Compute".

        """

    def SetUseGeometriesToCompute(self, value: bool) -> None:
        """
        Set the value of "Use Geometries To Compute".

        :param value:
            The value to set.
        """

    def GetGapScaleFactor(self) -> float:
        """
        Get the value of "Gap Scale Factor".

        """

    def SetGapScaleFactor(self, value: str | float) -> None:
        """
        Set the value of "Gap Scale Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetInitialVelocity(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Initial Velocity".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m/s".
        """

    def SetInitialVelocity(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Initial Velocity".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m/s".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
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

    def GetSeedCoordinates(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Seed Coordinates".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetSeedCoordinates(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Seed Coordinates".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetInjectionTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Injection Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetInjectionTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Injection Time".

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

    def GetSphMass(self, unit: str | None = None) -> float:
        """
        Get the value of "Sph Mass".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg".
        """

    def SetSphMass(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Sph Mass".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg".
        """

    def GetSphTemperature(self, unit: str | None = None) -> float:
        """
        Get the value of "Sph Temperature".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "K".
        """

    def SetSphTemperature(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Sph Temperature".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "K".
        """

    def GetUseBoxCenterAsSeedPoint(self) -> bool:
        """
        Get the value of "Use Box Center As Seed Point".

        """

    def SetUseBoxCenterAsSeedPoint(self, value: bool) -> None:
        """
        Set the value of "Use Box Center As Seed Point".

        :param value:
            The value to set.
        """

    def EnableUseBoxCenterAsSeedPoint(self) -> None:
        """
        Set the value of "Use Box Center As Seed Point" to True.
        """

    def DisableUseBoxCenterAsSeedPoint(self) -> None:
        """
        Set the value of "Use Box Center As Seed Point" to False.
        """

    def IsUseBoxCenterAsSeedPointEnabled(self) -> bool:
        """
        Check if the "Use Box Center As Seed Point" is enabled.

        """

    def GetGeometries(self):
        """
        Get the "Geometries".

        :rtype: List[:class:`RAWall`]
            A list of :class:`RAWall`.
        """

    def SetGeometries(self, values) -> None:
        """
        Set the "Geometries".

        :param List[str, :class:`RAWall`] values:
            A list with names, :class:`RAWall`.
        """

    def GetAvailableGeometries(self):
        """
        Get all available Geometries.

        :rtype: List[:class:`RAWall`]
            A list of :class:`RAWall`.
        """
