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

from typing import Optional, Type, Union

from rocky30.plugins.particles_calculations.selection_residence_time_calculation import (
    ParticlesSelectionResidenceTimeCalculator as ParticlesSelectionResidenceTimeCalculator,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RAResidenceTime(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> Type[ParticlesSelectionResidenceTimeCalculator]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetGridFunctionName(self) -> str: ...
    def GetCalculatorName(self) -> str: ...
    def GetNameMask(self) -> str: ...
    def SetNameMask(self, value: str) -> None: ...
    def GetStopTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStopTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetStartTime(self, unit: Optional[str] = ...) -> float: ...
    def SetStartTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
