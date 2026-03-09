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

from ansys.rocky.app.api_element_item import ApiElementItem

class RAFreeBodyRotation(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing a Free Body Rotation motion.

    Retrieve this specific wrapper after setting the correct motion type on a :class:`RAMotion`. For
    example:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType('Free Body Rotation')
        free_body_rotation = motion_1.GetTypeObject()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetFreeMotionDirection(self) -> str:
        """
        Get "Free Motion Direction" as a string.

        :return:
            The returned value will be one of [\'none\', \'x\', \'y\', \'xy\', \'z\', \'xz\', \'yz\', \'xyz\'].
        """

    def SetFreeMotionDirection(self, value: str) -> None:
        """
        Set the value of "Free Motion Direction".

        :param value:
            The value to set. Must be one of [\'none\', \'x\', \'y\', \'xy\', \'z\', \'xz\', \'yz\', \'xyz\'].
        :raises RockyApiError:
            If `value` is not a valid "Free Motion Direction" option.
        """

    def GetValidFreeMotionDirectionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Free Motion Direction".

        :return:
            The returned list is [\'none\', \'x\', \'y\', \'xy\', \'z\', \'xz\', \'yz\', \'xyz\'].
        """
