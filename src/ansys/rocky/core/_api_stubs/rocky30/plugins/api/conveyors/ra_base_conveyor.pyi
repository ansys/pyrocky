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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import (
    RABaseGeometry as RABaseGeometry,
)

class RABaseConveyor(RABaseGeometry):
    def GetBeltProfileName(self): ...
    def GetBeltProfile(self): ...
    def SetBeltProfile(self, belt_profile_name): ...
    def GetValidBeltProfileNames(self): ...
