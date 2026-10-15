# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

from rocky30.models.solver.general_settings import (
    LocalExecutionSettings as LocalExecutionSettings,
)

from ansys.rocky.app.api_element_item import ApiElementItem

class RALocalExecutionSettings(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for the Local Execution Settings.

    Access it from the :class:`RASimulatorRun` with:

    .. code-block:: python

        simulator_run = study.GetSimulatorRun()
        local_execution_settings = simulator_run.GetLocalExecutionSettings()
        local_execution_settings.GetNumberOfProcessors()
    """

    @classmethod
    def GetWrappedClass(cls) -> type["LocalExecutionSettings"]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetTargetGpus(self) -> list[int]:
        """
        :return: A list of IDs of the GPUs currently selected for Multi GPU simulation.
        """

    def SetTargetGpus(self, gpus: list[int | str]) -> None:
        """
        It will configure the IDs of GPUs that will be used in a local simulation based on the list of IDs or
        names of GPUs passed.

        :param gpus:
            List with IDs or names of GPUs to be used in simulation.
            For example in the name "1 - Geforce GTX 980", the ID is 1 and the name is "1 - Geforce GTX 980".
        """

    def GetMultiGpuSlicingDirection(self) -> str:
        """
        Get "Multi Gpu Slicing Direction" as a string.

        :return:
            The returned value will be one of [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        """

    def SetMultiGpuSlicingDirection(self, value: str) -> None:
        """
        Set the value of "Multi Gpu Slicing Direction".

        :param value:
            The value to set. Must be one of [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        :raises RockyApiError:
            If `value` is not a valid "Multi Gpu Slicing Direction" option.
        """

    def GetValidMultiGpuSlicingDirectionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Multi Gpu Slicing Direction".

        :return:
            The returned list is [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        """

    def GetNumberOfProcessors(self) -> int:
        """
        Get the value of "Number of Processors".

        """

    def SetNumberOfProcessors(self, value: str | int) -> None:
        """
        Set the value of "Number of Processors".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetProcessingUnit(self) -> str:
        """
        Get "Processing Unit" as a string.

        :return:
            The returned value will be one of [\'CPU\', \'GPU\', \'MULTI_GPU\'].
        """

    def SetProcessingUnit(self, value: str) -> None:
        """
        Set the value of "Processing Unit".

        :param value:
            The value to set. Must be one of [\'CPU\', \'GPU\', \'MULTI_GPU\'].
        :raises RockyApiError:
            If `value` is not a valid "Processing Unit" option.
        """

    def GetValidProcessingUnitValues(self) -> list[str]:
        """
        Get a list of all possible values for "Processing Unit".

        :return:
            The returned list is [\'CPU\', \'GPU\', \'MULTI_GPU\'].
        """

    def GetTargetGpu(self) -> int:
        """
        Get the value of "Target Gpu".

        """

    def SetTargetGpu(self, value: str | int) -> None:
        """
        Set the value of "Target Gpu".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """
