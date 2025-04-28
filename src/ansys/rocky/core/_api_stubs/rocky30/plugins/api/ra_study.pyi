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
from typing import Any

from _typeshed import Incomplete
from barril.units import Scalar
from ben10.foundation.types_ import AsList as AsList
from coilib50.process import IProcess as IProcess
from coilib50.status.status_interface import IStatusMessage
from coilib50.subject import Subject as Subject
from coilib50.time.time_set import TimeSet as TimeSet
from coilib50.time.time_step import TimeStep
from petroapp10.plugins.entities.input_reader.input_reader_model import (
    InputReader as InputReader,
)
from plugins10core.coroutines_hub.coroutines_hub_plugins import (
    GetDefaultCoroutinesHub as GetDefaultCoroutinesHub,
)
from rocky20.simulator import RestartData as RestartData
from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.geometry.custom_geometry import CustomGeometry as CustomGeometry
from rocky30.models.input.sph_inlet import SPHInlet as SPHInlet
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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.conveyors.ra_feed_conveyor import (
    RAFeedConveyor as RAFeedConveyor,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.conveyors.ra_receiving_conveyor import (
    RAReceivingConveyor as RAReceivingConveyor,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion_frame import (
    RAMotionFrame as RAMotionFrame,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion_frame_source import (
    RAMotionFrameSource as RAMotionFrameSource,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    RAModuleCollection as RAModuleCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_airflow import (
    RAAirFlow as RAAirFlow,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import (
    RABaseGeometry as RABaseGeometry,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_calculations import (
    RACalculations as RACalculations,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_cfd_coupling import (
    RACFDCoupling as RACFDCoupling,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_contact_data import (
    RAContactData as RAContactData,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_domain_settings import (
    RADomainSettings as RADomainSettings,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_export_toolkit import (
    RAExportToolkit as RAExportToolkit,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_fluid_inlet import (
    RAFluidInlet as RAFluidInlet,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_fluid_material import (
    RAFluidMaterial as RAFluidMaterial,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_geometry_collection import (
    RAGeometryCollection as RAGeometryCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_inlet import (
    RAInletGeometry as RAInletGeometry,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_inlets_outlets_collection import (
    RAInletsOutletsCollection as RAInletsOutletsCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_collection import (
    RAMaterialCollection as RAMaterialCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_interaction_collection import (
    RAMaterialsInteractionCollection as RAMaterialsInteractionCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_outlet import RAOutlet as RAOutlet
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle import (
    RAParticle as RAParticle,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle_collection import (
    RAParticleCollection as RAParticleCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle_inlet import (
    RAParticleInlet as RAParticleInlet,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle_joints_data import (
    RAParticleJointsData as RAParticleJointsData,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particles_process import (
    RAParticles as RAParticles,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_physics import (
    RAPhysics as RAPhysics,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_point_cloud_collection import (
    RAPointCloudCollection as RAPointCloudCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_regions_of_interest_collection import (
    RARegionsOfInterestCollection as RARegionsOfInterestCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_simulator_run import (
    RASimulatorRun as RASimulatorRun,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_solid_material import (
    RASolidMaterial as RASolidMaterial,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_sph_eulerian_solution import (
    RASPHEulerianSolution as RASPHEulerianSolution,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_sph_settings import (
    RASPHSettings as RASPHSettings,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_surface import (
    RASurface as RASurface,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_system_coupling_wall import (
    RASystemCouplingWall as RASystemCouplingWall,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_volumetric_inlet import (
    RAVolumetricInlet as RAVolumetricInlet,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_wall import RAWall as RAWall
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

RAMaterialOrName: Incomplete
Status = dict[str, Sequence[tuple[IStatusMessage, str]]]
Particle: Incomplete
ParticleInletExtensions: Incomplete
PeriodicMotionExtensions: Incomplete

class RAStudy(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[Study]: ...
    def GetCustomerName(self) -> str: ...
    def SetCustomerName(self, customer_name: str) -> None: ...
    customer_name: Incomplete
    def GetDescription(self) -> str: ...
    def SetDescription(self, description: str) -> None: ...
    description: Incomplete
    def GetElementNames(self, type_name: Union[str, None] = ...) -> list[str]: ...
    def GetElement(
        self,
        element_name: Union[str, None] = ...,
        type_name: Union[str, None] = ...,
        raise_if_no_found: bool = ...,
    ) -> ApiElementItem: ...
    def GetSubjectElement(self, subject: Union[Subject, str]) -> ApiElementItem: ...
    def GetExportToolkit(self) -> RAExportToolkit: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetPhysics(self) -> RAPhysics: ...
    def GetMotionFrameSource(self) -> Union[RAMotionFrameSource, None]: ...
    def GetDomainSettings(self) -> RADomainSettings: ...
    def GetSphSettings(self) -> RASPHSettings: ...
    def GetSphEulerianSolution(self) -> RASPHEulerianSolution: ...
    def GetGeometryCollection(self) -> RAGeometryCollection: ...
    def GetGeometry(self, geometry_name: str) -> Union[RAWall, None]: ...
    def CreateParticle(self) -> RAParticle: ...
    def CreateParticleInput(self, entry_point, particle) -> RAParticleInlet: ...
    def CreateContinuousInjection(
        self, entry_point: Union[RAFeedConveyor, RAInletGeometry], particle: RAParticle
    ) -> RAParticleInlet: ...
    def CreateParticleInlet(
        self,
        entry_point: Union[RAFeedConveyor, RAInletGeometry, RASurface],
        particle: RAParticle,
    ) -> RAParticleInlet: ...
    def CreateOutlet(self, exit_point: RABaseGeometry) -> RAOutlet: ...
    def CreateVolumeFill(
        self,
        particle: Union[RAParticle, None] = ...,
        name: Union[str, None] = ...,
        mass: float = ...,
        seed_coordinates: Union[Tuple3F, None] = ...,
        geometries: Union[list[Union[str, RAWall]], None] = ...,
        use_geometries_to_compute: bool = ...,
        box_center: Union[Tuple3F, None] = ...,
        box_dimensions: Union[Tuple3F, None] = ...,
    ) -> RAVolumetricInlet: ...
    def CreateVolumetricInlet(
        self,
        particle: Union[RAParticle, None] = ...,
        name: Union[str, None] = ...,
        mass: float = ...,
        seed_coordinates: Union[Tuple3F, None] = ...,
        geometries: Union[list[Union[str, RAWall]], None] = ...,
        use_geometries_to_compute: bool = ...,
        box_center: Union[Tuple3F, None] = ...,
        box_dimensions: Union[Tuple3F, None] = ...,
    ) -> RAVolumetricInlet: ...
    def CreateInlet(self) -> RAInletGeometry: ...
    def CreateRectangularSurface(self): ...
    def CreateCircularSurface(self): ...
    def CreateFeedConveyor(self) -> RAFeedConveyor: ...
    def CreateReceivingConveyor(self) -> RAReceivingConveyor: ...
    def ImportCustomGeometries(self, *args: Any, **kwargs: Any) -> Any: ...
    def ImportGeometries(
        self,
        custom_filename: str,
        import_scale: float = ...,
        convert_yz: bool = ...,
        custom_name_prefix: Union[str, None] = ...,
    ) -> list[RAWall]: ...
    def ImportWall(
        self,
        custom_filename: str,
        import_scale: float = ...,
        convert_yz: bool = ...,
        custom_name_prefix: Union[str, None] = ...,
    ) -> list[RAWall]: ...
    def ImportSystemCouplingWall(
        self,
        custom_filename: str,
        import_scale: float = ...,
        convert_yz: bool = ...,
        custom_name_prefix: Union[str, None] = ...,
    ) -> list[RASystemCouplingWall]: ...
    def ImportSurface(
        self,
        custom_filename: str,
        import_scale: float = ...,
        convert_yz: bool = ...,
        custom_name_prefix: Union[str, None] = ...,
    ) -> list[RASurface]: ...
    def ConvertToWall(
        self, geometries: list[Union[RASurface, RASystemCouplingWall]]
    ) -> list[RAWall]: ...
    def ConvertToSystemCouplingWall(
        self, geometries: list[RAWall]
    ) -> list[RASystemCouplingWall]: ...
    def ConvertToSurface(self, geometries: list[RAWall]) -> list[RASurface]: ...
    def GetCustomGeometriesFromFilename(self, *args: Any, **kwargs: Any) -> Any: ...
    def GetGeometriesFromFilename(self, new_filename: str) -> list[ApiElementItem]: ...
    def GetWallFromFilename(self, filename: str) -> list[ApiElementItem]: ...
    def GetSurfaceFromFilename(self, filename: str) -> list[ApiElementItem]: ...
    def ReplaceCustomGeometryTriangles(self, *args: Any, **kwargs: Any) -> Any: ...
    def ReplaceGeometryTriangles(
        self, new_filename: str, import_scale: float = ..., convert_yz: bool = ...
    ) -> None: ...
    def ReplaceWallTriangles(
        self, new_filename: str, import_scale: float = ..., convert_yz: bool = ...
    ) -> None: ...
    def RemoveCustomGeometries(self, *args: Any, **kwargs: Any) -> Any: ...
    def RemoveGeometries(self, filename: str) -> None: ...
    def RemoveWall(self, filename: str) -> None: ...
    def RemoveSurface(self, filename: str) -> None: ...
    def GetRegionsOfInterestCollection(self) -> RARegionsOfInterestCollection: ...
    def GetMaterialCollection(self) -> RAMaterialCollection: ...
    def GetParticleCollection(self) -> RAParticleCollection: ...
    def GetPointCloudCollection(self) -> RAPointCloudCollection: ...
    def GetMaterialsInteractionCollection(self) -> RAMaterialsInteractionCollection: ...
    def GetParticleInputCollection(self) -> RAInletsOutletsCollection: ...
    def GetInletsOutletsCollection(self) -> RAInletsOutletsCollection: ...
    def GetParticlesCalculations(self) -> RACalculations: ...
    def GetCalculations(self) -> RACalculations: ...
    def GetParticleInput(self, input_name: str) -> RAParticleInlet: ...
    def GetSourceForMeshProcesses(self) -> IProcess: ...
    def GetInputReader(self) -> InputReader: ...
    def GetSolutionId(self) -> str: ...
    def GetCFDCoupling(self) -> RACFDCoupling: ...
    def GetAirFlow(self) -> Union[RAAirFlow, None]: ...
    def GetContactData(self) -> RAContactData: ...
    def GetJointsData(self) -> RAParticleJointsData: ...
    def GetUnusedPartId(self) -> int: ...
    def UpdateTimeSet(self) -> None: ...
    def GetParticleMeshProcess(self) -> ParticleMeshProcess: ...
    def GetParticles(self) -> RAParticles: ...
    def SetRestartSubject(self, restart_subject: SimulationRestartSubject) -> None: ...
    def GetRestartSubject(self) -> SimulationRestartSubject: ...
    def GetSimulatorRun(self) -> RASimulatorRun: ...
    def GetSolver(self) -> RASimulatorRun: ...
    def CreateMaterialAndRelatedInteractions(
        self, material_name: Union[str, None] = ...
    ): ...
    def CreateSolidMaterialAndRelatedInteractions(
        self, material_name: Union[str, None] = ...
    ): ...
    def RemoveMaterialAndRelatedInteractions(
        self, material_or_name: RAMaterialOrName
    ) -> None: ...
    def RemoveSolidMaterialAndRelatedInteractions(
        self, material_or_name: RAMaterialOrName
    ) -> None: ...
    def CreateFluidMaterial(
        self, material_name: Union[str, None] = ...
    ) -> RAFluidMaterial: ...
    def RemoveFluidMaterial(
        self, material_or_name: Union[str, RAFluidMaterial]
    ) -> None: ...
    def GetElementCurve(
        self,
        element_name: str,
        curve_name: str,
        simulation_name: Union[str, None] = ...,
        realization: Union[str, None] = ...,
    ) -> SciApiCurve: ...
    def ClearPartIds(self) -> None: ...
    def ResetSimulationStatus(self) -> None: ...
    def SetupRestartPartIds(self) -> None: ...
    def CreateRestartSubject(
        self, timestep_index: int, restart_filename: str
    ) -> RestartData: ...
    def IsSimulating(self) -> bool: ...
    def GetProgress(self) -> Union[float, None]: ...
    def HasResults(self) -> bool: ...
    def CanResumeSimulation(self) -> bool: ...
    def DeleteResults(self): ...
    def RefreshResults(self): ...
    def StartSimulation(
        self,
        skip_summary: Union[bool, None] = ...,
        delete_results: Union[bool, None] = ...,
        non_blocking: bool = ...,
    ) -> bool: ...
    def StopSimulation(self): ...
    def ExtendSimulation(
        self,
        extension_amount: Union[float, Scalar] = ...,
        time: Union[int, TimeStep, None] = ...,
        inlet_extensions: Union[ParticleInletExtensions, None] = ...,
        periodic_motion_extensions: Union[PeriodicMotionExtensions, None] = ...,
    ) -> None: ...
    def GetTimeSet(self) -> TimeSet: ...
    def SetVariable(self, name: str, value: float) -> None: ...
    STATUS_ERROR: str
    STATUS_WARNING: str
    STATUS_INFO: str
    STATUS_UNKNOWN: str
    @classmethod
    def GetStatus(cls, include_opengl_messages: bool = ...) -> Status: ...
    def SetWorkbenchData(self, workbench_data: WorkbenchData) -> None: ...
    def GetWorkbenchData(self) -> WorkbenchData: ...
    def GetFEMForcesAnalysisModules(
        self, module_collection: RAModuleCollection
    ) -> dict[str, str]: ...
    def SetCollectForcesForFemAnalysis(self, value: bool) -> None: ...
    def GetCollectForcesForFemAnalysis(self) -> bool: ...
    def HasCalculatedHTC(self) -> bool: ...
    def GetModuleCollection(self) -> RAModuleCollection: ...
    def SetIntraParticleCollisionStatistics(self, value: bool) -> None: ...
    def SetHTCCalculatorEnabled(self, value: bool) -> None: ...
    def GetIntraParticleCollisionStatistics(self) -> bool: ...
    def SetMeshedParticlesUpscalingEnabled(self, value: bool) -> None: ...
    def GetMeshedParticlesUpscalingEnabled(self) -> bool: ...
