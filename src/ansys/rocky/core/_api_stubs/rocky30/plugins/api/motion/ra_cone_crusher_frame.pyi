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

from collections.abc import Sequence
from typing import List, Optional, Union

from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_base_motion import (
    RABaseMotionFrame as RABaseMotionFrame,
)

class RAConeCrusherFrame(RABaseMotionFrame):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetInitialOrientation(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetInitialOrientation(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetPivotPoint(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetPivotPoint(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetRotationAxis(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetRotationAxis(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetRotationalVelocity(self, unit: Optional[str] = ...) -> float: ...
    def SetRotationalVelocity(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
