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
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_particle import RAParticle as RAParticle
from ansys.rocky.app.ra_particle_inlet_properties import (
    RAParticleInletPropertiesList as RAParticleInletPropertiesList,
)

class RAParticleInlet(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a single Continuous Injection input.

    This wrapper class corresponds to an individual entry under the "Inputs" item on the project\'s
    data tree. Particle inputs can be retrieved from the :class:`RAStudy` or the
    :class:`RAInletsOutletsCollection` via:

    .. code-block:: python

        input_1 = study.GetElement(\'Continuous Injection <1>\')
        input_2 = input_collection.GetParticleInput(\'Continuous Injection <2>\')

    Instances of :class:`RAParticleInlet` comprise two parts: Properties that can be manipulated
    directly, such as the input\'s name and the particle entry point, and the input properties list
    that describe which particles enter via this input and with each mass flow rate, temperature, etc.
    This list must be manipulated via the :class:`RAParticleInputPropertiesList` returned by
    :meth:`GetInputPropertiesList()`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetInputPropertiesList(self) -> RAParticleInletPropertiesList:
        """
        Return a list of input properties
        """

    def AddParticle(self, particle: RAParticle | str) -> RAParticleInletPropertiesList:
        """
        Add a new particle to the Particle Inlet input properties list.

        : return: A new :class:`RAParticleInletPropertiesList` object that can be used to set
        """

    def RemoveParticle(self, particle: RAParticle | str) -> None:
        """
        Remove a particle from the Particle Inlet input properties list.

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

    def GetForcePacking(self) -> bool:
        """
        Get the value of "Force Packing".

        """

    def SetForcePacking(self, value: bool) -> None:
        """
        Set the value of "Force Packing".

        :param value:
            The value to set.
        """

    def EnableForcePacking(self) -> None:
        """
        Set the value of "Force Packing" to True.
        """

    def DisableForcePacking(self) -> None:
        """
        Set the value of "Force Packing" to False.
        """

    def IsForcePackingEnabled(self) -> bool:
        """
        Check if the "Force Packing" is enabled.

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

    def GetStopAllAtStopTime(self) -> bool:
        """
        Get the value of "Stop All At Stop Time".

        """

    def SetStopAllAtStopTime(self, value: bool) -> None:
        """
        Set the value of "Stop All At Stop Time".

        :param value:
            The value to set.
        """

    def EnableStopAllAtStopTime(self) -> None:
        """
        Set the value of "Stop All At Stop Time" to True.
        """

    def DisableStopAllAtStopTime(self) -> None:
        """
        Set the value of "Stop All At Stop Time" to False.
        """

    def IsStopAllAtStopTimeEnabled(self) -> bool:
        """
        Check if the "Stop All At Stop Time" is enabled.

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

    def GetTargetNormalVelocity(self, unit: str | None = None) -> float:
        """
        Get the value of "Target Normal Velocity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetTargetNormalVelocity(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Target Normal Velocity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetUseTargetNormalVelocity(self) -> bool:
        """
        Get the value of "Use Target Normal Velocity".

        """

    def SetUseTargetNormalVelocity(self, value: bool) -> None:
        """
        Set the value of "Use Target Normal Velocity".

        :param value:
            The value to set.
        """

    def EnableUseTargetNormalVelocity(self) -> None:
        """
        Set the value of "Use Target Normal Velocity" to True.
        """

    def DisableUseTargetNormalVelocity(self) -> None:
        """
        Set the value of "Use Target Normal Velocity" to False.
        """

    def IsUseTargetNormalVelocityEnabled(self) -> bool:
        """
        Check if the "Use Target Normal Velocity" is enabled.

        """

    def GetUxLocal(self, unit: str | None = None) -> float:
        """
        Get the value of "Ux Local".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetUxLocal(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Ux Local".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetUzLocal(self, unit: str | None = None) -> float:
        """
        Get the value of "Uz Local".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetUzLocal(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Uz Local".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """

    def GetSphInjectionEnabled(self) -> bool:
        """
        Get the value of "Sph Injection Enabled".

        """

    def SetSphInjectionEnabled(self, value: bool) -> None:
        """
        Set the value of "Sph Injection Enabled".

        :param value:
            The value to set.
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

    def GetEntryPoint(self):
        """
        Get the "Entry Point".

        :rtype: :class:`RAInletGeometry`, :class:`RAFeedConveyor`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`
        """

    def SetEntryPoint(self, value) -> None:
        """
        Set the "Entry Point".

        :param unicode, :class:`RAInletGeometry`, :class:`RAFeedConveyor`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableEntryPoints(self):
        """
        Get all available Entry Points.

        :rtype: List[:class:`RAInletGeometry`, :class:`RAFeedConveyor`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`]
            A list of :class:`RAInletGeometry`, :class:`RAFeedConveyor`, :class:`RARectangularSurface`, :class:`RACircularSurface`, :class:`RASurface`.
        """
