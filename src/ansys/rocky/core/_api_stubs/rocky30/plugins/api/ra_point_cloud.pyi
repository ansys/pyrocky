# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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

from pathlib import Path
from typing import Optional, Union

from rocky30.models.point_cloud.point_cloud import PointCloud as PointCloud

from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion._with_movement_mixin import (
    _WithMovementMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RAPointCloud(RAGridProcessElementItem, ElementWithAddins, _WithMovementMixin):
    @classmethod
    def GetWrappedClass(self) -> type[PointCloud]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetFilePath(self) -> str: ...
    def SetFilePath(self, file_path: Union[str, Path]) -> None: ...
    def IsTransient(self) -> bool: ...
    def GetEnablePeriodic(self) -> bool: ...
    def SetEnablePeriodic(self, value: bool) -> None: ...
    def EnablePeriodic(self) -> None: ...
    def DisablePeriodic(self) -> None: ...
    def IsPeriodicEnabled(self) -> bool: ...
    def GetPeriodicStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetPeriodicStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetPeriodicStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetPeriodicStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
