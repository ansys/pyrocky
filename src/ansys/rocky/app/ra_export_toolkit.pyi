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
from rocky30.models.motion.motion_reader_vtk_transform_query import (
    GetMotionTransformerFromPartId as GetMotionTransformerFromPartId,
)
from rocky30.models.particle.particle import Particle as Particle
from rocky30.models.particle.particle_tesselation import (
    GetParticleSizeDistribution as GetParticleSizeDistribution,
)
from rocky30.process.triangle_helper import (
    GetTrianglesFromGeometry as GetTrianglesFromGeometry,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry
from ansys.rocky.app.ra_study import RAStudy as RAStudy
from ansys.rocky.app.ra_wall import RAWall as RAWall

ExportValuesTuple = tuple[float, ...]

class RAExportToolkit:
    """
    Helper class, tied to a RAStudy, to perform export actions in Rocky.

    This toolkit can be obtained via a :class:`RAStudy`:

    .. code-block:: python

        study = app.GetStudy()
        export_toolkit = study.GetExportToolkit()
    """

    ra_study: Incomplete
    def __init__(self, ra_study: RAStudy) -> None:
        """

        :param RAStudy ra_study:
        The Study api object to which this RAExportToolkit is related. Export operations refer
        to this study.
        """

    def ExportFEMForces(
        self,
        csv_filename: str,
        entities_to_export: ApiElementItem | str | list,
        timestep_to_export: ITimeStep | str | int | None = None,
        apply_transformation: bool = True,
    ) -> None:
        """
        See :meth:`ExportGeometryLoads()`.

        File will have area and X, Y and Z forces also exported.
        """

    def ExportGeometryLoads(
        self,
        csv_filename: str,
        entities_to_export: ApiElementItem | str | list,
        timestep_to_export: ITimeStep | str | int | None = None,
        apply_transformation: bool = True,
        export_forces: bool = False,
    ) -> None:
        """
        Export the FEM forces of one or more entities to a CSV file. One CSV file may contain the
        forces of more than one entity, but only of a single timestep.

        :param csv_filename:
            The full pathname of the CSV file to generate. Previously existing files will be overwritten.

        :param entities_to_export:
            The entities to export. This parameter can be a single item, in which case it can be an
            ApiElementItem instance or the name of such an instance. The parameter can also be an
            iterable containing any mix of the two types mentioned.

        :param timestep_to_export:
            The timestep of which the FEM forces will be exported. Passing None means that the current
            active timestep will be exported instead.

        :param apply_transformation:
            True whether boundary coordinates and forces should be transformed back to boundary's
            original position, before all movements took place.

        :param export_forces:
            Flag to export force instead of pressure components.
        """

    def ExportGeometryLoadsMultiTime(
        self,
        csv_filename: str,
        entities_to_export: ApiElementItem | str | list,
        timesteps_to_export: list[ITimeStep | int],
        apply_transformation: bool = True,
        export_forces: bool = False,
        show_progress: bool = False,
    ) -> None:
        """
        Export the FEM forces of one or more entities to one or multiple CSV files. Each CSV contains the
        forces of more than one entity, but only of a single timestep.

        :param csv_filename:
            The full pathname of the CSV file to generate. Previously existing files will be overwritten.
            If timesteps_to_export has more than one timestep csv_filename will be modified to include the index
            e.g. my_csv_file.csv will write to my_csv_file_01.csv, my_csv_file_02.csv, etc

        :param entities_to_export:
            The entities to export. This parameter can be a single item, in which case it can be an
            ApiElementItem instance or the name of such an instance. The parameter can also be an
            iterable containing any mix of the two types mentioned.

        :param timesteps_to_export:
            The list of times to export. Passing None or an empty list means that the current
            active timestep will be exported instead.

        :param apply_transformation:
            True whether boundary coordinates and forces should be transformed back to boundary's
            original position, before all movements took place.

        :param export_forces:
            Flag to export force instead of pressure components.

        :param show_progress:
            Whether a progress dialog should be shown during export.
        """

    def ExportParticleToStl(
        self,
        stl_filename: str,
        particle: str | Particle | ApiElementItem,
        time_to_export: ITimeStep | int | None = None,
        output_unit: str | None = None,
        target_size: float | None = None,
        target_unit: str | None = None,
    ) -> None:
        """
        Export one and only one Particle (scaled or not) to STL file. The origin of Particle can be from a name, subject or the api element.

        :param stl_filename:
            The name of the resulting STL file. If multiple files are generated, the name of the
            entities will be appended to the filename, before the '.stl' extension.

        :param particle:
            The targets to export. The 'particle' can be the name of the Particle to export, the Subject instance, or the
            ApiElementItem instance.

        :param time_to_export:
            The timestep for which to export the items. If None is passed, the application's current
            timestep will be used.

        :param output_unit:
            The optional output unit. If None is passed, the geometry will be exported in its native
            unit (meters).

        :param target_size:
            The value of the wished scalar to scale the Particle

        :param target_unit:
            The unit of the wished scalar to scale the Particle
        """

    def ExportToSTL(
        self,
        stl_filename: str,
        entities: Subject | ApiElementItem | str | list,
        time_to_export: ITimeStep | int | None = None,
        output_unit: str | None = None,
    ) -> None:
        """
        Export one or more entities (scaled or not) to STL files. Valid entities to export are conveyors, custom
        boundaries and any user process created with one of the aforementioned types in its process
        hierarchy.

        :param stl_filename:
            The name of the resulting STL file. If multiple files are generated, the name of the
            entities will be appended to the filename, before the '.stl' extension.

        :param entities:
            The targets to export. This can be a list of elements, or a single element. Each
            'element' can be the name of the geometry to export, the Subject instance, or the
            ApiElementItem instance.

        :param time_to_export:
            The timestep for which to export the items. If None is passed, the application's current
            timestep will be used.

        :param output_unit:
            The optional output unit. If None is passed, the geometry will be exported in its native
            unit (meters).
        """

    def ExportHTC(
        self,
        csv_filename: str,
        entities_to_export: ApiElementItem | str | list,
        timestep_to_export: ITimeStep | str | int | None,
        apply_transformation: bool,
        ref_temperature: float | None,
    ) -> None:
        """
        Export the HTC of one or more entities to a CSV file. One CSV file may contain the
        HTC value of more than one entity, but only of a single timestep.

        :param csv_filename:
            The full pathname of the CSV file to generate. Previously existing files will be overwritten.

        :param entities_to_export:
            The entities to export. This parameter can be a single item, in which case it can be an
            ApiElementItem instance or the name of such an instance. The parameter can also be an
            iterable containing any mix of the two types mentioned.

        :param timestep_to_export:
            The timestep of which the HTC values will be exported. Passing None means that the current
            active timestep will be exported instead.

        :param apply_transformation:
            True whether boundary coordinates and forces should be transformed back to boundary's
            original position, before all movements took place.

        :param ref_temperature:
            The arbitrary reference temperature. If None is passed we assume that thermal is
            enabled and the adjacent temperature will be used.
        """
