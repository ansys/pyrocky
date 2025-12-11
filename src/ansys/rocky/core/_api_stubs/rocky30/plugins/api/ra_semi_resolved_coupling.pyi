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

from rocky30coupling.fluent.io.fluent_cas_description import (
    FluentCaseConfig as FluentCaseConfig,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)

class RAFluentSemiResolvedCoupling(ApiElementItem):
    """
    PrePost Scripting wrapper class for the Fluent Two-Way Semi Resolved coupling mode
    """

    @classmethod
    def GetWrappedClass(self) -> type: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def SetPartIdIfValid(self) -> None:
        """
        Set the process' part id (unused for now)
        """

    def SetupDatFilename(self, dat_filename: str) -> bool: ...
    def SetupStoreFiles(
        self, cas_filename: str, case_config: FluentCaseConfig | None = None
    ) -> None:
        """
        Copies CAS file to Rocky's project folder and update Fluent info
        """

    def GetFluentReleases(self) -> list[str]:
        """
        Get a list of available Fluent releases.

        :rtype: list(unicode)
        :return: The list of available Fluent releases
        """

    def GetFluentVersion(self) -> str:
        """
        Get the value of "Version".

        :rtype: str
        """

    def SetFluentVersion(self, fluent_version: str) -> str:
        """
        Set the Ansys Fluent version to be used in CFD coupling (deprecated).

        Currently, it's not possible to change the version of Ansys Fluent used for CFD coupling.
        This method is being kept for backward compatibility (and also because there's a chance
        of this feature to be brought back in future version).
        """

    def GetCouplingFilesKept(self) -> int:
        """
        Get the value of "Coupling Files Kept".

        """

    def SetCouplingFilesKept(self, value: str | int) -> None:
        """
        Set the value of "Coupling Files Kept".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetFluentAdditionalArgs(self) -> str:
        """
        Get the value of "Fluent Additional Args".

        """

    def SetFluentAdditionalArgs(self, value: str) -> None:
        """
        Set the value of "Fluent Additional Args".

        :param value:
            The value to set.
        """

    def GetFluentExecutionMode(self) -> str:
        """
        Get "Fluent Execution Mode" as a string.

        :return:
            The returned value will be one of [\'serial\', \'local_parallel\', \'distributed_parallel\'].
        """

    def SetFluentExecutionMode(self, value: str) -> None:
        """
        Set the value of "Fluent Execution Mode".

        :param value:
            The value to set. Must be one of [\'serial\', \'local_parallel\', \'distributed_parallel\'].
        :raises RockyApiError:
            If `value` is not a valid "Fluent Execution Mode" option.
        """

    def GetValidFluentExecutionModeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Fluent Execution Mode".

        :return:
            The returned list is [\'serial\', \'local_parallel\', \'distributed_parallel\'].
        """

    def GetFluentOutputFrequencyMultiplier(self) -> int:
        """
        Get the value of "Fluent Output Frequency Multiplier".

        """

    def SetFluentOutputFrequencyMultiplier(self, value: str | int) -> None:
        """
        Set the value of "Fluent Output Frequency Multiplier".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetFluentSolverProcesses(self) -> int:
        """
        Get the value of "Fluent Solver Processes".

        """

    def SetFluentSolverProcesses(self, value: str | int) -> None:
        """
        Set the value of "Fluent Solver Processes".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetUseDatInitialization(self) -> bool:
        """
        Get the value of "Use Dat Initialization".

        """

    def SetUseDatInitialization(self, value: bool) -> None:
        """
        Set the value of "Use Dat Initialization".

        :param value:
            The value to set.
        """
