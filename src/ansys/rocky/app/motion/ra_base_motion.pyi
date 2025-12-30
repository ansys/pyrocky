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

from collections.abc import Generator

from _typeshed import Incomplete

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.motion.ra_motion_frame import RAMotionFrame as RAMotionFrame

class RABaseMotionFrame(ApiElementItem):
    """
    Base class for Api representations of MotionFrames and MotionFrameSources. Provides methods
    to create, iterate and remove motion frames.
    """

    def NewFrame(self) -> RAMotionFrame:
        """
        Creates a new motion frame.
        """

    def NewConeCrusherFrame(self):
        """
        Creates a new cone crusher frame.

        :rtype: RAConeCrusherFrame
        """

    def IterMotionFrames(self) -> Generator[Incomplete]:
        """
        Iterates over all the motion frames available (recursively).

        :return iter(RAMotionFrame):
        """

    def GetMotionFrame(self, frame_name):
        """
        Get a specific motion frame given its name.

        :param unicode frame_name:

        :rtype: RAMotionFrame
        """

    def RemoveFrame(self, motion_frame) -> None:
        """
        Removes a previously-created motion frame.

        :param RAMotionFrame or RAConeCrusherFrame motion_frame:
        """

    def GetParentMotionFrame(self):
        """
        Gets the parent motion frame.
        If the Motion Frame is a RAMotionFrameSource it returns None.

        :rtype: RAMotionFrame
        """
