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
from coilib50.subject import Subject as Subject
from coilib50.time.time_step_interface import ITimeStep as ITimeStep
from rocky30.models.particle.particle import Particle as Particle
from rocky30.models.particle.particle_tesselation import (
    GetParticleSizeDistribution as GetParticleSizeDistribution,
)
from rocky30.models.rocky_process_queries import (
    QUERY_ROCKY_BOUNDARY_TRANSFORMER as QUERY_ROCKY_BOUNDARY_TRANSFORMER,
)
from rocky30.process.triangle_helper import (
    GetTrianglesFromGeometry as GetTrianglesFromGeometry,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import (
    RABaseGeometry as RABaseGeometry,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_study import RAStudy as RAStudy
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_wall import RAWall as RAWall

ExportValuesTuple = tuple[float, ...]

class RAExportToolkit:
    ra_study: Incomplete
    def __init__(self, ra_study: RAStudy) -> None: ...
    def ExportFEMForces(
        self,
        csv_filename: str,
        entities_to_export: Union[ApiElementItem, str, list],
        timestep_to_export: Union[ITimeStep, str, int, None] = ...,
        apply_transformation: bool = ...,
    ) -> None: ...
    def ExportGeometryLoads(
        self,
        csv_filename: str,
        entities_to_export: Union[ApiElementItem, str, list],
        timestep_to_export: Union[ITimeStep, str, int, None] = ...,
        apply_transformation: bool = ...,
        export_forces: bool = ...,
    ) -> None: ...
    def ExportGeometryLoadsMultiTime(
        self,
        csv_filename: str,
        entities_to_export: Union[ApiElementItem, str, list],
        timesteps_to_export: list[Union[ITimeStep, int]],
        apply_transformation: bool = ...,
        export_forces: bool = ...,
        show_progress: bool = ...,
    ) -> None: ...
    def ExportParticleToStl(
        self,
        stl_filename: str,
        particle: Union[str, Particle, ApiElementItem],
        time_to_export: Union[ITimeStep, int, None] = ...,
        output_unit: Union[str, None] = ...,
        target_size: Union[float, None] = ...,
        target_unit: Union[str, None] = ...,
    ) -> None: ...
    def ExportToSTL(
        self,
        stl_filename: str,
        entities: Union[Subject, ApiElementItem, str, list],
        time_to_export: Union[ITimeStep, int, None] = ...,
        output_unit: Union[str, None] = ...,
    ) -> None: ...
    def ExportHTC(
        self,
        csv_filename: str,
        entities_to_export: Union[ApiElementItem, str, list],
        timestep_to_export: Union[ITimeStep, str, int, None],
        apply_transformation: bool,
        ref_temperature: Union[float, None],
    ) -> None: ...
