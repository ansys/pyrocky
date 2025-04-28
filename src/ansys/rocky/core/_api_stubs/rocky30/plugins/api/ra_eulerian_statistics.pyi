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

from typing import Type

from kraken20.plugins.api.ka_grid_function import KAGridFunction as KAGridFunction
from rocky30.process.eulerian.eulerian_statistics_process import (
    EulerianStatisticsProcessSubject as EulerianStatisticsProcessSubject,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RAUserProcess as RAUserProcess,
)

class RAEulerianStatistics(RAUserProcess):
    @classmethod
    def GetWrappedClass(cls) -> Type[EulerianStatisticsProcessSubject]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetDivisions(self) -> tuple[int, int, int]: ...
    def SetDivisions(self, divisions: tuple[int, int, int]) -> None: ...
    def GetParticleGridFunctionNames(self) -> list[str]: ...
    def GetAvailableOperations(self) -> list[str]: ...
    def CreateEulerianGridFunction(
        self, operation_name: str, value_name: str, weight_name: Union[str, None] = ...
    ) -> KAGridFunction: ...
