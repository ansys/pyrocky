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

from kraken20.plugins.api.ka_grid_function import RAGridFunction as RAGridFunction
from rocky30.process.eulerian.eulerian_statistics_process import (
    EulerianStatisticsProcessSubject as EulerianStatisticsProcessSubject,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_expose import ApiExpose
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RAUserProcess as RAUserProcess,
)

class RAEulerianStatistics(RAUserProcess):
    @classmethod
    def GetWrappedClass(cls) -> type[EulerianStatisticsProcessSubject]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    @ApiExpose
    def GetDivisions(self) -> tuple[int, int, int]:
        """
        Get the number of divisions in i/j/k.

        :rtype: tuple(int)
        """

    @ApiExpose
    def SetDivisions(self, divisions: tuple[int, int, int]) -> None:
        """
        Set the number of divisions in i/j/k. Note that the minimum value for each number is 1.

        :param tuple(int) divisions:
            The divisions in (i,j,k) order.
        """

    @ApiExpose
    def GetParticleGridFunctionNames(self) -> list[str]:
        """
        Get a list with the particle grid function names that can be passed to `CreateGridFunction()`.

        :rtype: list(unicode)
        """

    @ApiExpose
    def GetAvailableOperations(self) -> list[str]:
        """
        Get a list with the operations that can be passed to `CreateGridFunction()`.

        :rtype: list(unicode)
        """

    @ApiExpose
    def CreateEulerianGridFunction(
        self,
        operation_name: str,
        value_name: str,
        weight_name: str | None = None,
        grid_function_source: None | RAGridProcessElementItem = None,
    ) -> RAGridFunction:
        """
        Add a new grid function to the Eulerian Statistics.

        This method takes an operation and one (or two) particle grid function names and creates
        a new grid function for this EulerianStatistics. For instance, the call:

            CreateEulerianGridFunction(\'Weighted Average\', \'Velocity : Translational : Absolute\', \'Particle Mass\')

        ... will create the `Weighted Average of Velocity : Translational : Absolute by Particle Mass`
        grid function. The grid function PrePost Scripting wrapper is returned.

        :param unicode operation_name:
            The name of the operation to be performed on the particles in each grid block. Must be
            one of `GetAvailableOperations()`.

        :param unicode value_name:
            The name of the first particle grid function to be used (the "value"). Must be one of
            `GetParticleGridFunctionNames()`.

        :param weight_name:
            The name of the second particle grid function to be used (the "weight"). Only used for
            operations that take two grid functions. Must be one of `GetParticleGridFunctionNames()`.

        :rtype: RAGridFunction
        """
