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

from coilib50.process import IProcess as IProcess
from coilib50.subject import Subject as Subject
from coilib50.time.time_set import TimeSet as TimeSet
from coilib50.time.time_step import TimeStep as TimeStep
from coilib50.time.time_step_interface import ITimeStep
from esss_qt10.qt_traits import QWidget as QWidget
from kraken20.plugins.api.ka_3dwindow import RA3DWindow
from kraken20.plugins.api.ka_cross_plot import KACrossPlotWindow
from kraken20.plugins.api.ka_histogram_window import KAHistogramWindow
from kraken20.plugins.api.ka_multi_time_plot_window import KAMultiTimePlotWindow
from kraken20.plugins.api.ka_space_plot import KASpacePlotWindow
from kraken20.plugins.api.ka_time_plot_window import RATimePlotWindow
from kraken20.plugins.api.ka_workspace_window import (
    KAWorkspaceWindow as KAWorkspaceWindow,
)
from sci20.app.base_process import BaseProcess as BaseProcess

from ansys.rocky.app.api_application import ApiApplication
from ansys.rocky.app.api_element_item import ApiElementItem as ApiElementItem
from ansys.rocky.app.api_expose import ApiExpose
from ansys.rocky.app.ra_additional_features import (
    RAAdditionalFeatures as RAAdditionalFeatures,
)
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_project import RAProject as RAProject
from ansys.rocky.app.ra_study import RAStudy as RAStudy
from ansys.rocky.app.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

Windows_Types = (
    RA3DWindow
    | RATimePlotWindow
    | KACrossPlotWindow
    | KAHistogramWindow
    | KASpacePlotWindow
    | KAMultiTimePlotWindow
)

class RockyApiApplication(ApiApplication):
    TYPE_3D_WINDOW: str
    TYPE_TIME_PLOT_WINDOW: str
    TYPE_CROSS_PLOT_WINDOW: str
    TYPE_HISTOGRAM_PLOT_WINDOW: str
    TYPE_SPACE_PLOT_WINDOW: str
    TYPE_MULTI_TIME_PLOT_WINDOW: str
    def CreateProject(self) -> RAProject:
        """
        Creates a new project.
        """

    def GetProject(self) -> RAProject:
        """
        Overrides Kraken API implementation to use the base class.
        If there is no project don't create a new one.
        """

    @ApiExpose
    def OpenProject(self, filename: str) -> RAProject:
        """
        Closes the current project, if any, and opens the project with the given filename.

        :param str filename:
        The complete path of the project to be opened.
        :rtype RAProject:
        """

    @ApiExpose
    def CloseProject(self, check_save_state: bool = True) -> None:
        """
        Close the current project.

        :param bool check_save_state:
            If False, it will close without asking the user to save it first.
        """

    @ApiExpose
    def SaveProject(self, filename: str | None = None) -> None:
        """
        Save the currently opened project.

        :param str filename:
            The name of the file to save the project or None if to update the current file
        """

    @ApiExpose
    def PlaybackMacroFile(self, filename: str) -> None: ...
    @ApiExpose
    def PlaybackMacro(self, macro_name: str) -> None: ...
    @ApiExpose
    def GetAdditionalFeatures(self) -> RAAdditionalFeatures:
        """
        Get the PrePost Scripting wrapper that corresponds to the "Additional Features" page on the application\'s Preferences

        :rtype: RAAdditionalFeatures
        """

    def GetVersion(self) -> str:
        """
        Return the current version of the application.
        """

    def GetStudy(self, study_name: str | None = None) -> RAStudy:
        """
        Get the project's Study.

        :param study_name:
            The name of the study
            If None is given the first model will be returned
        """
