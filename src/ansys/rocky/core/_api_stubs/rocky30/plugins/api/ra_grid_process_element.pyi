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

from _typeshed import Incomplete
from barril.units import Scalar
from ben10.element_function.semantic_association import (
    SemanticAssociation as SemanticAssociation,
)
from ben10.element_function.semantic_association_crossed_curve import (
    SemanticAssociationCrossedCurve as SemanticAssociationCrossedCurve,
)
from coilib50.time.time_step_interface import ITimeStep as ITimeStep
from kraken20.plugins.api.ka_grid import KAGrid
from rocky30.plugins.curve_calculation.grid_function.pre_calculated_grid_function_calculators import (
    Rocky30PreCalculatedGridFunctionCalculation as Rocky30PreCalculatedGridFunctionCalculation,
)
from sci20.core.geometry import IGeometry as IGeometry

from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_subject_with_coloring_mixin import (
    _RASubjectWithColoringMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_custom_calculators import (
    RACustomCurveAndGridProperty as RACustomCurveAndGridProperty,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_time_statistics import (
    RATimeStatistics as RATimeStatistics,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_wall import RAWall as RAWall

class RAGridProcessElementItem(
    KAGrid, _RASubjectWithColoringMixin, RACustomCurveAndGridProperty
):
    """
    Rocky API process model.
    """

    def GetGridFunction(
        self, grid_function_name, simulation_name=None, translated: bool = False
    ): ...
    def GetGridFunctionNames(
        self, translated: bool = False, context: str | None = None
    ) -> list[str]:
        """
        Overridden to filter out deprecated property names.
        """

    def GetGeometry(self, time_step: str | int | ITimeStep = "current") -> IGeometry: ...
    def GetTimeStatistics(self) -> RATimeStatistics:
        """
        Get the object responsible for handling time-statistics grid functions for this process.
        This call will return None if the process doesn't support time statistics.
        """
    VALID_OPERATIONS: Incomplete
    VALID_TIME_RANGE_DEFINITIONS: Incomplete
    VALID_DOMAIN_RANGE: Incomplete
    def CreateTransientCurveOutputVariable(
        self,
        curve_name: str,
        operation: str = "max",
        time_operation: str = "max",
        time_range: str = "last_output",
        initial_time_range: float = 0.0,
        final_time_range: float = 0.0,
        domain_range: str = "all",
        initial_domain_range: float = 0.0,
        final_domain_range: float = 0.0,
        domain_unit: str | None = None,
    ):
        """
        Used to create an output variable based on a curve for which there's a completely new
        representation for each time step -- such as Power : Impact X Belt Width
        (i.e.: will get the curve multiple times based on the time range, compute a value for each
        time based on the operation, to convert the multiple curves into a single curve and then
        will apply the time_operation to get a single scalar from those values).

        :param curve_name:
            The name of the transient curve for which the output variable is wanted.

        :param operation:
            The operation we want to do at the curve in each time (i.e.: go from transient curve
            to a regular curve).

            Valid operations:
                'min'
                'max'
                'sum'
                'sum_squared'
                'average'
                'variance'
                'standard_deviation'

        :param time_operation:
            The operation that we want to do at the curve when the curve is already converted to
            a regular time-based curve (by applying the 'operation' at each time).

            Valid operations:
                'min'
                'max'
                'sum'
                'sum_squared'
                'average'
                'variance'
                'standard_deviation'

        :param time_range:
            Defines the time range for the curve to be gathered for creating the output
            variable (depending on which time range is chosen, the initial_time_range and the
            final_time_range may be used to get the actual times for computing the statistics).

            Valid time ranges:
                'app_time_filter':
                    Uses the application time filter to get the relevant times.

                'all'
                    Uses all the times in the simulation.

                'last_output'
                    Uses only the last time in the simulation.

                'absolute'
                    Defines a time range using the initial_time_range and final_time_range.

                'single'
                    Defines a single time to be used as the time range specified as the
                    initial_time_range.

                'absolute_only_start'
                    Defines a time range using all the values after the given initial_time_range.

                'relative_to_end'
                    Uses all the values considering initial_time_range as a delta from the end of
                    the simulation.

        :param initial_time_range:
            A value in seconds (whose actual meaning depends on the defined time_range).

        :param final_time_range:
            A value in seconds (whose actual meaning depends on the defined time_range).

        :param domain_range:
            Define the domain range for the curve to create the output variable

            Valid domain_range:
                'all'
                    Uses all the domain in the simulation

                'single'
                    Defines a single time to be used as the time range specified as the initial_domain_range

                'absolute'
                    Defines a domain range using the initial_domain_range and final_domain_range.

        :param initial_domain_range:
            A value for the beginning of the domain (whose actual meaning depends on the defined domain_range).

        :param final_domain_range:
            A value for the end of the domain (whose actual meaning depends on the defined domain_range).

        :param domain_unit:
            A unit for the domain_range

        :rtype: str
        :return:
            Returns the name of the variable to be used later on to reference the output variable.
        """

    def CreateCurveOutputVariable(
        self,
        curve_name: str,
        operation: str = "max",
        time_range: str = "all",
        initial_time_range: float = 0.0,
        final_time_range: float = 0.0,
    ):
        """
        Used to create an output variable based on a curve which doesn't change at each new timestep
        (i.e.: a curve with a single value for each time).

        :see: CreateTransientCurveOutputVariable for dealing with curves that are transient.

        :param curve_name:
            The name of the curve for which the output variable is wanted.

        :param operation:
            The operation we want to do to convert the curve into a single value.

            Valid operations:
                'min'
                'max'
                'sum'
                'sum_squared'
                'average'
                'variance'
                'standard_deviation'

        :param time_range:
            Defines the time range for the curve to be gathered for creating the output
            variable (depending on which time range is chosen, the initial_time_range and the
            final_time_range may be used to get the actual times for computing the statistics).

            Valid time ranges:
                'app_time_filter':
                    Uses the application time filter to get the relevant times.

                'all'
                    Uses all the times in the simulation.

                'last_output'
                    Uses only the last time in the simulation.

                'absolute'
                    Defines a time range using the initial_time_range and final_time_range.

                'single'
                    Defines a single time to be used as the time range specified as the
                    initial_time_range.

                'absolute_only_start'
                    Defines a time range using all the values after the given initial_time_range.

                'relative_to_end'
                    Uses all the values considering initial_time_range as a delta from the end of
                    the simulation.

        :param initial_time_range:
            A value in seconds (whose actual meaning depends on the defined time_range).

        :param final_time_range:
            A value in seconds (whose actual meaning depends on the defined time_range).

        :rtype: str
        :return:
            Returns the name of the variable to be used later on to reference the output variable.
        """

    def CreateGridFunctionStatisticOutputVariable(
        self,
        grid_function_name: str,
        operation: str = "max",
        statistic_operation: str = "max",
        time_range: str = "last_output",
        initial_time_range: float = 0.0,
        final_time_range: float = 0.0,
    ) -> str:
        """
        Used to create an output variable based on a grid function statistic (i.e.: will get a
        grid function, compute its statistic based on statistic_operation and then based on
        the statistic values will apply the operation to get a single scalar).

        :param grid_function_name:
            The name of the grid function for which the output variable is wanted.

        :param operation:
            The operation used to select which value to get based on the statistic values obtained.

            Valid operations:
                'min'
                'max'
                'sum'
                'sum_squared'
                'average'
                'variance'
                'standard_deviation'

        :param statistic_operation:
            The statistic operation which should be applied to the grid function for each time to
            obtain a single value for each time.

            Valid operations:
                'min'
                'max'
                'sum'
                'sum_squared'
                'average'
                'variance'
                'standard_deviation'

        :param time_range:
            Defines the time range for the grid functions to be gathered for creating the output
            variable (depending on which time range is chosen, the initial_time_range and the
            final_time_range may be used to get the actual times for computing the statistics).

            Valid time ranges:
                'app_time_filter':
                    Uses the application time filter to get the relevant times.

                'all'
                    Uses all the times in the simulation.

                'last_output'
                    Uses only the last time in the simulation.

                'absolute'
                    Defines a time range using the initial_time_range and final_time_range.

                'single'
                    Defines a single time to be used as the time range specified as the
                    initial_time_range.

                'absolute_only_start'
                    Defines a time range using all the values after the given initial_time_range.

                'relative_to_end'
                    Uses all the values considering initial_time_range as a delta from the end of
                    the simulation.

        :param initial_time_range:
            A value in seconds (whose actual meaning depends on the defined time_range).

        :param final_time_range:
            A value in seconds (whose actual meaning depends on the defined time_range).

        :return:
            Returns the name of the variable to be used later on to reference the output variable.
        """

    def GetOutputVariableValue(self, variable_name: str) -> Scalar:
        """
        Get the value of a previously-created output variable.

        :param unicode variable_name:
            The variable name whose value we want.

        :return:
            Returns a scalar with the value and unit for the given variable_name or None if no
            variable was found with the given name or if it couldn't be computed.
        """

    def RemoveOutputVariable(self, variable_name: str) -> None:
        """
        Removes some output variable.

        :param variable_name:
            The name of the variable to be removed.
        """

    def RemoveProcess(self) -> None:
        """
        Removes the process from the project.
        """
