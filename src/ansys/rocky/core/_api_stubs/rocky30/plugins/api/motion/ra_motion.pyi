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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

class RAMotion(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper representing a single Motion in a Motion Frame.

    Access individual motions via a :class:`RAMotionFrame`\'s motion list:

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions[0]
        motion_2 = motions.New()

    Every :class:`RAMotion` contains properties that are common to all motions (such as start
    and stop times) and properties that are specific to the motion\'s type (translation, vibration,
    etc). These latter properties must be accessed by a "sub-object" that is retrieved via
    :meth:`GetTypeObject()` after the specific motion type is configured via :meth:`SetType()`.

    .. code-block:: python

        motions = motion_frame.GetMotions()
        motion_1 = motions.New()
        motion_1.SetType(\'Translation\')
        translation = motion_1.GetTypeObject()
        # `translation` is a RATranslation
        translation.SetVelocity([1.0, 0.0, 0.0], \'m/s\')

    Refer to the specific PrePost Scripting wrappers for documentation on the individual motion types:

    * :class:`RATranslation`
    * :class:`RARotation`
    * :class:`RAPendulum`
    * :class:`RAVibration`
    * :class:`RAFreeBodyRotation`
    * :class:`RAFreeBodyTranslation`
    * :class:`RAPrescribedForce`
    * :class:`RAPrescribedMoment`
    * :class:`RASpringDashpotForce`
    * :class:`RASpringDashpotMoment`
    * :class:`RALinearTimeVariableForce`
    * :class:`RALinearTimeVariableMoment`
    * :class:`RATimeSeriesTranslation`
    * :class:`RATimeSeriesRotation`

    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetType(self, motion_type):
        """
        Set the concrete type of motion.

        :param unicode motion_type:
            The concrete motion type. Accepted values are the strings in the "Type" drop-down menu
            in the UI.
        :return:
            The PrePost Scripting wrapper representing the concrete motion type.
        """

    def GetType(self):
        """
        Get the concrete type of motion.

        :rtype: unicode
        :return:
            A string describing the type of motion. The returned value will be one of the strings
            in the "Type" drop-down menu in the UI.
        """

    def GetTypeObject(self):
        """
        Get the API object that wraps the specific motion type.

        :rtype: ApiElementItem
        """

    def GetValidTypes(self):
        """
        Return a list with the possible values for the motion's type.

        :rtype: list(unicode)
        :return:
            A list of accepted values for `SetType()`.
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
