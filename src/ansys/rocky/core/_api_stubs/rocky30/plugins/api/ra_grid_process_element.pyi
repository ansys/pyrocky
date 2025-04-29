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
    def GetGridFunction(
        self,
        grid_function_name,
        simulation_name: Incomplete | None = ...,
        translated: bool = ...,
    ): ...
    def GetGeometry(self, time_step: Union[str, int, ITimeStep] = ...) -> IGeometry: ...
    def GetTimeStatistics(self) -> RATimeStatistics: ...
    VALID_OPERATIONS: Incomplete
    VALID_TIME_RANGE_DEFINITIONS: Incomplete
    VALID_DOMAIN_RANGE: Incomplete
    def CreateTransientCurveOutputVariable(
        self,
        curve_name: str,
        operation: str = ...,
        time_operation: str = ...,
        time_range: str = ...,
        initial_time_range: float = ...,
        final_time_range: float = ...,
        domain_range: str = ...,
        initial_domain_range: float = ...,
        final_domain_range: float = ...,
        domain_unit: Union[str, None] = ...,
    ): ...
    def CreateCurveOutputVariable(
        self,
        curve_name: str,
        operation: str = ...,
        time_range: str = ...,
        initial_time_range: float = ...,
        final_time_range: float = ...,
    ): ...
    def CreateGridFunctionStatisticOutputVariable(
        self,
        grid_function_name: str,
        operation: str = ...,
        statistic_operation: str = ...,
        time_range: str = ...,
        initial_time_range: float = ...,
        final_time_range: float = ...,
    ) -> str: ...
    def GetOutputVariableValue(self, variable_name: str) -> Scalar: ...
    def RemoveOutputVariable(self, variable_name: str) -> None: ...
    def RemoveProcess(self) -> None: ...
