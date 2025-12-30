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

from ansys.rocky.app.motion.ra_base_motion import RABaseMotionFrame as RABaseMotionFrame

class RAMotionFrameSource(RABaseMotionFrame):
    """
    Rocky PrePost Scripting wrapper for the root element for Motion Frames

    This class represents the "Motion Frame" item on the project\'s data tree. Get the :class:`RAMotionFrameSource`
    from a :class:`RAStudy` via:

    .. code-block:: python

        motion_frame_source = study.GetMotionFrameSource()

    This is the element through which motion frames with no parent frames can be created, and through
    which all motion frames can be directly accessed:

    .. code-block:: python

        motion_frame_1 = motion_frame_source.NewFrame()
        motion_frame_2 = motion_frame.GetMotionFrame(\'My Frame\')
        for motion_frame in motion_frame.IterMotionFrames():
            motion_frame.SetRelativePosition([1.0, 2.0, 3.0], \'m\')
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
