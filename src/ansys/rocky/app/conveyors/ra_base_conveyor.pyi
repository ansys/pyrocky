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

from ben10.foundation.decorators import Override as Override
from rocky30.models.geometry.conveyors.conveyor_belt_profile import (
    BELT_PROFILE_STRING_TO_CAPTION as BELT_PROFILE_STRING_TO_CAPTION,
)
from rocky30.models.geometry.conveyors.conveyor_belt_profile import (
    BeltProfileCaptionFromString as BeltProfileCaptionFromString,
)
from rocky30.models.geometry.conveyors.conveyor_belt_profile import (
    BeltProfileStringFromCaption as BeltProfileStringFromCaption,
)
from rocky30.models.geometry.conveyors.conveyor_belt_profile import (
    SetupNewBeltProfile as SetupNewBeltProfile,
)

from ansys.rocky.app.ra_base_geometry import RABaseGeometry as RABaseGeometry

class RABaseConveyor(RABaseGeometry):
    """
    Base class for Rocky API conveyor models.
    """

    def GetBeltProfileName(self):
        """
        Get the name of the belt profile.

        :rtype: str
        :return:
            A string describing the type of belt profile. The returned value will be one of the strings
            in the "Belt Profile" drop-down menu in the UI.
        """

    def GetBeltProfile(self):
        """
        :rtype: ApiElementItem
        :return:
            The API object that wraps the current belt profile.
        """

    def SetBeltProfile(self, belt_profile_name):
        """
        Set the belt profile object through its name as shown in the UI.

        :param str belt_profile_name:
            Accepted values are the strings in the "Belt Profile" dropdown menu in the UI.

        :rtype: ApiElementItem
        :return:
            The PrePost Scripting wrapper representing the belt profile.
        """

    def GetValidBeltProfileNames(self):
        """
        Return a list with possible values for belt profile.

        :rtype: list(str)
        :return:
            A list of accepted values for `SetBeltProfile()`.
        """
