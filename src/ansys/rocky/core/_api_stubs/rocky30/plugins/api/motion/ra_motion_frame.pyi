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

from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_orientation_mixin import (
    _RAOrientationMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_base_motion import (
    RABaseMotionFrame as RABaseMotionFrame,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion import (
    RAMotion as RAMotion,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion_list import (
    RAMotionList as RAMotionList,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToFixedArray as ConvertUserPassedValueToFixedArray,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToScalar as ConvertUserPassedValueToScalar,
)

class RAMotionFrame(RABaseMotionFrame, RAGridProcessElementItem, _RAOrientationMixin):
    def __init__(self, id, model_id=None) -> None: ...
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def AddFreeBodyTranslationMotion(
        self, motion_direction: str = "none"
    ) -> RAMotion: ...
    def AddFreeBodyRotationMotion(self, motion_direction: str = "none") -> RAMotion: ...
    def AddPendulumMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        initial_frequency=(0.0, "Hz"),
        angular_initial_amplitude=(0.0, "rad"),
        direction=((0.0, 0.0, 0.0), "m"),
        angular_initial_phase=(0.0, "rad"),
        frequency_variation=(0.0, "Hz/s"),
        angular_amplitude_variation=(0.0, "rad/s"),
    ): ...
    def AddVibrationMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        initial_frequency=(0.0, "Hz"),
        initial_amplitude=(0.0, "m"),
        direction=((0.0, 0.0, 0.0), "m"),
        frequency_variation=(0.0, "Hz/s"),
        amplitude_variation=(0.0, "m/s"),
    ): ...
    def AddRotationMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        angular_velocity=((0.0, 0.0, 0.0), "rad/s"),
        angular_acceleration=((0.0, 0.0, 0.0), "rad/s2"),
    ): ...
    def AddTranslationMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        velocity=((0.0, 0.0, 0.0), "m/s"),
        acceleration=((0.0, 0.0, 0.0), "m/s2"),
        define_as: str = "fixed_velocity",
        final_velocity=((0.0, 0.0, 0.0), "m/s"),
    ): ...
    def ApplyTo(self, obj) -> None: ...
    def GetMotions(self) -> RAMotionList: ...
    def GetFbmMaxAngularLimits(self, unit: str | None = None) -> list[float]: ...
    def SetFbmMaxAngularLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None: ...
    def GetFbmMaxLinearLimits(self, unit: str | None = None) -> list[float]: ...
    def SetFbmMaxLinearLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None: ...
    def GetFbmMinAngularLimits(self, unit: str | None = None) -> list[float]: ...
    def SetFbmMinAngularLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None: ...
    def GetFbmMinLinearLimits(self, unit: str | None = None) -> list[float]: ...
    def SetFbmMinLinearLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None: ...
    def GetEnableFbmAngularLimits(self) -> bool: ...
    def SetEnableFbmAngularLimits(self, value: bool) -> None: ...
    def GetEnableFbmLinearLimits(self) -> bool: ...
    def SetEnableFbmLinearLimits(self, value: bool) -> None: ...
    def GetEnablePeriodicMotion(self) -> bool: ...
    def SetEnablePeriodicMotion(self, value: bool) -> None: ...
    def GetKeepInPlace(self) -> int: ...
    def SetKeepInPlace(self, value: str | int) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetPeriodicMotionPeriod(self, unit: str | None = None) -> float: ...
    def SetPeriodicMotionPeriod(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
    def GetPeriodicMotionStartTime(self, unit: str | None = None) -> float: ...
    def SetPeriodicMotionStartTime(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
    def GetPeriodicMotionStopTime(self, unit: str | None = None) -> float: ...
    def SetPeriodicMotionStopTime(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
    def GetRelativePosition(self, unit: str | None = None) -> list[float]: ...
    def SetRelativePosition(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None: ...
