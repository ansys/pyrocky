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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import (
    RAProject as RAProject,
)

class RAPendulum(ApiElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetAmplitudeVariation(self, unit: str | None = None) -> float: ...
    def SetAmplitudeVariation(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
    def GetInitialAmplitude(self, unit: str | None = None) -> float: ...
    def SetInitialAmplitude(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
    def GetInitialPhase(self, unit: str | None = None) -> float: ...
    def SetInitialPhase(self, value: str | float, unit: str | None = None) -> None: ...
    def GetDirection(self) -> list[float]: ...
    def SetDirection(self, values: list[str | float]) -> None: ...
    def GetFrequencyVariation(self, unit: str | None = None) -> float: ...
    def SetFrequencyVariation(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
    def GetInitialFrequency(self, unit: str | None = None) -> float: ...
    def SetInitialFrequency(
        self, value: str | float, unit: str | None = None
    ) -> None: ...
