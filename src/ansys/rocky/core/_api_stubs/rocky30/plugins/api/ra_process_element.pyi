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
from typing import List, Optional, Union

from _typeshed import Incomplete
from coilib50.process.base_process_subject import (
    AbstractProcessSubject as AbstractProcessSubject,
)
from coilib50.time.time_step_interface import ITimeStep as ITimeStep
from coilib50.units import Scalar as Scalar
from kraken20.plugins.api.ka_element_item import KAElementItem
from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.core.geometry.rocky_document_constants import (
    UNIT_PLANE_ANGLE as UNIT_PLANE_ANGLE,
)
from rocky30.plugins.sph.surface_user_process.surface_user_process_subject import (
    SurfaceUserProcessSubject as SurfaceUserProcessSubject,
)
from rocky30.plugins.user_process.group.cube_process_group import (
    CubeProcessGroup as CubeProcessGroup,
)
from rocky30.plugins.user_process.group.cylinder_process_group import (
    CylinderProcessGroup as CylinderProcessGroup,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CUBE_GROUP_CHILD_PROCESS_COMMAND_ID as CUBE_GROUP_CHILD_PROCESS_COMMAND_ID,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CYLINDER_GROUP_CHILD_PROCESS_COMMAND_ID as CYLINDER_GROUP_CHILD_PROCESS_COMMAND_ID,
)
from rocky30.process.user_process.cube_process_with_movement import (
    CubeProcessWithMovement as CubeProcessWithMovement,
)
from rocky30.process.user_process.cylinder_process_with_movement import (
    CylinderProcessWithMovement as CylinderProcessWithMovement,
)
from rocky30.process.user_process.polyhedron_process_with_movement import (
    PolyhedronProcessWithMovement as PolyhedronProcessWithMovement,
)
from sci20.app.mesh_assembly.cube.abstract_cube import BaseCube as BaseCube
from sci20.app.mesh_assembly.cylinder.mesh_assembly_cylinder import (
    BaseCylinder as BaseCylinder,
)
from sci20.plugins.api.api_process_element import SciApiProcessElementItem
from sci20.plugins.process.plane_process.plane_process_subject import PlaneProcessSubject

