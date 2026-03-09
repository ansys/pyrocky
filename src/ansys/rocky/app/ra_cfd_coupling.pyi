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

from rocky30.process.cfd.cfd_coupling import CFDCouplingMode as CFDCouplingMode

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_airflow import RAAirFlow as RAAirFlow
from ansys.rocky.app.ra_cfd_parameters import RACFDParametersList as RACFDParametersList
from ansys.rocky.app.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.app.ra_semi_resolved_coupling import (
    RAFluentSemiResolvedCoupling as RAFluentSemiResolvedCoupling,
)

class RACFDCoupling(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper to configure the CFD coupling mode in a project.

    This wrapper can be accessed directly via the project's :class:`RAStudy`:

    .. code-block:: python

        cfd_coupling = study.GetCFDCoupling()
        cfd_coupling.SetupFluentTwoWay('fluent.cas')
        two_way_process = cfd_coupling.GetCouplingProcess()
    """

    @classmethod
    def GetWrappedClass(self) -> type: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def SetupNoCoupling(self):
        """
        Configure the project to use no CFD coupling.
        """

    def SetupOneWayLBM(self) -> RAAirFlow | None:
        """
        Configure the project to use 1-Way LBM.
        """

    def GetOneWayLBM(self) -> RAAirFlow | None:
        """
        Get the PrePost Scripting wrapper for 1-Way LBM properties.

        Returns `None` if the current CFD coupling mode isn't Air Flow.

        :rtype: RAAirFlow
        """

    def SetupOneWayFluent(self, f2r_filename: str) -> RACFDCouplingTypes | None:
        """
        Configure the project to use 1-Way Fluent.

        :param f2r_filename: str
            The exported file name describing the Fluent simulation
        """

    def SetupTwoWayFluent(self, cas_filename: str) -> RACFDCouplingTypes | None:
        """
        Configure the project to use 2-Way Fluent.

        :param cas_filename: str
            The Fluent file name describing the Fluent simulation
        """

    def SetupFluentTwoWaySemiResolved(
        self, cas_filename: str
    ) -> RACFDCouplingTypes | None:
        """
        Configure the project to use Fluent Two-Way Semi Resolved.

        :param cas_filename:
            The filename describing the Fluent simulation
        """

    def SetupOneWayConstant(self) -> RACFDCouplingTypes | None:
        """
        Configure the project to use 1-Way Constant.
        """

    def GetCouplingMode(self) -> str:
        """
        :rtype: unicode
        :return:
            The current coupling mode
        """

    def GetCouplingProcess(self) -> RACFDCouplingTypes | None:
        """
        :return:
            The configured coupling process
        """

    def SetCurrentCouplingPartId(self) -> None: ...

class RABaseCFDCoupling(RAGridProcessElementItem):
    """
    Base class for PrePost Scripting wrappers for the various CFD coupling modes.
    """

    def GetCFDParametersList(self) -> RACFDParametersList:
        """
        Get the list of per-Particle CFD parameter sets.

        :rtype: RACFDParametersList
        """

    def SetPartIdIfValid(self) -> None:
        """
        Subclasses should implement this method if it's a Process with visualization
        """

    def GetConvectiveHeatTransferLaw(self):
        """
        Get the current "Convective Heat Transfer Law". This is a shortcut to access the "Convective Heat Transfer Law" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetConvectiveHeatTransferLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Convective Heat Transfer Law".
        """

    def SetConvectiveHeatTransferLaw(self, value) -> None:
        """
        Set the current "Convective Heat Transfer Law". This is a shortcut to set the "Convective Heat Transfer Law" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetConvectiveHeatTransferLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetDragLaw(self):
        """
        Get the current "Drag Law". This is a shortcut to access the "Drag Law" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetDragLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Drag Law".
        """

    def SetDragLaw(self, value) -> None:
        """
        Set the current "Drag Law". This is a shortcut to set the "Drag Law" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetDragLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetLiftLaw(self):
        """
        Get the current "Lift Law". This is a shortcut to access the "Lift Law" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetLiftLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Lift Law".
        """

    def SetLiftLaw(self, value) -> None:
        """
        Set the current "Lift Law". This is a shortcut to set the "Lift Law" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetLiftLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetMorsiAndAlexanderK1(self):
        """
        Get the current "Morsi And Alexander K1". This is a shortcut to access the "Morsi And Alexander K1" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetMorsiAndAlexanderK1()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Morsi And Alexander K1".
        """

    def SetMorsiAndAlexanderK1(self, value) -> None:
        """
        Set the current "Morsi And Alexander K1". This is a shortcut to set the "Morsi And Alexander K1" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetMorsiAndAlexanderK1()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetMorsiAndAlexanderK2(self):
        """
        Get the current "Morsi And Alexander K2". This is a shortcut to access the "Morsi And Alexander K2" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetMorsiAndAlexanderK2()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Morsi And Alexander K2".
        """

    def SetMorsiAndAlexanderK2(self, value) -> None:
        """
        Set the current "Morsi And Alexander K2". This is a shortcut to set the "Morsi And Alexander K2" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetMorsiAndAlexanderK2()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetMorsiAndAlexanderK3(self):
        """
        Get the current "Morsi And Alexander K3". This is a shortcut to access the "Morsi And Alexander K3" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetMorsiAndAlexanderK3()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Morsi And Alexander K3".
        """

    def SetMorsiAndAlexanderK3(self, value) -> None:
        """
        Set the current "Morsi And Alexander K3". This is a shortcut to set the "Morsi And Alexander K3" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetMorsiAndAlexanderK3()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetSyamlalObrienC1(self):
        """
        Get the current "Syamlal Obrien C1". This is a shortcut to access the "Syamlal Obrien C1" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetSyamlalObrienC1()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Syamlal Obrien C1".
        """

    def SetSyamlalObrienC1(self, value) -> None:
        """
        Set the current "Syamlal Obrien C1". This is a shortcut to set the "Syamlal Obrien C1" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetSyamlalObrienC1()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetSyamlalObrienD1(self):
        """
        Get the current "Syamlal Obrien D1". This is a shortcut to access the "Syamlal Obrien D1" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetSyamlalObrienD1()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Syamlal Obrien D1".
        """

    def SetSyamlalObrienD1(self, value) -> None:
        """
        Set the current "Syamlal Obrien D1". This is a shortcut to set the "Syamlal Obrien D1" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetSyamlalObrienD1()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetTorqueLaw(self):
        """
        Get the current "Torque Law". This is a shortcut to access the "Torque Law" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetTorqueLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Torque Law".
        """

    def SetTorqueLaw(self, value) -> None:
        """
        Set the current "Torque Law". This is a shortcut to set the "Torque Law" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetTorqueLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetUseUserDefinedConstants(self):
        """
        Get the current "Use User Defined Constants". This is a shortcut to access the "Use User Defined Constants" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetUseUserDefinedConstants()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Use User Defined Constants".
        """

    def SetUseUserDefinedConstants(self, value) -> None:
        """
        Set the current "Use User Defined Constants". This is a shortcut to set the "Use User Defined Constants" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetUseUserDefinedConstants()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

    def GetVirtualMassLaw(self):
        """
        Get the current "Virtual Mass Law". This is a shortcut to access the "Virtual Mass Law" of the individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.GetVirtualMassLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet, or if the :class:`RACFDPerParticleParameters`
            for the Particles have different values for the "Virtual Mass Law".
        """

    def SetVirtualMassLaw(self, value) -> None:
        """
        Set the current "Virtual Mass Law". This is a shortcut to set the "Virtual Mass Law" of all individual
        :class:`RACFDPerParticleParameters` configured in the coupling.

        See also :meth:`RACFDPerParticleParameters.SetVirtualMassLaw()`

        :raises RockyApiError:
            If there are no Particles in the project yet.
        """

class RAConstantOneWayCoupling(RABaseCFDCoupling):
    """
    Rocky PrePost Scripting wrapper for One-Way Constant CFD coupling properties.

    This wrapper can be accessed via the project's :class:`RACFDCoupling`:

    .. code-block:: python

        cfd_coupling = study.GetCFDCoupling()
        cfd_coupling.SetupOneWayConstant()
        constant_one_way = cfd_coupling.GetCouplingProcess()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetDensity(self, unit: str | None = None) -> float:
        """
        Get the value of "Density".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg/m3".
        """

    def SetDensity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Density".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg/m3".
        """

    def GetSpecificHeat(self, unit: str | None = None) -> float:
        """
        Get the value of "Specific Heat".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg.K".
        """

    def SetSpecificHeat(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Specific Heat".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg.K".
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

    def GetThermalConductivity(self, unit: str | None = None) -> float:
        """
        Get the value of "Thermal Conductivity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "W/m.K".
        """

    def SetThermalConductivity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Thermal Conductivity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "W/m.K".
        """

    def GetTurbulentDissipationRate(self, unit: str | None = None) -> float:
        """
        Get the value of "Turbulent Dissipation Rate".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "W/kg".
        """

    def SetTurbulentDissipationRate(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Turbulent Dissipation Rate".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "W/kg".
        """

    def GetTurbulentKineticEnergy(self, unit: str | None = None) -> float:
        """
        Get the value of "Turbulent Kinetic Energy".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg".
        """

    def SetTurbulentKineticEnergy(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Turbulent Kinetic Energy".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg".
        """

    def GetUseTurbulentDispersion(self) -> bool:
        """
        Get the value of "Use Turbulent Dispersion".

        """

    def SetUseTurbulentDispersion(self, value: bool) -> None:
        """
        Set the value of "Use Turbulent Dispersion".

        :param value:
            The value to set.
        """

    def EnableTurbulentDispersion(self) -> None:
        """
        Set the value of "Turbulent Dispersion" to True.
        """

    def DisableTurbulentDispersion(self) -> None:
        """
        Set the value of "Turbulent Dispersion" to False.
        """

    def IsTurbulentDispersionEnabled(self) -> bool:
        """
        Check if the "Turbulent Dispersion" is enabled.

        """

    def GetVelocity(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Velocity".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m/s".
        """

    def SetVelocity(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Velocity".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m/s".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetViscosity(self, unit: str | None = None) -> float:
        """
        Get the value of "Viscosity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa.s".
        """

    def SetViscosity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Viscosity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa.s".
        """

RACFDCouplingTypes = RAAirFlow | RABaseCFDCoupling | RAFluentSemiResolvedCoupling
