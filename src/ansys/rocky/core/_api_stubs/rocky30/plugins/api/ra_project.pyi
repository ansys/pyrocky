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

from typing import Type, Union

from _typeshed import Incomplete
from coilib50.time.time_step import TimeStep
from petroapp10.plugins.entities.petroapp10_project import Petroapp10Project
from rocky30.models.study.study import Study as Study

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_input_variables import (
    RAInputVariables as RAInputVariables,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_parametric_variables import (
    RAParametricVariables as RAParametricVariables,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_study import RAStudy as RAStudy
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_time_filter import (
    RATimeFilter as RATimeFilter,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_user_process_collection import (
    RAUserProcessCollection as RAUserProcessCollection,
)

RATimeOrIndex = Union[TimeStep, int]

class RAProject(ApiElementItem):
    def __init__(self) -> None: ...
    def CloseProject(self, check_save_state: bool = ...) -> None: ...
    def SaveProject(self, filename: Union[str, None] = ...) -> None: ...
    def SaveProjectForRestart(
        self, filename: str, timestep_or_index: Union[RATimeOrIndex, None] = ...
    ) -> None: ...
    def GetProjectFilename(self) -> str: ...
    @classmethod
    def GetWrappedClass(self) -> Type["Petroapp10Project"]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def CreateStudy(self, study_name: Union[str, None] = ...) -> RAStudy: ...
    def GetStudyNames(self) -> list[str]: ...
    def GetStudy(self, study_name: Union[str, None] = ...) -> Union[RAStudy, None]: ...
    @classmethod
    def GetModelStudy(cls, model_item): ...
    def GetModelElement(self, model_element_id): ...
    def GetUserProcessCollection(self) -> Union[RAUserProcessCollection, None]: ...
    def GetUserProcess(self, process_name): ...
    def GetTimeFilter(self) -> Union[RATimeFilter, None]: ...
    def GetParametricVariables(self) -> RAParametricVariables: ...
    def GetInputVariables(self) -> RAInputVariables: ...
    def RemoveProcess(self, process: Union[RAGridProcessElementItem, str]) -> None: ...
    def GetElementNames(self, type_name: Incomplete | None = ...): ...
    def GetElement(
        self,
        element_name: Incomplete | None = ...,
        type_name: Incomplete | None = ...,
        raise_if_no_found: bool = ...,
    ): ...
