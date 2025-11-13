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

from rocky30.process.geometry.coupled_boundary_process import (
    CoupledBoundaryProcessSubject as CoupledBoundaryProcessSubject,
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

class RACoupledWall(RABaseGeometry, ElementWithAddins, _WithMovementMixin):
    @classmethod
    def GetWrappedClass(self) -> type[object]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def HasMotionFrame(self) -> bool: ...
    def GetDisableTime(self, unit: str | None = None) -> float: ...
    def SetDisableTime(self, value: str | float, unit: str | None = None) -> None: ...
    def GetEnableTime(self, unit: str | None = None) -> float: ...
    def SetEnableTime(self, value: str | float, unit: str | None = None) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetMaterial(self): ...
    def SetMaterial(self, value) -> None: ...
    def GetAvailableMaterials(self): ...
