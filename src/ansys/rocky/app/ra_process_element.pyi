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

from coilib50.process.base_process_subject import (
    AbstractProcessSubject as AbstractProcessSubject,
)
from coilib50.time.time_step_interface import ITimeStep as ITimeStep
from coilib50.units import Scalar as Scalar
from kraken20.plugins.api.ka_element_item import KAElementItem
from oop_ext.foundation.decorators import Abstract
from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.plugins.sph.surface_user_process.surface_user_process_subject import (
    SurfaceUserProcessSubject as SurfaceUserProcessSubject,
)
from rocky30.plugins.user_process.group.cube_process_group import (
    CubeProcessGroup as CubeProcessGroup,
)
from rocky30.plugins.user_process.group.cylinder_process_group import (
    CylinderProcessGroup as CylinderProcessGroup,
)
from rocky30.plugins.user_process.group.plane_process_group import (
    PlaneProcessGroup as PlaneProcessGroup,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CUBE_GROUP_CHILD_PROCESS_COMMAND_ID as CUBE_GROUP_CHILD_PROCESS_COMMAND_ID,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    CYLINDER_GROUP_CHILD_PROCESS_COMMAND_ID as CYLINDER_GROUP_CHILD_PROCESS_COMMAND_ID,
)
from rocky30.plugins.user_process.process_factories.group_process_factory_constants import (
    PLANE_GROUP_CHILD_PROCESS_COMMAND_ID as PLANE_GROUP_CHILD_PROCESS_COMMAND_ID,
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
from sci20.app.mesh_assembly.plane.mesh_assembly_plane_process import (
    BasePlane as BasePlane,
)
from sci20.plugins.api.api_process_element import SciApiProcessElementItem
from sci20.plugins.process.plane_process.plane_process_subject import PlaneProcessSubject

from ansys.rocky.app._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin
from ansys.rocky.app.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RAProcessElementItem(SciApiProcessElementItem):
    """
    Rocky api process model.
    """

    def GetCurve(
        self, curve_name, simulation_name=None, realization=None, time_step=None
    ):
        """
        Override base class implementation so to properly handle all delayed tasks that might being
        used to compute the required curve.
        """

class RAUserProcess(RAGridProcessElementItem):
    """
    Base class for UserProcesses
    """

    def GetNumberOfParticles(self, time_step):
        """
        Get the total number of particles in this selection. Only for processes created on Particles.

        :type time_step: unicode, ITimeStep or int
        :param time_step:
            Either a 'current' string with meaning the current time step
            or an ITimeStep identifying the time to get the topology shape
            or an int identifying the time step index to be used based on the global time set

        :rtype: int
        :returns:
            The number of particles
        """

    def IterParticles(self, time_step):
        """
        Iterate on particles in this selection at the given time. Only for processes created on Particles.

        :type time_step: unicode, ITimeStep or int
        :param time_step:
            Either a 'current' string with meaning the current time step
            or an ITimeStep identifying the time to get the topology shape
            or an int identifying the time step index to be used based on the global time set

        :rtype: iterator(Particle)
        :returns:
            An iterator over the particles.
            A Particle has:
            - x, y, z, size
            - x_axis, y_axis, z_axis, orientation_angle
            - type, particle_group
        """

class _RAAbstractCubeMixin:
    @Abstract
    def GetSubject(self) -> BaseCube: ...
    def GetCenter(self, unit=None):
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z center
        """

    def SetCenter(self, x: float, y: float, z: float, unit: str | None = None) -> None:
        """
        Sets the cube X, Y and Z center

        :param x: float
            The center X coordinate

        :param y:
            The center Y coordinate

        :param z:
            The center Z coordinate

        :param str|None unit:
            The unit of the given values or None if given in meters (m)
        """

    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F:
        """
        Get the Process center position considering the assigned motion.

        :return:
            Returns the X, Y and Z center
        """

    def GetSize(self, unit: str | None = None) -> Tuple3F:
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z cube magnitude
        """

    def SetSize(self, x: float, y: float, z: float, unit: str | None = None):
        """
        Sets the cube X, Y and Z magnitude

        :param x: float
            The X magnitude

        :param y:
            The Y magnitude

        :param z:
            The Z magnitude

        :param str|None unit:
            The unit of the given values or None if given in meters (m)
        """

    def GetRotation(self, unit=None):
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z cube rotation
        """

    def SetRotation(self, x, y, z, unit=None):
        """
        Sets the cube X, Y and Z rotation

        :param x: float
            The X rotation

        :param y:
            The Y rotation

        :param z:
            The Z rotation

        :param str|None unit:
            The unit of the given values or None if given in degrees (dega)
        """

class RACubeGroup(
    KAElementItem, _WithMovementMixin, _RAOrientationMixin, _RAAbstractCubeMixin
):
    @classmethod
    def GetWrappedClass(cls) -> type[CubeProcessGroup]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def AddProcess(self, source_process: AbstractProcessSubject) -> None: ...

class _RAAbstractCylinderMixin:
    """
    Mixin for classes that define a cylinder
    """

    @Abstract
    def GetSubject(self) -> BaseCylinder: ...
    def GetCenter(self, unit=None):
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z center
        """

    def SetCenter(self, x: float, y: float, z: float, unit: str | None = None) -> None:
        """
        Sets the cylinder X, Y and Z center

        :param x: float
            The center X coordinate

        :param y:
            The center Y coordinate

        :param z:
            The center Z coordinate

        :param str|None unit:
            The unit of the given values or None if given in meters (m)
        """

    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F:
        """
        Get the Process center position considering the assigned motion.

        :return:
            Returns the X, Y and Z center
        """

    def GetSize(self, unit: str | None = None) -> Tuple3F:
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z cylinder magnitude
        """

    def SetSize(self, x: float, y: float, z: float, unit: str | None = None) -> None:
        """
        Sets the cylinder X, Y and Z magnitude

        :param x: float
            The X magnitude

        :param y:
            The Y magnitude

        :param z:
            The Z magnitude

        :param str|None unit:
            The unit of the given values or None if given in meters (m)
        """

    def GetRotation(self, unit=None):
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z cylinder rotation
        """

    def SetRotation(self, x, y, z, unit=None):
        """
        Sets the cylinder X, Y and Z rotation

        :param x: float
            The X rotation

        :param y:
            The Y rotation

        :param z:
            The Z rotation

        :param str|None unit:
            The unit of the given values or None if given in degrees (dega)
        """

    def GetInternalFactor(self, unit=None):
        """
        :return internal_factor: float
            The internal hole radius factor (default %) of the external given by the size
        """

    def SetInternalFactor(self, internal_factor, unit=None) -> None:
        """
        Sets the internal hole radius factor of the external given by the size

        :param internal_factor: float
            The internal factor

        :param str|None unit:
            The unit of the given value or None if given in percentage (%)
        """

    def GetInitialAngle(self, unit=None):
        """
        :return initial_angle: float
            The initial angle (default dega) of the external given by the size
        """

    def SetInitialAngle(self, initial_angle, unit=None) -> None:
        """
        Sets the initial hole radius factor of the external given by the size

        :param initial_angle: float
            The initial angle

        :param str|None unit:
            The unit of the given value or None if given in degrees (dega)
        """

    def GetFinalAngle(self, unit=None):
        """
        :return final_angle: float
            The final angle (default dega) of the final given by the size
        """

    def SetFinalAngle(self, final_angle, unit=None) -> None:
        """
        Sets the final hole radius factor of the final given by the size

        :param final_angle: float
            The final angle

        :param str|None unit:
            The unit of the given value or None if given in degrees (dega)
        """

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

class RACylinderProcess(
    RAUserProcess, _WithMovementMixin, _RAOrientationMixin, _RAAbstractCylinderMixin
):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...

class RAFilterProcess(RAUserProcess):
    """
    PrePost Scripting wrapper for Property Processes.

    Limits properties by a specific cut or range of values.

    .. note::
        Originally named "RAPropertyProcess". Although the public api uses "Filter"
        for functions related to this process, the original "PropertyProcess" name
        is still used internally.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetType(self):
        """
        :rtype: 'Value' or 'Range'
        :return:
            Return whether the property process filters elements that match a specific value or a range of values
        """

    def SetType(self, filter_type) -> None:
        """
        :param filter_type: 'Value' or 'Range'
            Sets whether the property process filters elements that match a specific value or a range of values
        """

    def GetMode(self):
        """
        :rtype: unicode
        :return:
            'Cut' or 'Select', whether the property process is selecting or cutting the cell's from the input process
        """

    def SetMode(self, property_mode) -> None:
        """
        :param plane_mode: 'Cut' or 'Select'
            Sets whether the property process is selecting or cutting the cell's from the input process
        """

    def GetMinValue(self, unit=None):
        """
        :rtype: Scalar
        :return:
            Returns the lowest value by which you want the property results limited when Type is Range
        """

    def SetMinValue(self, value, unit=None) -> None:
        """
        Sets the lowest value by which you want the property results limited when Type is Range

        :param value: float
            The new minimum value

        :param str|None unit:
            The unit of the given value or None if given the same unit already used
        """

    def GetMaxValue(self, unit=None):
        """
        :rtype: Scalar
        :return:
            Returns the highest value by which you want the property results limited when Type is Range
        """

    def SetMaxValue(self, value, unit=None) -> None:
        """
        Sets the highest value by which you want the property results limited when Type is Range

        :param value: float
            The new maximum value

        :param str|None unit:
            The unit of the given value or None if given the same unit already used
        """

    def GetCutValue(self, unit=None):
        """
        :rtype: Scalar
        :return:
            Returns the single, exact value by which you want the property results limited when Type is Value
        """

    def SetCutValue(self, value, unit=None) -> None:
        """
        Sets the single, exact value by which you want the property results limited when Type is Value

        :param value: float
            The new cut value

        :param str|None unit:
            The unit of the given value or None if given the same unit already used
        """

    def SetPropertyGridFunction(self, grid_function, realization=None) -> None:
        """
        Set the grid function which this property process will use to filter its input elements

        :param unicode grid_function:
            The new grid function

        :param unicode realization:
            An additional keyword to identify the curve realization

        """

    def GetPropertyGridFunction(self):
        """
        Get the grid function which this property process will use to filter its input elements

        :rtype: unicode
        :return:
            The current grid function
        """

class _RAAbstractPlaneMixin:
    @Abstract
    def GetSubject(self) -> BasePlane: ...
    def GetType(self) -> str:
        """
        :return:
            'Cut' or 'Clip', whether the plane process is cutting or clipping the input process.
        """

    def SetType(self, plane_type: str) -> None:
        """
        :param plane_type:
            'Cut' or 'Clip', sets whether the plane process is cutting or clipping the input process.
        """

    def GetMode(self) -> str:
        """
        :return:
            'Exact' or 'Select', whether the plane process is selecting or cutting the cell's from the input process.
        """

    def SetMode(self, plane_mode: str) -> None:
        """
        :param plane_mode: 'Exact' or 'Select'
            Sets whether the plane process is selecting or cutting the cell's from the input process
        """

    def GetOrigin(self, unit=None) -> Tuple3F:
        """
        :return:
            Returns the X, Y and Z plane origin
        """

    def SetOrigin(self, x: float, y: float, z: float) -> None:
        """

        :param x:
        :param y:
        :param z:
        """

class RAPlaneProcess(RAUserProcess, _RAOrientationMixin, _RAAbstractPlaneMixin):
    @classmethod
    def GetWrappedClass(self) -> type[PlaneProcessSubject]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def SetRelativeRotationVector(self, x: float, y: float, z: float) -> None:
        """
        Set the X, Y and Z parameters of the plane normal
        """

    def GetRelativeRotationVector(self) -> Tuple3F:
        """
        Returns the X, Y and Z plane normal
        """

class RAPlaneGroup(KAElementItem, _RAOrientationMixin, _RAAbstractPlaneMixin):
    @classmethod
    def GetWrappedClass(cls) -> type[PlaneProcessGroup]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def AddProcess(self, source_process: AbstractProcessSubject) -> None: ...

class RATrajectoryProcess(RAUserProcess):
    """
    PrePost Scripting wrapper for Particle Trajectory Processes.

    Trajectory processes only work on particle-based processes. Before the trajectories can be
    analyzed the process must first be configured by calling :py:meth:`SetStartingTimeStep()`,
    :py:meth:`SetNumberOfTimeSteps()` and :py:meth:`SetParticleStride()`, followed by
    :py:meth:`UpdateParticlesSelection()`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetStartingTime(self, time: str | ITimeStep | int) -> None:
        """
        Set the initial time step for the computed trajectories.

        :param time:
            The time step to use as the initial one to compute the trajectories. Can be either a TimeStep,
            an integer representing the timestep's index in the timeset or the string 'current' for the
            current application time step.
        """

    def GetStartingTime(self) -> ITimeStep:
        """
        Get the time step currently configured as the initial one for the particle trajectories.
        """

    def SetNumberOfIntervals(self, number_of_intervals: int):
        """
        Set the total number of intervals in the computed trajectories.
        """

    def GetNumberOfIntervals(self) -> int:
        """
        Get the total number of intervals in the computed trajectories.
        """

    def SetParticleStride(self, particle_stride) -> None:
        """
        Set the particle stride for computed trajectories.

        The "stride" is the number of particles that are "skipped" when selecting the particles
        whose trajectories will be computed. For example, if this value is 1 then the trajectories
        of all particles in the starting timestep will be computed. If 2, the trajectory of every
        other particle (one out of every two) will be computed, etc.

        :param int particle_stride:
        """

    def GetParticleStride(self):
        """
        Get the particle stride for computed trajectories.

        :see: SetParticleStride()
        :rtype: int
        """

    def UpdateParticlesSelection(self) -> None:
        """
        Recompute the trajectories from the current values of starting timestep, number of timesteps
        and particle stride.

        Since computing the trajectories is potentially slow when the number of particles and/or
        timesteps is big, this method must be explicitly called in order to update the trajectories.
        """

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
    def GetCenter(self, unit=None) -> Tuple3F:
        """
        :return:
            Returns the X, Y and Z Polyhedron center
        """

    def SetCenter(self, x: float, y: float, z: float, unit: str | None = None) -> None:
        """
        Sets the Polyhedron X, Y and Z center

        :param x:
            The center X coordinate

        :param y:
            The center Y coordinate

        :param z:
            The center Z coordinate

        :param unit:
            The unit of the given values or None if given in meters (m)
        """

    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F:
        """
        Get the Process center position considering the assigned motion.

        :return:
            Returns the X, Y and Z center
        """

    def SetSTL(self, filename: str, mesh_unit: str | None = None) -> None:
        """
        Sets the Polyhedron file

        :param filename:
            Path to the file to be used

        :param mesh_unit:
            unit to be used for the mesh, or None if given in meters (m)
        """

    def GetName(self) -> str:
        """
        Get the value of "Name".

        """

    def SetName(self, value: str) -> None:
        """
        Set the value of "Name".

        :param value:
            The value to set.
        """

    def GetScale(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Scale".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetScale(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Scale".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

class RASurfaceUserProcess(RAUserProcess, _WithMovementMixin, _RAOrientationMixin):
    @classmethod
    def GetWrappedClass(cls) -> type["SurfaceUserProcessSubject"]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def SetSTL(self, filename: str, mesh_unit: str | None = None) -> None:
        """
        Sets the Polyhedron file

        :param filename: string
            Path to the file to be used

        :param mesh_unit: string or None
            unit to be used for the mesh, or None if given in meters (m)
        """

    def GetCenter(self, unit: str | None = None) -> Tuple3F:
        """
        :rtype: tuple(float, float, float)
        :return:
            Returns the X, Y and Z Polyhedron center
        """

    def SetCenter(self, x: float, y: float, z: float, unit: str | None = None) -> None:
        """
        Sets the Polyhedron X, Y and Z center

        :param x: float
            The center X coordinate

        :param y:
            The center Y coordinate

        :param z:
            The center Z coordinate

        :param str|None unit:
            The unit of the given values or None if given in meters (m)
        """

    def GetName(self) -> str:
        """
        Get the value of "Name".

        """

    def SetName(self, value: str) -> None:
        """
        Set the value of "Name".

        :param value:
            The value to set.
        """

    def GetScale(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Scale".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetScale(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Scale".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """
