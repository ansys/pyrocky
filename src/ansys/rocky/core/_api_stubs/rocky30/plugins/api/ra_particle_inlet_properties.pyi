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

from rocky30.models.input.particle_inlet import (
    ParticleInletProperties as ParticleInletProperties,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAParticleInletProperties(ApiElementItem, ElementWithAddins):
    """
    Rocky PrePost Scripting wrapper for a single entry in a single Particle Input's input list.

    Access this wrapper from a given :class:`RAParticleInlet` with:

    .. code-block:: python

        input_properties_list = particle_input.GetInputPropertiesList()
        input_properties_1 = input_properties_list.New()
        input_properties_1.SetParticle('Particle 1')
        input_properties_1.SetMassFlowRate(100, 't/h')
    """

    @classmethod
    def GetWrappedClass(self) -> type[ParticleInletProperties]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetMassFlowRate(self, unit: str | None = None) -> float:
        """
        Get the value of "Mass Flow Rate".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "t/h".
        """

    def SetMassFlowRate(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Mass Flow Rate".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "t/h".
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

    def GetParticle(self):
        """
        Get the "Particle".

        :rtype: :class:`RAParticle`
        """

    def SetParticle(self, value) -> None:
        """
        Set the "Particle".

        :param unicode, :class:`RAParticle` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableParticles(self):
        """
        Get all available Particles.

        :rtype: List[:class:`RAParticle`]
            A list of :class:`RAParticle`.
        """

class RAParticleInletPropertiesList(RAList):
    """
    Rocky PrePost Scripting wrapper for the input entries list in a single Particle Input.

    To get the :class:`RAParticleInletPropertiesList` from a :class:`RAParticleInlet`, use:

    .. code-block:: python

        input_properties_list = particle_input.GetInputPropertiesList()

    :class:`RAParticleInletPropertiesList` contains methods to add, remove and retrieve individual
    input property entries. It corresponds to the list of entries on a Particle Input\'s "Input" tab
    on the Rocky UI.

    The following examples add, remove and access individual entries in the input properties list:

    .. code-block:: python

        # Add new items
        input_properties_1 = input_properties_list.New()

        # Access and modify items
        input_properties_2 = input_properties_list[0]
        input_properties_2.SetParticle(\'Particle 1\')

        # Remove items
        input_properties_list.Remove(input_properties_2)
        del input_properties_list[0]
        input_properties_list.Clear()

    The :class:`RAParticleInletPropertiesList` is a list of :class:`RAParticleInletProperties`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
