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

from pathlib import Path
from typing import Union

from kraken20.plugins.api.ka_application import KAApplication
from sci20.app.base_process import BaseProcess as BaseProcess

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem as ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_additional_features import (
    RAAdditionalFeatures as RAAdditionalFeatures,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_matplotlib_window import (
    RAMplWindow as RAMplWindow,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_matplotlib_window import (
    UserWindowSubjectContainer as UserWindowSubjectContainer,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import (
    RAProject as RAProject,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_study import RAStudy as RAStudy

class RockyApiApplication(KAApplication):
    def CreateProject(self) -> RAProject: ...
    def GetProject(self) -> RAProject: ...
    def OpenProject(self, filename: str) -> RAProject: ...
    def CloseProject(self, check_save_state: bool = ...) -> None: ...
    def SaveProject(self, filename: Union[str, None] = ...) -> None: ...
    def PlaybackMacroFile(self, filename: str) -> None: ...
    def PlaybackMacro(self, macro_name: str) -> None: ...
    def GetAdditionalFeatures(self) -> RAAdditionalFeatures: ...
    def GetVersion(self) -> str: ...
    def GetStudy(self, study_name: Union[str, None] = ...) -> RAStudy: ...
