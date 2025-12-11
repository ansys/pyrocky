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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion.ra_motion import (
    RAMotion as RAMotion,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RAMotionList(RAList[RAMotion]):
    """
    Rocky PrePost Scripting wrapper to manipulate the motions in a single Motion Frame.

    To get the :class:`RAMotionList` from a :class:`RAMotionFrame`, use:

    .. code-block:: python

        motions = motion_frame.GetMotions()

    The :class:`RAMotionList` class acts as a regular Python list, with the usual methods to iterate
    and access individual motions:

    .. code-block:: python

        motion_1 = motions.New()
        motion_2 = motions.New()

        for motion in motions:
            motion.SetStartTime(1, 's')

        del motions[0]
        motions.Clear()

    The items in the motion list are of type :class:`RAMotion`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
