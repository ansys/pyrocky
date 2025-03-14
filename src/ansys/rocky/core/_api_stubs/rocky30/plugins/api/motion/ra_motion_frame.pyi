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

from _typeshed import Incomplete

from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_orientation_mixin import (
    _RAOrientationMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_base_motion import (
    RABaseMotionFrame as RABaseMotionFrame,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion_list import (
    RAMotionList as RAMotionList,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToFixedArray as ConvertUserPassedValueToFixedArray,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToScalar as ConvertUserPassedValueToScalar,
)

class RAMotionFrame(RABaseMotionFrame, RAGridProcessElementItem, _RAOrientationMixin):
    def __init__(self, id, model_id: Incomplete | None = ...) -> None: ...
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def AddPendulumMotion(
        self,
        start_time=...,
        stop_time=...,
        initial_frequency=...,
        angular_initial_amplitude=...,
        direction=...,
        angular_initial_phase=...,
        frequency_variation=...,
        angular_amplitude_variation=...,
    ): ...
    def AddVibrationMotion(
        self,
        start_time=...,
        stop_time=...,
        initial_frequency=...,
        initial_amplitude=...,
        direction=...,
        frequency_variation=...,
        amplitude_variation=...,
    ): ...
    def AddRotationMotion(
        self,
        start_time=...,
        stop_time=...,
        angular_velocity=...,
        angular_acceleration=...,
    ): ...
    def AddTranslationMotion(
        self,
        start_time=...,
        stop_time=...,
        velocity=...,
        acceleration=...,
        define_as: str = ...,
        final_velocity=...,
    ): ...
    def ApplyTo(self, obj) -> None: ...
    def GetMotions(self) -> RAMotionList: ...
    def GetRotationAngle(self, unit: Union[str, None] = ...) -> float: ...
    def SetRotationAngle(
        self, value: Union[str, float], unit: Union[str, None] = ...
    ) -> None: ...
    def GetRelativeRotationVector(self, unit: Union[str, None] = ...) -> list[float]: ...
    def SetRelativeRotationVector(
        self, values: Sequence[Union[str, float]], unit: Union[str, None] = ...
    ) -> None: ...
    def GetFbmMaxAngularLimits(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetFbmMaxAngularLimits(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetFbmMaxLinearLimits(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetFbmMaxLinearLimits(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetFbmMinAngularLimits(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetFbmMinAngularLimits(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetFbmMinLinearLimits(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetFbmMinLinearLimits(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetEnableFbmAngularLimits(self) -> bool: ...
    def SetEnableFbmAngularLimits(self, value: bool) -> None: ...
    def GetEnableFbmLinearLimits(self) -> bool: ...
    def SetEnableFbmLinearLimits(self, value: bool) -> None: ...
    def GetEnablePeriodicMotion(self) -> bool: ...
    def SetEnablePeriodicMotion(self, value: bool) -> None: ...
    def GetKeepInPlace(self) -> int: ...
    def SetKeepInPlace(self, value: Union[str, int]) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetPeriodicMotionPeriod(self, unit: Optional[str] = ...) -> float: ...
    def SetPeriodicMotionPeriod(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetPeriodicMotionStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetPeriodicMotionStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetPeriodicMotionStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetPeriodicMotionStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetRelativePosition(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetRelativePosition(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
