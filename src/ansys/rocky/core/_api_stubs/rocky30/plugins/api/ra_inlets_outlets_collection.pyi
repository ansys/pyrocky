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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_custom_input import (
    RACustomInput as RACustomInput,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_fluid_inlet import (
    RAFluidInlet as RAFluidInlet,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_outlet import RAOutlet as RAOutlet
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle_inlet import (
    RAParticleInlet as RAParticleInlet,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_volumetric_inlet import (
    RAVolumetricInlet as RAVolumetricInlet,
)

class RAInletsOutletsCollection(RAList[RAParticleInlet]):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def New(self): ...
    def AddParticleInlet(self) -> RAParticleInlet: ...
    def AddOutlet(self) -> RAOutlet: ...
    def AddVolumetricInlet(self) -> RAVolumetricInlet: ...
    def AddCustomInput(self) -> RACustomInput: ...
    def AddFluidInlet(self) -> RAFluidInlet: ...
    def GetParticleInputNames(self): ...
    def GetParticleInput(self, input_name): ...
