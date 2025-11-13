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

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.regions_of_interest.roi_cylinder import RoiCylinder as RoiCylinder

from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_orientation_mixin import (
    _RAOrientationMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion._with_movement_mixin import (
    _WithMovementMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RARegionOfInterestCylinder(
    RAGridProcessElementItem, _WithMovementMixin, _RAOrientationMixin
):
    @classmethod
    def GetWrappedClass(cls) -> type: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F: ...
    def GetCenter(self, unit: str | None = None) -> list[float]: ...
    def SetCenter(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None: ...
    def GetFinalAngle(self, unit: str | None = None) -> float: ...
    def SetFinalAngle(self, value: str | float, unit: str | None = None) -> None: ...
    def GetHeight(self, unit: str | None = None) -> float: ...
    def SetHeight(self, value: str | float, unit: str | None = None) -> None: ...
    def GetInitialAngle(self, unit: str | None = None) -> float: ...
    def SetInitialAngle(self, value: str | float, unit: str | None = None) -> None: ...
    def GetInternalFactor(self, unit: str | None = None) -> float: ...
    def SetInternalFactor(self, value: str | float, unit: str | None = None) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetRadius(self, unit: str | None = None) -> float: ...
    def SetRadius(self, value: str | float, unit: str | None = None) -> None: ...
