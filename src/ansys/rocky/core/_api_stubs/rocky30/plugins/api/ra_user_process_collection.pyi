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

from coilib50.process import Process as Process
from coilib50.units.mapped_io import FixedArray as FixedArray
from kraken20.plugins.api.ka_element_item import KAElementItem as KAElementItem
from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.rocky_model_type import MatchModelType as MatchModelType
from rocky30.models.rocky_model_type import RockyModelTypeEnum as RockyModelTypeEnum
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CUBE_GROUP_FACTORY_COMMAND_ID as CUBE_GROUP_FACTORY_COMMAND_ID,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CYLINDER_GROUP_FACTORY_COMMAND_ID as CYLINDER_GROUP_FACTORY_COMMAND_ID,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    PLANE_GROUP_FACTORY_COMMAND_ID as PLANE_GROUP_FACTORY_COMMAND_ID,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_expose import ApiExpose
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
    RAPlaneGroup as RAPlaneGroup,
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
    """
    Rocky api collection of geometries.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetProcessNames(self):
        """
        Get a list with the name of the user processes.

        :rtype: list(unicode)
        """

    def GetProcess(self, process_name):
        """
        Get a user process given its name.

        :param unicode process_name:
        :rtype: ApiElementItem
        """

    def CreatePlaneProcess(
        self,
        parent,
        name=None,
        origin=None,
        normal=None,
        plane_type=None,
        plane_mode=None,
    ):
        """
        Creates a new plane process using the given parent as input.

        :param Grid|Process parent:
            The plane process parent

        :param str|None name:
            The name of the new process or None for default

        :param tuple(float, float, float) origin:
            The origin X, Y and Z coordinates in meters (m)

        :param tuple(float, float, float) normal:
            The normal X, Y and Z in meters (m)

        :rtype: RAPlaneProcess
        :return:
            A new plane process
        """

    def CreateInspectorProcess(self, parent, name=None):
        """
        Creates a new plane process using the given parent as input.

        :param Grid|Process parent:
            The plane process parent

        :param str|None name:
            The name of the new process or None for default

        :rtype: RAPlaneProcess
        :return:
            A new plane process
        """

    def GetPlaneProcessNames(self):
        """
        Get the names of created plane processes.

        :return:
            The list of plane user process names
        """

    def GetInspectorProcessNames(self):
        """
        Get the names of created inspector processes.

        :return:
            The list of inspector user process names
        """

    def CreatePlaneGroupProcess(
        self,
        parent_processes: list[RAGridProcessElementItem] | RAGridProcessElementItem,
        name: str | None = None,
        plane_origin_fixed_array: FixedArray | None = None,
        mode: str | None = None,
        type: str | None = None,
    ) -> RAPlaneGroup: ...
    def CreateCylinderGroupProcess(
        self,
        parent_processes,
        name=None,
        center: Tuple3F | None = None,
        size: Tuple3F | None = None,
        rotation: Tuple3F | None = None,
        internal_factor=None,
        initial_angle=None,
        final_angle=None,
    ) -> RACylinderGroup: ...
    def CreateCubeGroupProcess(
        self,
        parent_processes,
        name: str | None = None,
        center: Tuple3F | None = None,
        magnitude: Tuple3F | None = None,
        rotation: Tuple3F | None = None,
    ) -> RACubeGroup: ...
    def CreateCubeProcess(
        self,
        parent,
        name=None,
        center=None,
        magnitude=None,
        rotation=None,
        parent_pool_id=None,
    ):
        """
        Creates a new cube process using the given parent as input.

        :param Grid|Process parent:
            The cube process parent

        :param str|None name:
            The name of the new process or None for default

        :param tuple(float, float, float) center:
            The center X, Y and Z coordinates in meters (m)

        :param magnitude:
            The center X, Y and Z magnitude in meters (m)

        :param rotation:
            The center X, Y and Z rotation in degress (dega)

        :rtype: RACubeProcess
        :return:
            A new cube process
        """

    def GetCubeProcessNames(self):
        """
        Get the names of created cube processes.

        :return:
            The list of cube user process names
        """

    def GetTrajectoryProcessNames(self):
        """
        Get the names of created trajectory processes.

        :return:
            The list of trajectory user process names
        """

    def CreateCylinderProcess(
        self,
        parent,
        name=None,
        center=None,
        size=None,
        rotation=None,
        internal_factor=None,
        initial_angle=None,
        final_angle=None,
    ):
        """
        Creates a new cube process using the given parent as input.

        :param Grid|Process parent:
            The cube process parent

        :param str|None name:
            The name of the new process or None for default

        :param tuple(float, float, float) center:
            The center X, Y and Z coordinates in meters (m)

        :param size:
            The X, Y and Z size in meters (m)

        :param rotation:
            The center X, Y and Z rotation in degress (dega)

        :param internal_factor:
            The internal hole radius factor of the external given by the size in percentage (%)

        :param initial_angle:
            The initial angle in degress (dega)

        :param final_angle:
            The final angle in degress (dega)

        :rtype: RACylinderProcess
        :return:
            A new cylinder process
        """

    def CreateParticleTimeSelectionProcess(
        self,
        parent,
        range_definition: str = "absolute",
        initial: int = 0,
        final: int = 0,
        unit: str = "s",
    ):
        """
        Creates a new particle time selection process using the given parent as input.

        :param parent:
            Input for the particle time selection.

        :param range_definition:
            One of:
            'app_time_filter', 'all', 'last_output', 'absolute', 'single', 'absolute_only_start', 'relative_to_end'.

        :param float initial:
            The initial value for the particle time selection to consider particles. May be ignored
            depending on the range definition.

        :param float final:
            The final time for the particle time selection to consider particles. May be ignored
            depending on the range definition.

        :param unit:
            The unit for the initial/final values passed.
        """

    def CreateTrajectoryProcess(
        self, parent, starting_timestep=None, number_timesteps=None, particle_stride=None
    ):
        """
        Create a new Particle Trajectory process.

        :see: RATrajectoryProcess for a explanation of the parameters.
        :rtype: RATrajectoryProcess
        """

    def GetCylinderProcessNames(self):
        """
        Get the names of created cylinder processes.

        :return:
            The list of cylinder user process names
        """

    def GetParticleTimeSelectionProcessNames(self):
        """
        Get the names of created particle time selection processes.

        :return:
            The list of particle time selection user process names
        """

    @ApiExpose
    def CreateEulerianStatistics(self, parent, name=None, divisions=None):
        """
        Creates a new cube process using the given parent as input.

        :param Grid|Process parent:
            The process parent. Must be either a cube or a cylinder.

        :param str|None name:
            The name of the new process or None for default

        :param divisions:
            The number of divisions in i, j and k.

        :rtype: RAEulerianStatistics
        :return:
            A new Eulerian Statistics process.
        """

    @ApiExpose
    def GetEulerianStatisticsNames(self):
        """
        Get the names of created eulerian statistics processes.

        :return:
            The list of eulerian statistics user process names
        """

    def CreateFilterProcess(self, parent, name=None):
        """
        Creates a new filter process using the given parent as input.

        :param Grid|Process parent:
            The filter process parent

        :param str|None name:
            The name of the new process or None for default

        :rtype: RAFilterProcess
        :return:
            A new filter process
        """

    def CreatePropertyProcess(self, parent, name=None):
        """
        Deprecated: Use CreateFilterProcess instead.
        """

    def GetFilterProcessNames(self):
        """
        Get the names of created property processes.

        :return:
            The list of property user process names.
        """

    def GetPropertyProcessNames(self):
        """
        Deprecated: Use GetFilterProcessNames instead.
        """

    def CreatePolyhedronProcess(
        self,
        parent: ApiElementItem,
        stl_filename: str,
        name: str | None = None,
        import_scale: float = 1.0,
        convert_yz: bool = False,
    ) -> RAPolyhedronProcess | None:
        """
        Creates a new polyhedron process using the given parent as input.

        :param Grid|Process parent:
            The polyhedron process parent.

        :param str stl_filename:
            The filename with the stl to be loaded for the polyhedron.

        :param str|None name:
            The name of the new process or None for default.

        :param float import_scale:
            The import scale to be applied on the STL's geometry when importing.

        :param bool convert_yz:
            Whether the Y and Z axes should be swapped on the STL's geometry when importing.

        :rtype: RAPolyhedronProcess
        :return:
            A new polyhedron process.
        """

    def GetPolyhedronProcessNames(self):
        """
        Get the names of created polyhedron processes.

        :return:
            The list of polyhedron user process names.
        """

    def CreateSurfaceUserProcess(
        self,
        parent: ApiElementItem,
        stl_filename: str,
        name: str | None = None,
        import_scale: float = 1.0,
        convert_yz: bool = False,
    ) -> RASurfaceUserProcess | None:
        """
        Creates a new Surface process using the given parent as input.

        :param parent:
            The surface process parent.

        :param stl_filename:
            The filename with the stl to be loaded for the surface.

        :param name:
            The name of the new process or None for default.

        :param import_scale:
            The import scale to be applied on the STL's geometry when importing.

        :param convert_yz:
            Whether the Y and Z axes should be swapped on the STL's geometry when importing.

        :return:
            A new surface process.
        """

    def GetSurfaceUserProcessNames(self) -> list[str]:
        """
        Get the names of created surfaces processes.

        :return:
            The list of surfaces user process names.
        """

    def CreateParticleToContactProcess(self, parent, name=None):
        """
        Creates a new ParticleToContact process using the given parent as input.

        :param RAGridProcessElementItem parent:
            The new process' parent

        :param str|None name:
            The name of the new process or None for default

        :rtype: RAParticleToContactProcess
        :return:
            A new ParticleToContact process
        """

    def CreateContactToParticleProcess(self, parent, name=None):
        """
        Creates a new ContactToParticle process using the given parent as input.

        :param RAGridProcessElementItem parent:
            The new process' parent

        :param str|None name:
            The name of the new process or None for default

        :rtype: RAContactToParticleProcess
        :return:
            A new ContactToParticle process
        """

    def GetParticleToContactProcessNames(self):
        """
        Get the names of created Particle to Contact processes.

        :return:
            The list of Particle to Contact user process names
        """

    def GetContactToParticleProcessNames(self):
        """
        Get the names of created Contact to Particle processes.

        :return:
            The list of Contact to Particle user process names
        """

    def CreateStreamlinesUserProcess(
        self, parent: ApiElementItem, name: str | None = None
    ) -> RAStreamlinesUserProcess | None:
        """
        Creates a new StreamlinesUserProcess process using the given parent as input.

        :param parent:
            The parent process.

        :param name:
            The name of the new process or None for default
        """

    def GetStreamlinesUserProcessNames(self) -> list[str]:
        """
        Get the names of created streamlines processes.

        :return:
            The list of streamlines user process names.
        """
