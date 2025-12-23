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
from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin
from ansys.rocky.app.motion.ra_motion_frame import RAMotionFrame as RAMotionFrame
from ansys.rocky.app.ra_addins import ElementWithAddins as ElementWithAddins

class RACustomInput(ApiElementItem, ElementWithAddins, _WithMovementMixin):
    """
    Rocky PrePost Scripting wrapper for a single Custom Input.

    This wrapper class corresponds to an individual entry under the "Inputs" item on the project\'s
    data tree. Particle inputs can be retrieved from the :class:`RAStudy` or the
    :class:`RAInletsOutletsCollection` via:

    .. code-block:: python

        input_1 = study.GetElement(\'Custom Input <1>\')
        input_2 = input_collection.GetParticleInput(\'Custom Input <2>\')

    Instances of :class:`RACustomInput` gives access to its two properties:
    The id of the Particle that will be used in the particle generation and the path of the csv file which will
    contain the information for each desired particle to be generated, such as, positioning, size, release time.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetFilePath(self):
        """
        Get the value of "File Path".

        :rtype: str
        """

    def SetFilePath(self, file_path) -> None:
        """
        Set the path of the file that will be used to generate the particles
        described on the content of the file.

        The accepted file extensions are [".csv", ".xls", ".xlsx", ".xlsm", ".xlsb", ".odf"].

        :param str or Path file_path:
        """

    def GetMotionFrame(self):
        """
        Get the "Motion Frame".

        :rtype: :class:`RAMotionFrame`
        """

    def SetMotionFrame(self, motion_frame: RAMotionFrame | str | None) -> None:
        """
        Assign a Motion Frame to the custom input.

        :param motion_frame:
            Either the API object or its name.
        """

    def GetAvailableMotionFrames(self):
        """
        Get all available Motion Frames.

        :rtype: List[:class:`RAMotionFrame`]
            A list of :class:`RAMotionFrame`.
        """

    def GetDefaultTemperature(self, unit: str | None = None) -> float:
        """
        Get the value of "Default Temperature".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "K".
        """

    def SetDefaultTemperature(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Default Temperature".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "K".
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

    def GetParticle(self):
        """
        Get the "Particle".

        :rtype: :class:`RAParticle`
        """

    def SetParticle(self, value) -> None:
        """
        Set the "Particle".

        :param unicode, :class:`RAParticle` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableParticles(self):
        """
        Get all available Particles.

        :rtype: List[:class:`RAParticle`]
            A list of :class:`RAParticle`.
        """
