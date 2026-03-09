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

from ansys.rocky.app.motion.ra_base_motion import RABaseMotionFrame as RABaseMotionFrame

class RAConeCrusherFrame(RABaseMotionFrame):
    """
    Rocky PrePost Scripting wrapper for a cone crusher frame.

    The class contains methods to configure a cone crusher frame. There are some options
    to retrieve a specific :class:`RAConeCrusherFrame` in a project from a :class:`RAStudy`,
    a :class:`RAMotionFrameSource`, another :class:`RAConeCrusherFrame` or a :class:`RAMotionFrame`:

    .. code-block:: python

        # From the RAStudy
        motion_frame = study.GetElement(\'<motion frame name>\')

        # From the RAMotionFrameSource
        frame_source = study.GetMotionFrameSource()
        motion_frame = frame_source.GetMotionFrame(\'<motion frame name>\')

        # From a "parent" motion frame
        frame_1 = study.GetElement(\'<frame 1 name>\')
        frame_2 = frame_1.GetMotionFrame(\'<frame 2 name>\')

    Motion frames can be created on the "root" of the project\'s cone crusher frames (the source returned
    in :meth:`RAStudy.GetMotionFrameSource()`), or as a \'child\' frame of a pre-existing cone crusher frame:

    .. code-block:: python

        frame_source = study.GetMotionFrameSource()

        # Create a motion frame with no parent frame
        frame_1 = frame_source.NewConeCrusherFrame()
        # Configure this new frame frame_1
        frame_1.SetInitialOrientation(...)
        frame_1.SetPivotPoint(...)

        # Create a new frame, as a child of `frame_1`
        frame_2 = frame_1.NewConeCrusherFrame()
        # Configure this new frame frame_2
        frame_2.SetInitialOrientation(...)
        # ... configure motions, etc.
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetInitialOrientation(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Initial Orientation".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetInitialOrientation(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Initial Orientation".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetPivotPoint(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Pivot Point".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetPivotPoint(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Pivot Point".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetRotationAxis(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Rotation Axis".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetRotationAxis(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Rotation Axis".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetRotationalVelocity(self, unit: str | None = None) -> float:
        """
        Get the value of "Rotational Velocity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "rad/s".
        """

    def SetRotationalVelocity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Rotational Velocity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "rad/s".
        """

    def GetStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetStartTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetStopTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Stop Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetStopTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Stop Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """
