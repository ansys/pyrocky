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

from rocky30.models.input.inlet_type import InletType as InletType
from rocky30.models.input.inlets_outlets_collection import (
    InletsOutletsCollection as InletsOutletsCollection,
)
from rocky30.plugins.inlets_outlets.actions.inlets_outlets_action import (
    CreateInletOutletAction as CreateInletOutletAction,
)

from ansys.rocky.app.ra_custom_input import RACustomInput as RACustomInput
from ansys.rocky.app.ra_fluid_inlet import RAFluidInlet as RAFluidInlet
from ansys.rocky.app.ra_list import RAList as RAList
from ansys.rocky.app.ra_outlet import RAOutlet as RAOutlet
from ansys.rocky.app.ra_particle_inlet import RAParticleInlet as RAParticleInlet
from ansys.rocky.app.ra_volumetric_inlet import RAVolumetricInlet as RAVolumetricInlet

class RAInletsOutletsCollection(RAList[RAParticleInlet]):
    """
    Rocky PrePost Scripting wrapper for the collection of particle inputs in a project.

    This wrapper corresponds to the "Inputs" item in the project\'s data tree. To retrieve the
    :class:`RAInletsOutletsCollection` from a :class:`RAStudy`, use:

    .. code-block:: python

        input_collection = study.GetInletsOutletsCollection()

    Instances of the :class:`RAInletsOutletsCollection` class act as regular Python lists, and can be
    iterated on, accessed via index, etc:

    .. code-block:: python

        input_1 = input_collection.New()
        input_2 = input_collection[1]
        del input_collection[0]
        for input in input_collection:
            print(input.GetName())

    Items in this list are of type :class:`RAParticleInlet`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def New(self):
        """
        Add a new item. Returns the newly created item.

        :rtype: ApiElementItem
        """

    def AddParticleInlet(self) -> RAParticleInlet:
        """
        Add a new ParticleInlet. Returns the newly created item.
        """

    def AddOutlet(self) -> RAOutlet:
        """
        Add a new Outlet. Returns the newly created item.
        """

    def AddVolumetricInlet(self) -> RAVolumetricInlet:
        """
        Add a new VolumeFill. Returns the newly created item.
        """

    def AddCustomInput(self) -> RACustomInput:
        """
        Add a new CustomInput. Returns the newly created item.
        """

    def AddFluidInlet(self) -> RAFluidInlet:
        """
        Add a new SPHInlet. Returns the newly created item.
        """

    def GetParticleInputNames(self):
        """
        Get the names of all particle inputs.

        :rtype: list(unicode)
        """

    def GetParticleInput(self, input_name):
        """
        Get the particle input with the given name.

        :param unicode input_name:
        :rtype: RAParticleInlet
        """
