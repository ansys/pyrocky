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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RACFDPerParticleParameters(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing the set of CFD parameters for a specific Particle.

    Access individual sets of parameters via a :class:`RABaseCFDCoupling`'s parameters list:

    .. code-block:: python

        parameters_list = coupling_process.GetCFDParametersList()
        parameters = parameters_list.GetParametersFor('Particle <01>')
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetConvectiveHeatTransferLaw(self) -> str:
        """
        Get "Convective Heat Transfer Law" as a string.

        :return:
            The returned value will be one of [\'none\', \'RanzMarshall1952\', \'Whitaker1972\', \'Gunn1978\', \'custom\'].
        """

    def SetConvectiveHeatTransferLaw(self, value: str) -> None:
        """
        Set the value of "Convective Heat Transfer Law".

        :param value:
            The value to set. Must be one of [\'none\', \'RanzMarshall1952\', \'Whitaker1972\', \'Gunn1978\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Convective Heat Transfer Law" option.
        """

    def GetValidConvectiveHeatTransferLawValues(self) -> list[str]:
        """
        Get a list of all possible values for "Convective Heat Transfer Law".

        :return:
            The returned list is [\'none\', \'RanzMarshall1952\', \'Whitaker1972\', \'Gunn1978\', \'custom\'].
        """

    def GetDragLaw(self) -> str:
        """
        Get "Drag Law" as a string.

        :return:
            The returned value will be one of [\'WenYu1966\', \'SchillerNaumann1933\', \'HaiderLevenspiel1989\', \'Ganser1993\', \'Ergun1958\', \'GidaspowBezburuahDing1992\', \'HuilinGidaspow2003\', \'DiFelice1994\', \'Dallavalle1948\', \'MarheinekeWegener2011\', \'SyamlalOBrien1987\', \'MorsiAlexander1972\', \'HillKochLadd2001\', \'HillKoch2001\', \'custom\'].
        """

    def SetDragLaw(self, value: str) -> None:
        """
        Set the value of "Drag Law".

        :param value:
            The value to set. Must be one of [\'WenYu1966\', \'SchillerNaumann1933\', \'HaiderLevenspiel1989\', \'Ganser1993\', \'Ergun1958\', \'GidaspowBezburuahDing1992\', \'HuilinGidaspow2003\', \'DiFelice1994\', \'Dallavalle1948\', \'MarheinekeWegener2011\', \'SyamlalOBrien1987\', \'MorsiAlexander1972\', \'HillKochLadd2001\', \'HillKoch2001\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Drag Law" option.
        """

    def GetValidDragLawValues(self) -> list[str]:
        """
        Get a list of all possible values for "Drag Law".

        :return:
            The returned list is [\'WenYu1966\', \'SchillerNaumann1933\', \'HaiderLevenspiel1989\', \'Ganser1993\', \'Ergun1958\', \'GidaspowBezburuahDing1992\', \'HuilinGidaspow2003\', \'DiFelice1994\', \'Dallavalle1948\', \'MarheinekeWegener2011\', \'SyamlalOBrien1987\', \'MorsiAlexander1972\', \'HillKochLadd2001\', \'HillKoch2001\', \'custom\'].
        """

    def GetLiftLaw(self) -> str:
        """
        Get "Lift Law" as a string.

        :return:
            The returned value will be one of [\'none\', \'Saffman1968\', \'Mei1992\', \'custom\'].
        """

    def SetLiftLaw(self, value: str) -> None:
        """
        Set the value of "Lift Law".

        :param value:
            The value to set. Must be one of [\'none\', \'Saffman1968\', \'Mei1992\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Lift Law" option.
        """

    def GetValidLiftLawValues(self) -> list[str]:
        """
        Get a list of all possible values for "Lift Law".

        :return:
            The returned list is [\'none\', \'Saffman1968\', \'Mei1992\', \'custom\'].
        """

    def GetMorsiAndAlexanderK1(self) -> float:
        """
        Get the value of "Morsi And Alexander K1".

        """

    def SetMorsiAndAlexanderK1(self, value: str | float) -> None:
        """
        Set the value of "Morsi And Alexander K1".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMorsiAndAlexanderK2(self) -> float:
        """
        Get the value of "Morsi And Alexander K2".

        """

    def SetMorsiAndAlexanderK2(self, value: str | float) -> None:
        """
        Set the value of "Morsi And Alexander K2".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMorsiAndAlexanderK3(self) -> float:
        """
        Get the value of "Morsi And Alexander K3".

        """

    def SetMorsiAndAlexanderK3(self, value: str | float) -> None:
        """
        Set the value of "Morsi And Alexander K3".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSyamlalObrienC1(self) -> float:
        """
        Get the value of "Syamlal Obrien C1".

        """

    def SetSyamlalObrienC1(self, value: str | float) -> None:
        """
        Set the value of "Syamlal Obrien C1".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSyamlalObrienD1(self) -> float:
        """
        Get the value of "Syamlal Obrien D1".

        """

    def SetSyamlalObrienD1(self, value: str | float) -> None:
        """
        Set the value of "Syamlal Obrien D1".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTorqueLaw(self) -> str:
        """
        Get "Torque Law" as a string.

        :return:
            The returned value will be one of [\'none\', \'DennisSinghIngham1980\', \'custom\'].
        """

    def SetTorqueLaw(self, value: str) -> None:
        """
        Set the value of "Torque Law".

        :param value:
            The value to set. Must be one of [\'none\', \'DennisSinghIngham1980\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Torque Law" option.
        """

    def GetValidTorqueLawValues(self) -> list[str]:
        """
        Get a list of all possible values for "Torque Law".

        :return:
            The returned list is [\'none\', \'DennisSinghIngham1980\', \'custom\'].
        """

    def GetUseUserDefinedConstants(self) -> bool:
        """
        Get the value of "Use User Defined Constants".

        """

    def SetUseUserDefinedConstants(self, value: bool) -> None:
        """
        Set the value of "Use User Defined Constants".

        :param value:
            The value to set.
        """

    def GetVirtualMassLaw(self) -> str:
        """
        Get "Virtual Mass Law" as a string.

        :return:
            The returned value will be one of [\'none\', \'constant\', \'Paladino2005\', \'IshiiMishima1984\', \'custom\'].
        """

    def SetVirtualMassLaw(self, value: str) -> None:
        """
        Set the value of "Virtual Mass Law".

        :param value:
            The value to set. Must be one of [\'none\', \'constant\', \'Paladino2005\', \'IshiiMishima1984\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Virtual Mass Law" option.
        """

    def GetValidVirtualMassLawValues(self) -> list[str]:
        """
        Get a list of all possible values for "Virtual Mass Law".

        :return:
            The returned list is [\'none\', \'constant\', \'Paladino2005\', \'IshiiMishima1984\', \'custom\'].
        """

class RACFDParametersList(RAList[RACFDPerParticleParameters]):
    """
    Rocky PrePost Scripting wrapper to manipulate the list of per-particle CFD parameters in a CFD coupling configuration.

    To get the :class:`RACFDParametersList` from a CFD coupling wrapper (such as :class:`RAConstantOneWayCoupling`,
    :class:`RAFluentOneWaySteadyCoupling`, or :class:`RAFluentTwoWayCoupling`), use:

    .. code-block:: python

        parameters_list = coupling_process.GetCFDParametersList()

    The :class:`RACFDParametersList` class acts as a regular Python list, with the usual methods to iterate
    and access individual parameter sets. Note that it's not possible to add and remove items from the
    list, as they are added and removed automatically as Particles are added or removed from the project.

    The items in the parameters list are of type :class:`RACFDPerParticleParameters`.
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetParametersFor(self, particle):
        """
        Get the set of CFD parameters for a given Particle.

        :param RAParticle or str particle:
            Either the PrePost Scripting wrapper for a Particle, or the name of the Particle.
        :rtype: RACFDPerParticleParameters
        """

    def New(self) -> None:
        """
        Overriden: Raises an error when called.

        RACFDPerParticleParameters are created and removed automatically when Particles are added
        or removed.
        """

    def Remove(self, item) -> None:
        """
        Overriden: Raises an error when called.

        RACFDPerParticleParameters are created and removed automatically when Particles are added
        or removed.
        """

    def Clear(self) -> None:
        """
        Overriden: Raises an error when called.

        RACFDPerParticleParameters are created and removed automatically when Particles are added
        or removed.
        """

    def __delitem__(self, index) -> None:
        """
        Overriden: Raises an error when called.

        RACFDPerParticleParameters are created and removed automatically when Particles are added
        or removed.
        """
