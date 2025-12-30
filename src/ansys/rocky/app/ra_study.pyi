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

from collections.abc import Sequence

from _typeshed import Incomplete
from barril.units import Scalar
from coilib50.process import IProcess as IProcess
from coilib50.status.status_interface import IStatusMessage
from coilib50.subject import Subject as Subject
from coilib50.time.time_set import TimeSet as TimeSet
from coilib50.time.time_step import TimeStep
from petroapp10.plugins.entities.input_reader.input_reader_model import (
    InputReader as InputReader,
)
from rocky20.simulator import RestartData as RestartData
from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.geometry.custom_geometry import CustomGeometry as CustomGeometry
from rocky30.models.naming import CreateNewName as CreateNewName
from rocky30.models.restart.simulation_restart_subject import (
    SimulationRestartSubject as SimulationRestartSubject,
)
from rocky30.models.study.study import Study as Study
from rocky30.models.workbench.workbench_data_subject import WorkbenchData as WorkbenchData
from rocky30.plugins.prop_change.prop_change_service import (
    RockyPropChangeValidator as RockyPropChangeValidator,
)
from rocky30.process.geometry.custom_boundary_process import (
    CustomBoundaryProcessSubject as CustomBoundaryProcessSubject,
)
from rocky30.process.particle.particle_mesh_process import (
    ParticleMeshProcess as ParticleMeshProcess,
)
from sci20.plugins.api.api_curve import SciApiCurve as SciApiCurve

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.api_expose import ApiExpose
from ansys.rocky.app.conveyors.ra_feed_conveyor import RAFeedConveyor as RAFeedConveyor
from ansys.rocky.app.conveyors.ra_receiving_conveyor import (
    RAReceivingConveyor as RAReceivingConveyor,
)
from ansys.rocky.app.motion.ra_motion_frame import RAMotionFrame as RAMotionFrame
from ansys.rocky.app.motion.ra_motion_frame_source import (
    RAMotionFrameSource as RAMotionFrameSource,
)
from ansys.rocky.app.ra_addins import RAModuleCollection as RAModuleCollection
from ansys.rocky.app.ra_airflow import RAAirFlow as RAAirFlow
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry
from ansys.rocky.app.ra_calculations import RACalculations as RACalculations
from ansys.rocky.app.ra_cfd_coupling import RACFDCoupling as RACFDCoupling
from ansys.rocky.app.ra_circular_surface import RACircularSurface as RACircularSurface
from ansys.rocky.app.ra_contact_data import RAContactData as RAContactData
from ansys.rocky.app.ra_domain_settings import RADomainSettings as RADomainSettings
from ansys.rocky.app.ra_export_toolkit import RAExportToolkit as RAExportToolkit
from ansys.rocky.app.ra_fluid_inlet import RAFluidInlet as RAFluidInlet
from ansys.rocky.app.ra_fluid_material import RAFluidMaterial as RAFluidMaterial
from ansys.rocky.app.ra_geometry_collection import (
    RAGeometryCollection as RAGeometryCollection,
)
from ansys.rocky.app.ra_inlet import RAInletGeometry as RAInletGeometry
from ansys.rocky.app.ra_inlets_outlets_collection import (
    RAInletsOutletsCollection as RAInletsOutletsCollection,
)
from ansys.rocky.app.ra_materials_collection import (
    RAMaterialCollection as RAMaterialCollection,
)
from ansys.rocky.app.ra_materials_interaction_collection import (
    RAMaterialsInteractionCollection as RAMaterialsInteractionCollection,
)
from ansys.rocky.app.ra_outlet import RAOutlet as RAOutlet
from ansys.rocky.app.ra_particle import RAParticle as RAParticle
from ansys.rocky.app.ra_particle_collection import (
    RAParticleCollection as RAParticleCollection,
)
from ansys.rocky.app.ra_particle_inlet import RAParticleInlet as RAParticleInlet
from ansys.rocky.app.ra_particle_joints_data import (
    RAParticleJointsData as RAParticleJointsData,
)
from ansys.rocky.app.ra_particles_process import RAParticles as RAParticles
from ansys.rocky.app.ra_physics import RAPhysics as RAPhysics
from ansys.rocky.app.ra_point_cloud_collection import (
    RAPointCloudCollection as RAPointCloudCollection,
)
from ansys.rocky.app.ra_rectangular_surface import (
    RARectangularSurface as RARectangularSurface,
)
from ansys.rocky.app.ra_regions_of_interest_collection import (
    RARegionsOfInterestCollection as RARegionsOfInterestCollection,
)
from ansys.rocky.app.ra_simulator_run import RASimulatorRun as RASimulatorRun
from ansys.rocky.app.ra_solid_material import RASolidMaterial as RASolidMaterial
from ansys.rocky.app.ra_sph_eulerian_solution import (
    RASPHEulerianSolution as RASPHEulerianSolution,
)
from ansys.rocky.app.ra_sph_settings import RASPHSettings as RASPHSettings
from ansys.rocky.app.ra_surface import RASurface as RASurface
from ansys.rocky.app.ra_system_coupling_wall import (
    RASystemCouplingWall as RASystemCouplingWall,
)
from ansys.rocky.app.ra_volumetric_inlet import RAVolumetricInlet as RAVolumetricInlet
from ansys.rocky.app.ra_wall import RAWall as RAWall
from ansys.rocky.app.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

