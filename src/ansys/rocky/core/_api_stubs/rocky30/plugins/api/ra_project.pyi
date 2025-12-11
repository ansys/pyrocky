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

from coilib50.time.time_step import TimeStep
from petroapp10.plugins.entities.petroapp10_project import Petroapp10Project
from rocky30.models.study.study import Study as Study

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_expose import ApiExpose
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

RATimeOrIndex = TimeStep | int

class RAProject(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a project.

    The :class:`RAProject` class serves as the main access point for a project's :class:`RAStudy`
    and the project entities that aren't directly related to a simulation's configuration, such as
    the time filter, the collection of user processes, etc.

    The :class:`RAProject` can be obtained directly via the `app` global object. Example usage:

    .. code-block:: python

        project = app.CreateProject()
        study = project.GetStudy()
        user_processes = project.GetUserProcessCollection()
        input_variables = project.GetInputVariables()

        project.SaveProject('my_project.rocky')
        project.SaveProjectForRestart('my_restart_project.rocky', timestep_or_index=10)
    """

    def __init__(self) -> None: ...
    @ApiExpose
    def CloseProject(self, check_save_state: bool = True) -> None:
        """
        Close the current project.

        :param check_save_state:
            If False, it will close without asking the user to save it first.
        """

    @ApiExpose
    def SaveProject(self, filename: str | None = None) -> None:
        """
        Save the currently opened project.

        :param filename:
            The name of the file to save the project or None if to update the current file
        """

    @ApiExpose
    def SaveProjectForRestart(
        self, filename: str, timestep_or_index: RATimeOrIndex | None = None
    ) -> None:
        """
        Create a new restart project from the current project.

        :param filename:
            The new filename to be saved.
        :param timestep_or_index:
            Either the index of the timestep, or the timestep itself, in which to create the restart
            project. If None is passed, the application's current timestep will be used.
        """

    @ApiExpose
    def GetProjectFilename(self) -> str:
        """
        Get the current project's filename.

        :return:
            The current project's file name, or None if there is no current project or if the
            project hasn't been saved yet.
        """

    @ApiExpose
    def HasUnsavedChanges(self) -> bool:
        """
        Check if the current project has unsaved changes.

        :return:
            True if the project is modified (unsaved changes), False otherwise.
        """

    @classmethod
    def GetWrappedClass(self) -> type["Petroapp10Project"]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def CreateStudy(self, study_name: str | None = None) -> RAStudy:
        """
        Creates a new study and returns its wrapper

        :param study_name:
            The name of the study
        """

    @ApiExpose
    def GetStudyNames(self) -> list[str]: ...
    @ApiExpose
    def GetStudy(self, study_name: str | None = None) -> RAStudy | None:
        """
        Get the project's Study.

        :param study_name:
            The name of the study
            If None is given the first model will be returned
        """

    @classmethod
    @ApiExpose
    def GetModelStudy(cls, model_item):
        """
        Get the study model associated with a given model item

        :param Subject model_item:
            A study child

        @return RAStudy or None if no study was found for the given element
        """

    def GetModelElement(self, model_element_id):
        """
        Get the model element associated with the given ID

        :param unicode model_element_id:
            The element id

        @return
            The wrapped object with the given ID
        """

    def GetUserProcessCollection(self) -> RAUserProcessCollection | None:
        """
        Get the project's collection of User Processes.
        """

    def GetUserProcess(self, process_name): ...
    def GetTimeFilter(self) -> RATimeFilter | None:
        """
        Utility function to return the api object representing the project's time filter
        """

    def GetParametricVariables(self) -> RAParametricVariables:
        """
        Get the PrePost Scripting wrapper for the project's Parametric Variables.
        """

    def GetInputVariables(self) -> RAInputVariables:
        """
        Get the PrePost Scripting wrapper for the project's Input Variables.
        """

    def RemoveProcess(self, process: RAGridProcessElementItem | str) -> None:
        """
        Removes the given process from the project.

        :param process:
            a process or process name
        """

    @ApiExpose
    def GetElementNames(self, type_name=None): ...
    @ApiExpose
    def GetElement(
        self, element_name=None, type_name=None, raise_if_no_found: bool = True
    ): ...