from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_orientation_mixin import (
    _RAOrientationMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion._with_movement_mixin import (
    _WithMovementMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAProcessElementItem(SciApiProcessElementItem):
    def GetCurve(
        self,
        curve_name,
        simulation_name: Incomplete | None = ...,
        realization: Incomplete | None = ...,
        time_step: Incomplete | None = ...,
    ): ...

class RAUserProcess(RAGridProcessElementItem):
    def GetNumberOfParticles(self, time_step): ...
    def IterParticles(self, time_step): ...

class _RAAbstractCubeMixin:
    def GetSubject(self) -> BaseCube: ...
    def GetCenter(self, unit: Incomplete | None = ...): ...
    def SetCenter(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F: ...
    def GetSize(self, unit: Union[str, None] = ...) -> Tuple3F: ...
    def SetSize(self, x: float, y: float, z: float, unit: Union[str, None] = ...): ...
    def GetRotation(self, unit: Incomplete | None = ...): ...
    def SetRotation(self, x, y, z, unit: Incomplete | None = ...): ...

class RACubeGroup(
    KAElementItem, _WithMovementMixin, _RAOrientationMixin, _RAAbstractCubeMixin
):
    @classmethod
    def GetWrappedClass(cls) -> type[CubeProcessGroup]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def AddProcess(self, source_process: AbstractProcessSubject) -> None: ...

class _RAAbstractCylinderMixin:
    def GetSubject(self) -> BaseCylinder: ...
    def GetCenter(self, unit: Incomplete | None = ...): ...
    def SetCenter(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F: ...
    def GetSize(self, unit: Union[str, None] = ...) -> Tuple3F: ...
    def SetSize(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetRotation(self, unit: Incomplete | None = ...): ...
    def SetRotation(self, x, y, z, unit: Incomplete | None = ...): ...
    def GetInternalFactor(self, unit: Incomplete | None = ...): ...
    def SetInternalFactor(
        self, internal_factor, unit: Incomplete | None = ...
    ) -> None: ...
    def GetInitialAngle(self, unit: Incomplete | None = ...): ...
    def SetInitialAngle(self, initial_angle, unit: Incomplete | None = ...) -> None: ...
    def GetFinalAngle(self, unit: Incomplete | None = ...): ...
    def SetFinalAngle(self, final_angle, unit: Incomplete | None = ...) -> None: ...

class RACylinderGroup(
    KAElementItem, _WithMovementMixin, _RAOrientationMixin, _RAAbstractCylinderMixin
):
    @classmethod
    def GetWrappedClass(cls) -> type[CylinderProcessGroup]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def AddProcess(self, source_process: AbstractProcessSubject) -> None: ...

class RACubeProcess(
    RAUserProcess, _WithMovementMixin, _RAOrientationMixin, _RAAbstractCubeMixin
):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetCubeCenter(self, unit: Incomplete | None = ...): ...
    def SetCubeCenter(self, x, y, z, unit: Incomplete | None = ...): ...
    def GetCubeMagnitude(self, unit: Incomplete | None = ...): ...
    def SetCubeMagnitude(self, x, y, z, unit: Incomplete | None = ...): ...
    def GetCubeRotation(self, unit: Incomplete | None = ...): ...
    def SetCubeRotation(self, x, y, z, unit: Incomplete | None = ...): ...

class RACylinderProcess(
    RAUserProcess, _WithMovementMixin, _RAOrientationMixin, _RAAbstractCylinderMixin
):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...

class RAFilterProcess(RAUserProcess):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetType(self): ...
    def SetType(self, filter_type) -> None: ...
    def GetMode(self): ...
    def SetMode(self, property_mode) -> None: ...
    def GetMinValue(self, unit: Incomplete | None = ...): ...
    def SetMinValue(self, value, unit: Incomplete | None = ...) -> None: ...
    def GetMaxValue(self, unit: Incomplete | None = ...): ...
    def SetMaxValue(self, value, unit: Incomplete | None = ...) -> None: ...
    def GetCutValue(self, unit: Incomplete | None = ...): ...
    def SetCutValue(self, value, unit: Incomplete | None = ...) -> None: ...
    def SetPropertyGridFunction(
        self, grid_function, realization: Incomplete | None = ...
    ) -> None: ...
    def GetPropertyGridFunction(self): ...

class RAPlaneProcess(RAUserProcess, _RAOrientationMixin):
    @classmethod
    def GetWrappedClass(self) -> type[PlaneProcessSubject]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetType(self) -> str: ...
    def SetType(self, plane_type: str) -> None: ...
    def GetMode(self) -> str: ...
    def SetMode(self, plane_mode: str) -> None: ...
    def GetOrigin(self) -> Tuple3F: ...
    def GetPlaneOrigin(self) -> Tuple3F: ...
    def SetOrigin(self, x: float, y: float, z: float) -> None: ...
    def SetPlaneOrigin(self, x: float, y: float, z: float) -> None: ...
    def GetNormal(self) -> Tuple3F: ...
    def GetPlaneNormal(self) -> Tuple3F: ...
    def SetNormal(self, x: float, y: float, z: float) -> None: ...
    def SetPlaneNormal(self, x: float, y: float, z: float) -> None: ...

class RATrajectoryProcess(RAUserProcess):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetStartingTimeStep(self, time_step) -> None: ...
    def SetStartingTime(self, time: Union[str, ITimeStep, int]) -> None: ...
    def GetStartingTimeStep(self): ...
    def GetStartingTime(self) -> ITimeStep: ...
    def SetNumberOfTimeSteps(self, number_of_intervals) -> None: ...
    def SetNumberOfIntervals(self, number_of_intervals: int): ...
    def GetNumberOfTimeSteps(self): ...
    def GetNumberOfIntervals(self) -> int: ...
    def SetParticleStride(self, particle_stride) -> None: ...
    def GetParticleStride(self): ...
    def UpdateParticlesSelection(self) -> None: ...

class RAInspectorProcess(RAUserProcess):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetCellId(self, cell_id) -> None: ...

class RAPolyhedronProcess(RAUserProcess, _WithMovementMixin, _RAOrientationMixin):
    @classmethod
    def GetWrappedClass(cls) -> type[PolyhedronProcessWithMovement]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetCenter(self, unit: Incomplete | None = ...) -> Tuple3F: ...
    def SetCenter(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F: ...
    def GetSize(self, unit: Union[str, None] = ...) -> Tuple3F: ...
    def SetSize(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetRotation(self, unit: Union[str, None] = ...) -> Tuple3F: ...
    def SetRotation(self, x: float, y: float, z: float, unit: Union[str, None] = ...): ...
    def SetSTL(self, filename: str, mesh_unit: Union[str, None] = ...) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetScale(self, unit: Union[str, None] = ...) -> list[float]: ...
    def SetScale(
        self, values: Sequence[Union[str, float]], unit: Union[str, None] = ...
    ) -> None: ...

class RASurfaceUserProcess(RAUserProcess, _WithMovementMixin, _RAOrientationMixin):
    @classmethod
    def GetWrappedClass(cls) -> type["SurfaceUserProcessSubject"]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def SetSTL(self, filename: str, mesh_unit: Union[str, None] = ...) -> None: ...
    def GetRotation(self, unit: Union[str, None] = ...) -> Tuple3F: ...
    def SetRotation(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetSize(self, unit: Union[str, None] = ...) -> list[float]: ...
    def SetSize(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetCenter(self, unit: Union[str, None] = ...) -> Tuple3F: ...
    def SetCenter(
        self, x: float, y: float, z: float, unit: Union[str, None] = ...
    ) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetScale(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetScale(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