RAMaterialOrName = RASolidMaterial | str
Status = dict[str, Sequence[tuple[IStatusMessage, str]]]
Particle = RAParticle | list[RAParticle] | None
ParticleInletExtensions = list[tuple[str, float | Scalar]]
PeriodicMotionExtensions = list[tuple[str, float | Scalar]]

class RAStudy(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a project's Study.

    This wrapper is the main access point for all other entities typically present in a Rocky
    project. Access the :class:`RAStudy` via the :class:`RAProject` once a project has been created
    or opened (:ref:`more <more>`):

    .. code-block:: python

        project = app.GetProject()
        study = project.GetStudy()

    .. _more:

    The :class:`RAStudy` class acts as a main hub of functionality, providing methods to perform
    various common actions related to simulations:

    - Helper creation methods for simulation entities such as :meth:`CreateParticle()`,
      :meth:`CreateFeedConveyor()`, :meth:`ImportWall()`, etc.
    - Accessor methods for specialized PrePost Scripting wrapper objects such as :meth:`GetMaterialCollection()`,
      :meth:`GetPhysics()`, :meth:`GetSimulatorRun()`, etc.
    - Methods related to the simulation and its results, such as :meth:`StartSimulation()`,
      :meth:`StopSimulation()`, :meth:`DeleteResults()`, etc.
    """

    @classmethod
    def GetWrappedClass(self) -> type[Study]: ...
    @ApiExpose
    def GetCustomerName(self) -> str:
        """
        Get the study customer name.
        """

    @ApiExpose
    def SetCustomerName(self, customer_name: str) -> None:
        """
        Change the study customer's name

        :param customer_name:
            The customer name to be set
        """
    customer_name: Incomplete
    @ApiExpose
    def GetDescription(self) -> str:
        """
        Get the study description.
        """

    @ApiExpose
    def SetDescription(self, description: str) -> None:
        """
        Change the study description

        :param description:
            The customer name to be set
        """
    description: Incomplete
    def GetElementNames(self, type_name: str | None = None) -> list[str]: ...
    def GetElement(
        self,
        element_name: str | None = None,
        type_name: str | None = None,
        raise_if_no_found: bool = True,
    ) -> ApiElementItem: ...
    def GetSubjectElement(self, subject: Subject | str) -> ApiElementItem: ...
    def GetExportToolkit(self) -> RAExportToolkit:
        """
        Get a RAExportToolkit object related to this RAStudy. The returned object can be used
        for export operations.
        """

    @classmethod
    def GetClassName(self) -> str: ...
    def GetPhysics(self) -> RAPhysics:
        """
        Get the study's Physics object.
        """

    def GetMotionFrameSource(self) -> RAMotionFrameSource | None:
        """
        Get the study's Motion Frame Source.

        :return:
            The motion frame source, used to deal with motion.
        """

    def GetDomainSettings(self) -> RADomainSettings:
        """
        Get the study's Domain Settings.
        """

    def GetSphSettings(self) -> RASPHSettings: ...
    def GetSphEulerianSolution(self) -> RASPHEulerianSolution: ...
    def GetGeometryCollection(self) -> RAGeometryCollection:
        """
        Get the study's Geometry Collection.
        """

    def GetGeometry(self, geometry_name: str) -> RAWall | None:
        """
        Get the geometry with the given name

        :return: The geometry with the given name
        """

    def CreateParticle(self) -> RAParticle:
        """
        Create a particle in the study with default values.
        """

    def CreateParticleInlet(
        self,
        entry_point: RAFeedConveyor | RAInletGeometry | RASurface,
        particle: RAParticle,
    ) -> RAParticleInlet:
        """
        Create a particle inlet with the given entry_point and particle.

        :param entry_point:
            The input's entry point - either a FeedConveyor or an Inlet.
        :param particle:
            The particle that will enter through this input.
        """

    def CreateOutlet(self, exit_point: RABaseGeometry) -> RAOutlet:
        """
        Create an outlet with the given exit point.

        :param exit_point:
            The outlet's exit point surface.
        """

    def CreateVolumetricInlet(
        self,
        particle: RAParticle | None = None,
        name: str | None = None,
        mass: float = 100.0,
        seed_coordinates: Tuple3F | None = None,
        geometries: list[str | RAWall] | None = None,
        use_geometries_to_compute: bool = False,
        box_center: Tuple3F | None = None,
        box_dimensions: Tuple3F | None = None,
        use_box_center_as_seed_point: bool = False,
    ) -> RAVolumetricInlet:
        """
        Creates a volumetric inlet with the given properties.

        :param name:
            The name which will be used for the volume fill.
        :param seed_coordinates:
            A point (x, y, z) in meters that will be the reference to start the filling process.
        :param geometries:
            A list of names or RAWall selected in RAVolumetricInlet. The names or RAWall list must match the
            existent geometries.
        :param use_geometries_to_compute:
            If true: the limits of the filling process will be the selected boundaries.
            If false: a cube must be defined to be the limits of the filling process.
        :param box_center:
            A point (x, y, z) that will be the center of the limit cube.
        :param dimensions:
            The dimensions (length, width, height) of the limit cube.
        :param box_dimensions:
            The dimensions (lenght, width, height) of the limit cube.
        :param use_box_center_as_seed_point:
            If true, the seed point will be set to the box center.
        """

    def CreateRectangularSurface(self) -> RARectangularSurface: ...
    def CreateCircularSurface(self) -> RACircularSurface: ...
    def CreateFeedConveyor(self) -> RAFeedConveyor:
        """
        Creates a new feed conveyor and add it to the project.
        """

    def CreateReceivingConveyor(self) -> RAReceivingConveyor:
        """
        Creates a new receiving conveyor and add it to the project.
        """

    def ImportWall(
        self,
        custom_filename: str,
        import_scale: float = 1.0,
        convert_yz: bool = False,
        custom_name_prefix: str | None = None,
    ) -> list[RAWall]:
        """
        Import a geometry file and create one or more corresponding geometries in the study.

        :param custom_filename:
            The filename of the STL, DXF or XGL file to import.

        :param import_scale:
            The import scale to be applied to the imported geometry.

        :param convert_yz:
            Whether the y and z axes of the imported geometry should be converted.
        """

    def ImportSystemCouplingWall(
        self,
        custom_filename: str,
        import_scale: float = 1.0,
        convert_yz: bool = False,
        custom_name_prefix: str | None = None,
    ) -> list[RASystemCouplingWall]:
        """
        Import a geometry file and create one or more corresponding geometries in the study.

        :param custom_filename:
            The filename of the STL, DXF or XGL file to import.

        :param import_scale:
            The import scale to be applied to the imported geometry.

        :param convert_yz:
            Whether the y and z axes of the imported geometry should be converted.
        """

    def ImportSurface(
        self,
        custom_filename: str,
        import_scale: float = 1.0,
        convert_yz: bool = False,
        custom_name_prefix: str | None = None,
    ) -> list[RASurface]:
        """
        Import a custom surface file and create one or more corresponding geometries in the study.

        :param custom_filename:
            The filename of the STL, DXF or XGL file to import.

        :param import_scale:
            The import scale to be applied to the imported geometry.

        :param convert_yz:
            Whether the y and z axes of the imported geometry should be converted.
        """

    def ConvertToWall(
        self, geometries: list[RASurface | RASystemCouplingWall]
    ) -> list[RAWall]: ...
    def ConvertToSystemCouplingWall(
        self, geometries: list[RAWall]
    ) -> list[RASystemCouplingWall]: ...
    def ConvertToSurface(self, geometries: list[RAWall]) -> list[RASurface]: ...
    def GetWallFromFilename(self, filename: str) -> list[ApiElementItem]:
        """
        Given a filename finds all imported geometries created from it.

        :param filename:
            The name of the file that originally created a set of geometries
        """

    def GetSurfaceFromFilename(self, filename: str) -> list[ApiElementItem]:
        """
        Given a filename finds all imported geometries created from it.

        :param filename:
            The name of the file that originally created a set of geometries
        """

    def ReplaceWallTriangles(
        self, new_filename: str, import_scale: float = 1.0, convert_yz: bool = False
    ) -> None:
        """
        Replace the existing triangles of a geometry with new triangles.

        It is assumed that there is a geometry corresponding to new_filename, previously
        imported. This method is used to update the triangles of the geometry, without
        creating new model entities.

        This method only supports geometry files that contain a single object. This is true for
        all STL files, but XGL and DXF files generally support multiple objects per file - this
        method will raise a RuntimeError in this case.

        :param new_filename:
            The filename of the STL, DXF or XGL file with new triangle data.

        :param import_scale:
            The import scale to be applied to the imported geometry.

        :param convert_yz:
            Whether the y and z axes of the imported geometry should be converted.
        """

    def RemoveWall(self, filename: str) -> None:
        """
        Remove walls associated with the given filename.

        :param filename:
            The name of the filename associated with the current project walls
        """

    def RemoveSurface(self, filename: str) -> None:
        """
        Remove custom surfaces associated with the given filename.

        :param filename:
            The name of the filename associated with the current project custom surfaces
        """

    def GetRegionsOfInterestCollection(self) -> RARegionsOfInterestCollection: ...
    def GetMaterialCollection(self) -> RAMaterialCollection:
        """
        Get the study's Material Collection.
        """

    def GetParticleCollection(self) -> RAParticleCollection:
        """
        Get the study's Particle Collection.
        """

    def GetPointCloudCollection(self) -> RAPointCloudCollection:
        """
        Get the study's Point Cloud Collection.
        """

    def GetMaterialsInteractionCollection(self) -> RAMaterialsInteractionCollection:
        """
        Deprecated: Use :meth:`RAMaterialCollection.GetMaterialsInteractionCollection()` instead.
        """

    def GetInletsOutletsCollection(self) -> RAInletsOutletsCollection:
        """
        Get the study's Inlets and Outlets Collection.
        """

    def GetCalculations(self) -> RACalculations:
        """
        Get the project's Calculations.
        """

    def GetParticleInput(self, input_name: str) -> RAParticleInlet:
        """
        Get the particle input with the given name.
        """

    def GetSourceForMeshProcesses(self) -> IProcess:
        """
        :return:
            Get the process in the associated study that should be used as source for mesh processes
        """

    def GetInputReader(self) -> InputReader:
        """
        Get the study's input reader.
        :return:
            The input reader associated with the study.
        """

    def GetSolutionId(self) -> str:
        """
        :returns:
            The id identifying the source of the solution
        """

    def GetCFDCoupling(self) -> RACFDCoupling:
        """
        Get the current CFD coupling object.

        :return:
            The CFDCoupling object
        """

    def GetAirFlow(self) -> RAAirFlow | None:
        """
        Get the RAAirFlow object (if applicable).

        :return:
            The AirFlow object is configured as the CFD coupling mode
            None otherwise
        """

    def GetContactData(self) -> RAContactData:
        """
        Get the RAContactData object.

        :return:
            The contact data object.
        """

    def GetJointsData(self) -> RAParticleJointsData:
        """
        Get the RAParticleJointsData object.

        :return:
            The joint statisctics data object.
        """

    def GetUnusedPartId(self) -> int:
        """
        :returns:
            A valid part id to associate with a new process
        """

    def UpdateTimeSet(self) -> None:
        """
        Request an update in the the time steps available in the study.
        """

    def GetParticleMeshProcess(self) -> ParticleMeshProcess:
        """
        Get the process that generated the particle mesh.

        :return:
            The particle mesh process associated with the current this study

        :raise AssertionError if no process was found associated with this study.
        """

    def GetParticles(self) -> RAParticles:
        """
        Get the process that contains the simulated particles.

        :return:
            The particles process
        """

    def SetRestartSubject(self, restart_subject: SimulationRestartSubject) -> None:
        """
        Set the restart subject

        :param restart_subject:
            The subject with study restart information
        """

    def GetRestartSubject(self) -> SimulationRestartSubject:
        """
        :return:
            The subject with study restart information
        """

    def GetSimulatorRun(self) -> RASimulatorRun:
        """
        Get the PrePost Scripting wrapper for simulation-related parameters.
        """

    def GetSolver(self) -> RASimulatorRun:
        """
        Synonym for :meth:`GetSimulatorRun()`.
        """

    def CreateSolidMaterialAndRelatedInteractions(
        self, material_name: str | None = None
    ) -> RASolidMaterial: ...
    def RemoveSolidMaterialAndRelatedInteractions(
        self, material_or_name: RAMaterialOrName
    ) -> None: ...
    def CreateFluidMaterial(
        self, material_name: str | None = None
    ) -> RAFluidMaterial: ...
    def RemoveFluidMaterial(self, material_or_name: str | RAFluidMaterial) -> None: ...
    @ApiExpose
    def GetElementCurve(
        self,
        element_name: str,
        curve_name: str,
        simulation_name: str | None = None,
        realization: str | None = None,
    ) -> SciApiCurve:
        """
        Get the curve matching a given element name and curve name.

        :param element_name: unicode
            The name of the element

        :param curve_name: unicode
            The name of the curve

        :param simulation_name: unicode
            An optional parameter for defining the simulation to get the curve from.

        :param realization: unicode
            An additional keyword to identify the curve realization

        :rtype: Curve
        :return:
            The curves for the given element and name.
        """

    def ClearPartIds(self) -> None:
        """
        Re-set the process part ids to None
        """

    def ResetSimulationStatus(self) -> None:
        """
        In addition to clearing the part ids, removes the possibility of "resuming" the simulation
        next.
        """

    def SetupRestartPartIds(self) -> None:
        """
        Re-set the particle and geometry processes to the default configuration when the source
        of the processes is a restart data.

        In a restart there is only particle information, so the process is set to the default id
        and all the other are set to None.
        """

    def CreateRestartSubject(
        self, timestep_index: int, restart_filename: str
    ) -> RestartData:
        """
        Creates, configure and set the restart subject to the current study.
        The given time-step index defines the time to which the restart information will be create from.

        :param timestep_index:
            The time-step index to create the restart information

        :param restart_filename:
            the filename to be set so the restart subject could write and read the data from

        :raise RestartValidationFailedException:
            If it cannot create a restart subject.
        """

    @ApiExpose
    def IsSimulating(self) -> bool:
        """
        Whether we're currently simulating something.
        """

    @ApiExpose
    def GetProgress(self) -> float | None:
        """
        Get the current simulation progress [0.00, 100.00] or None if no simulation is running.
        """

    @ApiExpose
    def HasResults(self) -> bool:
        """
        Whether we have results from a previous simulation.
        """

    @ApiExpose
    def CanResumeSimulation(self) -> bool:
        """
        Whether the simulation can be resumed.
        """

    @ApiExpose
    def DeleteResults(self):
        """
        Called to delete any results we currently have from a simulation.
        """

    @ApiExpose
    def RefreshResults(self):
        """
        Called to refresh the results we currently have from a simulation.
        """

    @ApiExpose
    def StartSimulation(
        self,
        skip_summary: bool | None = False,
        delete_results: bool | None = False,
        non_blocking: bool = False,
    ) -> bool:
        """
        Start the simulation. If possible, will resume a previously interrupted simulation.
        If you wish to start a simulation from scratch, delete previous results via
        DeleteResults() first.

        :param bool skip_summary:
            If starting from scratch, whether the simulation summary will be skipped (False) or
            presented to the user (True).

        :param bool delete_results:
            True if the simulation results should be deleted, False otherwise.
            If there are no simulation results, this flag is ignored

        :param bool non_blocking:
            If True, start the simulation asynchronously. Only works in headless mode (raises an error if otherwise).

        :return bool
            Returns True if the simulation has started successfully, False otherwise.
        """

    @ApiExpose
    def StopSimulation(self) -> None:
        """
        Stops a currently running simulation. If there's no simulation running, does nothing.
        """

    @ApiExpose
    def ExtendSimulation(
        self,
        extension_amount: float | Scalar = 0,
        time: int | TimeStep | None = None,
        inlet_extensions: ParticleInletExtensions | None = None,
        periodic_motion_extensions: PeriodicMotionExtensions | None = None,
    ) -> None:
        """
        Extend the simulation: either its duration, the duration of an inlet in the study or the
        duration of a periodic motion frame.

        :param extension_amount: The number of seconds to extend the simulation by.
        :param time: The optional time at which to extend the simulation.
        :param inlet_extensions: The list of input extensions.
            The first parameter of each pair must be the name of the continuous injection to extend,
            and the second is the number of seconds to extend the input by.
        :param periodic_motion_extensions: the list of periodic motions extensions.
            The first parameter of each pair must be the name of the periodic motion to extend,
            and the second is the number of seconds to extend the periodic motion by.
        """

    @ApiExpose
    def GetTimeSet(self) -> TimeSet:
        """
        Get the study's timeset.

        - Before simulation, the timeset will contain the timesteps used in motion preview.
        - After simulation, the timeset will contain the actual simulation timesteps.
        """

    def SetVariable(self, name: str, value: float) -> None:
        """
        Sets the values the given parametric variable

        :param name:
            The name of the variable

        :param value:
            The value to be set
        """
    STATUS_ERROR: str
    STATUS_WARNING: str
    STATUS_INFO: str
    STATUS_UNKNOWN: str
    @classmethod
    def GetStatus(cls, include_opengl_messages: bool = False) -> Status:
        """
        Check the current Study status

        :param include_opengl_messages:
            Whether messages related to OpenGL should be included in the status.
        :return:
            Returns a list of subject names and the existing status as a list of tuples with the
            message type and description
        """

    def SetWorkbenchData(self, workbench_data: WorkbenchData) -> None:
        """
        Set the workbench data subject

        :param workbench_data:
            The subject with study workbench information
        """

    def GetWorkbenchData(self) -> WorkbenchData:
        """
        :return:
            The subject with study workbench information
        """

    def GetFEMForcesAnalysisModules(
        self, module_collection: RAModuleCollection
    ) -> dict[str, str]:
        """
        Get the name and the FEM Forces property for all available Boundary Collision Statistics
        modules

        :param RAModuleCollection module_collection:
            The study's Module Collection

        :return Dict[str, str]:
            A Dict with the Module Name and the FEM Forces property name
        """

    def SetCollectForcesForFemAnalysis(self, value: bool) -> None:
        """
        Enable the Boundary Collision Statistics modules and enable/disable
        the FEM Forces analysis

        :param bool value: Wheter to enable or disable the modules
        """

    def GetCollectForcesForFemAnalysis(self) -> bool:
        """
        Checks wheter the Collision Statistics modules are colecting FEM Forces for analysis

        :return bool:
            True if the Collect FEM Forces property of any Collision Statistics module is enabled
        """

    def HasCalculatedHTC(self) -> bool:
        """
        Checks whether HTC is being calculated.

        :return bool:
            True if HTC is being calculated.
        """

    def GetModuleCollection(self) -> RAModuleCollection:
        """
        Get the study's Module Collection.
        """

    def SetIntraParticleCollisionStatistics(self, value: bool) -> None:
        """
        Enable/disable the Intra Particle Collision Statistics Module.

        Note: This shortcut method enables/disables _all_ properties related to that Module.

        :param value:
        """

    def SetHTCCalculatorEnabled(self, value: bool) -> None:
        """
        Enable/disable the SPH HTC Calculator module.
        """

    def GetIntraParticleCollisionStatistics(self) -> bool:
        """
        Get whether the Intra Particle Collision Statistics Module is enabled.
        """

    def SetMeshedParticlesUpscalingEnabled(self, value: bool) -> None: ...
    def GetMeshedParticlesUpscalingEnabled(self) -> bool:
        """
        Get the Meshed Particles Upscaling value.
        """
