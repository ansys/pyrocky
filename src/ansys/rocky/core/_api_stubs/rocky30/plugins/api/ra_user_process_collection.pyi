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
from coilib50.process import Process as Process
from kraken20.plugins.api.ka_element_item import KAElementItem as KAElementItem
from rocky30.models.rocky_model_type import MatchModelType as MatchModelType
from rocky30.models.rocky_model_type import RockyModelTypeEnum as RockyModelTypeEnum
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CUBE_GROUP_FACTORY_COMMAND_ID as CUBE_GROUP_FACTORY_COMMAND_ID,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CYLINDER_GROUP_FACTORY_COMMAND_ID as CYLINDER_GROUP_FACTORY_COMMAND_ID,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RACubeGroup as RACubeGroup,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RACylinderGroup as RACylinderGroup,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RAPolyhedronProcess as RAPolyhedronProcess,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RASurfaceUserProcess as RASurfaceUserProcess,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_streamlines_user_process import (
    RAStreamlinesUserProcess as RAStreamlinesUserProcess,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAUserProcessCollection(ApiElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetProcessNames(self): ...
    def GetProcess(self, process_name): ...
    def CreatePlaneProcess(
        self,
        parent,
        name: Incomplete | None = ...,
        origin: Incomplete | None = ...,
        normal: Incomplete | None = ...,
        plane_type: Incomplete | None = ...,
        plane_mode: Incomplete | None = ...,
    ): ...
    def CreateInspectorProcess(self, parent, name: Incomplete | None = ...): ...
    def GetPlaneProcessNames(self): ...
    def GetInspectorProcessNames(self): ...
    def CreateCylinderGroupProcess(
        self,
        parent_processes,
        name: Incomplete | None = ...,
        center: Incomplete | None = ...,
        size: Incomplete | None = ...,
        rotation: Incomplete | None = ...,
        internal_factor: Incomplete | None = ...,
        initial_angle: Incomplete | None = ...,
        final_angle: Incomplete | None = ...,
    ) -> RACylinderGroup: ...
    def CreateCubeGroupProcess(
        self,
        parent_processes,
        name: Incomplete | None = ...,
        center: Incomplete | None = ...,
        magnitude: Incomplete | None = ...,
        rotation: Incomplete | None = ...,
    ) -> RACubeGroup: ...
    def CreateCubeProcess(
        self,
        parent,
        name: Incomplete | None = ...,
        center: Incomplete | None = ...,
        magnitude: Incomplete | None = ...,
        rotation: Incomplete | None = ...,
        parent_pool_id: Incomplete | None = ...,
    ): ...
    def GetCubeProcessNames(self): ...
    def GetTrajectoryProcessNames(self): ...
    def CreateCylinderProcess(
        self,
        parent,
        name: Incomplete | None = ...,
        center: Incomplete | None = ...,
        size: Incomplete | None = ...,
        rotation: Incomplete | None = ...,
        internal_factor: Incomplete | None = ...,
        initial_angle: Incomplete | None = ...,
        final_angle: Incomplete | None = ...,
    ): ...
    def CreateParticleTimeSelectionProcess(
        self,
        parent,
        range_definition: str = ...,
        initial: int = ...,
        final: int = ...,
        unit: str = ...,
    ): ...
    def CreateTrajectoryProcess(
        self,
        parent,
        starting_timestep: Incomplete | None = ...,
        number_timesteps: Incomplete | None = ...,
        particle_stride: Incomplete | None = ...,
    ): ...
    def GetCylinderProcessNames(self): ...
    def GetParticleTimeSelectionProcessNames(self): ...
    def CreateEulerianStatistics(
        self, parent, name: Incomplete | None = ..., divisions: Incomplete | None = ...
    ): ...
    def GetEulerianStatisticsNames(self): ...
    def CreateFilterProcess(self, parent, name: Incomplete | None = ...): ...
    def CreatePropertyProcess(self, parent, name: Incomplete | None = ...): ...
    def GetFilterProcessNames(self): ...
    def GetPropertyProcessNames(self): ...
    def CreatePolyhedronProcess(
        self,
        parent: ApiElementItem,
        stl_filename: str,
        name: Union[str, None] = ...,
        import_scale: float = ...,
        convert_yz: bool = ...,
    ) -> Union[RAPolyhedronProcess, None]: ...
    def GetPolyhedronProcessNames(self): ...
    def CreateSurfaceUserProcess(
        self,
        parent: ApiElementItem,
        stl_filename: str,
        name: Union[str, None] = ...,
        import_scale: float = ...,
        convert_yz: bool = ...,
    ) -> Union[RASurfaceUserProcess, None]: ...
    def GetSurfaceUserProcessNames(self) -> list[str]: ...
    def CreateParticleToContactProcess(self, parent, name: Incomplete | None = ...): ...
    def CreateContactToParticleProcess(self, parent, name: Incomplete | None = ...): ...
    def GetParticleToContactProcessNames(self): ...
    def GetContactToParticleProcessNames(self): ...
    def CreateStreamlinesUserProcess(
        self, parent: ApiElementItem, name: Union[str, None] = ...
    ) -> Union[RAStreamlinesUserProcess, None]: ...
    def GetStreamlinesUserProcessNames(self) -> list[str]: ...
