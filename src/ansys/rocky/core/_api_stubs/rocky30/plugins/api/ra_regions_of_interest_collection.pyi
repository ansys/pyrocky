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

from rocky30.models.regions_of_interest.roi_collection import (
    RoiCollection as RoiCollection,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_region_of_interest_cube import (
    RARegionOfInterestCube as RARegionOfInterestCube,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_region_of_interest_cylinder import (
    RARegionOfInterestCylinder as RARegionOfInterestCylinder,
)

class RARegionsOfInterestCollection(RAList):
    """
    Rocky PrePost Scripting wrapper for the collection of Regions of Interest in a project.

    This wrapper corresponds to the "Regions Of Interest" item in the project\'s data tree. To
    retrieve the :class:`RARegionsOfInterestCollection` from a :class:`RAStudy`, use:

        roi_collection = study.GetRegionsOfInterestCollection()

    Instances of the :class:`RARegionsOfInterestCollection` class act as regular Python lists, and
    can be iterated on, accessed via index, etc:
    """

    @classmethod
    def GetWrappedClass(cls) -> type[RoiCollection]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def AddCube(self, name: str | None = None) -> RARegionOfInterestCube:
        """
        Add a new Cube. Returns the newly created item.
        """

    def AddCylinder(self, name: str | None = None) -> RARegionOfInterestCylinder:
        """
        Add a new Cylinder. Returns the newly created item.
        """
