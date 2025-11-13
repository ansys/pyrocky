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
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_subject_element import (
    BaseSubjectApiElement as BaseSubjectApiElement,
)

class RATimeStatisticsCalculator(BaseSubjectApiElement):
    def GetStartTime(self): ...
    def SetStartTime(self, time_value) -> None: ...
    def GetStopTime(self): ...
    def SetStopTime(self, time_value) -> None: ...
    def GetGridFunctionName(self): ...

class RATimeStatistics(ApiElementItem):
    def __init__(self, id, ra_process, model_id=None) -> None: ...
    def AddGridFunction(
        self, start_time, stop_time, operation, grid_function_name, location=None
    ): ...
    def RemoveGridFunction(self, name_or_calculator) -> None: ...
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    @classmethod
    def CreateFor(self, ra_process): ...
