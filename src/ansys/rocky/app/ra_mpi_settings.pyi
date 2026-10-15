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

from rocky30.models.solver.general_settings import MpiSettings as MpiSettings

from ansys.rocky.app.api_element_item import ApiElementItem

class RAMpiSettings(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for the MPI Execution Settings.

    Access it from the :class:`RASimulatorRun` with:

    .. code-block:: python

        simulator_run = study.GetSimulatorRun()
        mpi_settings = simulator_run.GetMpiSettings()
        mpi_settings.GetNumberOfProcessors()
    """

    @classmethod
    def GetWrappedClass(cls) -> type["MpiSettings"]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetExtraParams(self) -> str:
        """
        Get the value of "Extra Params".

        """

    def SetExtraParams(self, value: str) -> None:
        """
        Set the value of "Extra Params".

        :param value:
            The value to set.
        """

    def GetHeterogeneous(self) -> bool:
        """
        Get the value of "Heterogeneous".

        """

    def SetHeterogeneous(self, value: bool) -> None:
        """
        Set the value of "Heterogeneous".

        :param value:
            The value to set.
        """

    def EnableHeterogeneous(self) -> None:
        """
        Set the value of "Heterogeneous" to True.
        """

    def DisableHeterogeneous(self) -> None:
        """
        Set the value of "Heterogeneous" to False.
        """

    def IsHeterogeneousEnabled(self) -> bool:
        """
        Check if the "Heterogeneous" is enabled.

        """

    def GetHostfile(self) -> str:
        """
        Get the value of "Hostfile".

        """

    def SetHostfile(self, value: str) -> None:
        """
        Set the value of "Hostfile".

        :param value:
            The value to set.
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

    def GetNumberOfThreadsPerProcess(self) -> int:
        """
        Get the value of "Number of Threads Per Process".

        """

    def SetNumberOfThreadsPerProcess(self, value: str | int) -> None:
        """
        Set the value of "Number of Threads Per Process".

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

    def GetSlicingDirection(self) -> str:
        """
        Get "Slicing Direction" as a string.

        :return:
            The returned value will be one of [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        """

    def SetSlicingDirection(self, value: str) -> None:
        """
        Set the value of "Slicing Direction".

        :param value:
            The value to set. Must be one of [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
        :raises RockyApiError:
            If `value` is not a valid "Slicing Direction" option.
        """

    def GetValidSlicingDirectionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Slicing Direction".

        :return:
            The returned list is [\'X_Parallel\', \'Y_Parallel\', \'Z_Parallel\'].
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
