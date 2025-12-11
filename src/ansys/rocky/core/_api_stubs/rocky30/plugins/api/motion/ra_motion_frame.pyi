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

from ansys.rocky.core._api_stubs.rocky30.plugins.api._ra_orientation_mixin import (
    _RAOrientationMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_base_motion import (
    RABaseMotionFrame as RABaseMotionFrame,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion import (
    RAMotion as RAMotion,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion_list import (
    RAMotionList as RAMotionList,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToFixedArray as ConvertUserPassedValueToFixedArray,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_utils import (
    ConvertUserPassedValueToScalar as ConvertUserPassedValueToScalar,
)

class RAMotionFrame(RABaseMotionFrame, RAGridProcessElementItem, _RAOrientationMixin):
    """
    Rocky PrePost Scripting wrapper for a motion frame.

    The class contains methods to configure a motion frame and its motions. There are some options
    to retrieve a specific :class:`RAMotionFrame` in a project from a :class:`RAStudy`, a
    :class:`RAMotionFrameSource` or another :class:`RAMotionFrame`:

    .. code-block:: python

        # From the RAStudy
        motion_frame = study.GetElement(\'<motion frame name>\')

        # From the RAMotionFrameSource
        frame_source = study.GetMotionFrameSource()
        motion_frame = frame_source.GetMotionFrame(\'<motion frame name>\')

        # From a "parent" motion frame
        frame_1 = study.GetElement(\'<frame 1 name>\')
        frame_2 = frame_1.GetMotionFrame(\'<frame 2 name>\')

    A motion frame comprises frame properties (relative position, rotation angle, free body limits,
    etc) and a list of motions. The properties are manipulated via direct `Get*()` and `Set*()`
    methods, while the motions are accessed separately via the list returned by :meth:`GetMotions()`.

    Motion frames can be created on the "root" of the project\'s motion frames (the source returned
    in :meth:`RAStudy.GetMotionFrameSource()`), or as a \'child\' frame of a pre-existing motion frame:

    .. code-block:: python

        frame_source = study.GetMotionFrameSource()

        # Create a motion frame with no parent frame
        frame_1 = frame_source.NewFrame()
        # Configure this new frame frame_1
        frame_1.SetRelativePosition(...)
        frame_1.SetEnablePeriodicMotion(...)
        # ... configure motions, etc.

        # Create a new frame, as a child of `frame_1`
        frame_2 = frame_1.NewFrame()
        # Configure this new frame frame_2
        frame_2.SetRelativePosition(...)
        # ... configure motions, etc.
    """

    def __init__(self, id, model_id=None) -> None: ...
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def AddFreeBodyTranslationMotion(self, motion_direction: str = "none") -> RAMotion:
        """
        Adds a free body translation motion to the frame.

        :param motion_direction:
            The motion direction string. It can be one of the followings:
            ['none', 'x', 'y', 'xy', 'z', 'xz', 'yz', 'xyz']

        :return:
            Returns the RAMotion created.
        """

    def AddFreeBodyRotationMotion(self, motion_direction: str = "none") -> RAMotion:
        """
        Adds a free body rotation motion to the frame.

        :param motion_direction:
            The motion direction string. It can be one of the followings:
            ['none', 'x', 'y', 'xy', 'z', 'xz', 'yz', 'xyz']

        :return:
            Returns the RAMotion created.
        """

    def AddPendulumMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        initial_frequency=(0.0, "Hz"),
        angular_initial_amplitude=(0.0, "rad"),
        direction=((0.0, 0.0, 0.0), "m"),
        angular_initial_phase=(0.0, "rad"),
        frequency_variation=(0.0, "Hz/s"),
        angular_amplitude_variation=(0.0, "rad/s"),
    ):
        """
        Adds a pendulum motion to the frame.

        :param float start_time:
            The start time for the motion.

        :param float stop_time:
            The end time for the motion.

        :param float initial_frequency:
            The initial frequency of the rotation (in Hz).

        :param float angular_initial_amplitude:
            The initial angular amplitude of the rotation (in rad).

        :param list(float) direction:
            The direction of the rotation (in m).

        :param list(float) angular_initial_phase:
            The initial angular phase of the rotation (in rad).

        :param float frequency_variation:
            The variation of the frequency (in Hz/s).

        :param float angular_amplitude_variation:
            The angular amplitude variation (in rad/s).

        """

    def AddVibrationMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        initial_frequency=(0.0, "Hz"),
        initial_amplitude=(0.0, "m"),
        direction=((0.0, 0.0, 0.0), "m"),
        frequency_variation=(0.0, "Hz/s"),
        amplitude_variation=(0.0, "m/s"),
    ):
        """
        Adds a vibration motion to the frame.

        :param float start_time:
            The start time for the motion.

        :param float stop_time:
            The end time for the motion.

        :param float initial_frequency:
            The initial frequency of the vibration (in Hz).

        :param float initial_amplitude:
            The initial amplitude of the vibration (in m).

        :param list(float) direction:
            The direction of the vibration (in m).

        :param float frequency_variation:
            The variation of the frequency (in Hz/s).

        :param float amplitude_variation:
            The amplitude variation (in m/s).

        """

    def AddRotationMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        angular_velocity=((0.0, 0.0, 0.0), "rad/s"),
        angular_acceleration=((0.0, 0.0, 0.0), "rad/s2"),
    ):
        """
        Adds a rotation motion to the frame.

        :param float start_time:
            The start time for the motion.

        :param float stop_time:
            The end time for the motion.

        :param list(float) angular_velocity:
            The motion angular velocity (x, y, z).

        :param list(float) angular_acceleration:
            The motion angular acceleration (x, y, z).

        :return RAMotion:
            Returns the motion created.
        """

    def AddTranslationMotion(
        self,
        start_time=(0.0, "s"),
        stop_time=(1000.0, "s"),
        velocity=((0.0, 0.0, 0.0), "m/s"),
        acceleration=((0.0, 0.0, 0.0), "m/s2"),
        define_as: str = "fixed_velocity",
        final_velocity=((0.0, 0.0, 0.0), "m/s"),
    ):
        """
        Adds a translation motion to the frame.

        :param float start_time:
            The start time for the motion.

        :param float stop_time:
            The end time for the motion.

        :param list(float,float,float) velocity:
            The motion velocity (x, y, z) in m/s.

        :param list(float,float,float) acceleration:
            The motion acceleration (x, y, z) in m/s2

        :param bool displace_geometry:
            Whether the geometry should be displaced with the movement or not.

        :param unicode define_as:
            How it should be defined. Valid values are:
                'fixed_velocity'
                'initial_and_final_velocity'
                'initial_velocity_and_acceleration'

        :param list(float,float,float) final_velocity:
            The final motion velocity (x, y, z) in m/2.

            Used only if define_as == 'initial_and_final_velocity', in which case
            the initial velocity is given by the velocity parameter.

        :return RAMotion:
            Returns the motion created.
        """

    def ApplyTo(self, obj) -> None:
        """
        Link this motion frame to the given geometry.

        :param Subject|ScriptingWrapper obj:
            Either the actual object or the wrapper in the scripting for the object.
        """

    def GetMotions(self) -> RAMotionList:
        """
        Get the list of motions in the motion frame.

        :return:
            Returns a list with the motions configured.
        """

    def GetFbmMaxAngularLimits(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Fbm Max Angular Limits".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "dega".
        """

    def SetFbmMaxAngularLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Fbm Max Angular Limits".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "dega".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetFbmMaxLinearLimits(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Fbm Max Linear Limits".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetFbmMaxLinearLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Fbm Max Linear Limits".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetFbmMinAngularLimits(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Fbm Min Angular Limits".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "dega".
        """

    def SetFbmMinAngularLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Fbm Min Angular Limits".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "dega".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetFbmMinLinearLimits(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Fbm Min Linear Limits".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetFbmMinLinearLimits(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Fbm Min Linear Limits".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetEnableFbmAngularLimits(self) -> bool:
        """
        Get the value of "Enable Fbm Angular Limits".

        """

    def SetEnableFbmAngularLimits(self, value: bool) -> None:
        """
        Set the value of "Enable Fbm Angular Limits".

        :param value:
            The value to set.
        """

    def GetEnableFbmLinearLimits(self) -> bool:
        """
        Get the value of "Enable Fbm Linear Limits".

        """

    def SetEnableFbmLinearLimits(self, value: bool) -> None:
        """
        Set the value of "Enable Fbm Linear Limits".

        :param value:
            The value to set.
        """

    def GetEnablePeriodicMotion(self) -> bool:
        """
        Get the value of "Enable Periodic Motion".

        """

    def SetEnablePeriodicMotion(self, value: bool) -> None:
        """
        Set the value of "Enable Periodic Motion".

        :param value:
            The value to set.
        """

    def GetKeepInPlace(self) -> int:
        """
        Get the value of "Keep In Place".

        """

    def SetKeepInPlace(self, value: str | int) -> None:
        """
        Set the value of "Keep In Place".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
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

    def GetPeriodicMotionPeriod(self, unit: str | None = None) -> float:
        """
        Get the value of "Periodic Motion Period".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetPeriodicMotionPeriod(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Periodic Motion Period".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetPeriodicMotionStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Periodic Motion Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetPeriodicMotionStartTime(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Periodic Motion Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetPeriodicMotionStopTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Periodic Motion Stop Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetPeriodicMotionStopTime(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Periodic Motion Stop Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetRelativePosition(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Relative Position".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetRelativePosition(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Relative Position".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """
