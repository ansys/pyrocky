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
from typing import List, Optional, Union

from rocky30.models.particle.particle_assembly import (
    ParticleAssemblyCustom as ParticleAssemblyCustom,
)
from rocky30.models.particle.particle_assembly import (
    ParticleAssemblyPart as ParticleAssemblyPart,
)
from rocky30.models.particle.particle_assembly import (
    ParticleAssemblyPartList as ParticleAssemblyPartList,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAParticleAssemblyPart(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[ParticleAssemblyPart]: ...
    @classmethod
    def GetClassName(self): ...
    def GetAngle(self, unit: Optional[str] = ...) -> float: ...
    def SetAngle(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetPositionX(self, unit: Optional[str] = ...) -> float: ...
    def SetPositionX(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetPositionY(self, unit: Optional[str] = ...) -> float: ...
    def SetPositionY(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetPositionZ(self, unit: Optional[str] = ...) -> float: ...
    def SetPositionZ(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetRotationX(self, unit: Optional[str] = ...) -> float: ...
    def SetRotationX(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetRotationY(self, unit: Optional[str] = ...) -> float: ...
    def SetRotationY(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetRotationZ(self, unit: Optional[str] = ...) -> float: ...
    def SetRotationZ(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetScale(self, unit: Optional[str] = ...) -> float: ...
    def SetScale(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetParticle(self): ...
    def SetParticle(self, value) -> None: ...
    def GetAvailableParticles(self): ...

class RAParticleAssemblyPartList(RAList[RAParticleAssemblyPart]):
    @classmethod
    def GetWrappedClass(self) -> type[ParticleAssemblyPartList]: ...
    @classmethod
    def GetClassName(self) -> str: ...

class RAParticleAssemblyCustom(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[ParticleAssemblyCustom]: ...
    @classmethod
    def GetClassName(self): ...
    def GetArea(self, unit: Optional[str] = ...) -> float: ...
    def SetArea(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetCenterOfMass(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetCenterOfMass(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetEnabled(self) -> bool: ...
    def SetEnabled(self, value: bool) -> None: ...
    def GetGeometricCenter(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetGeometricCenter(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetInertiaXAxis(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetInertiaXAxis(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetInertiaYAxis(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetInertiaYAxis(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetInertiaZAxis(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetInertiaZAxis(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetMass(self, unit: Optional[str] = ...) -> float: ...
    def SetMass(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
    def GetMomentOfInertia(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetMomentOfInertia(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetPorosity(self, unit: Optional[str] = ...) -> float: ...
    def SetPorosity(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetVolume(self, unit: Optional[str] = ...) -> float: ...
    def SetVolume(self, value: Union[str, float], unit: Optional[str] = ...) -> None: ...
