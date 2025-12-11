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

from pathlib import Path

from rocky30.models.point_cloud.point_cloud import PointCloud as PointCloud

from ansys.rocky.core._api_stubs.rocky30.plugins.api.motion._with_movement_mixin import (
    _WithMovementMixin,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RAPointCloud(RAGridProcessElementItem, ElementWithAddins, _WithMovementMixin):
    """
    Rocky PrePost Scripting wrapper for a point cloud in the project.

    The wrapper corresponds to an individual PointCloud in the project\'s data tree, below the
    "Point Clouds" item. PointCloud can be retrieved from the :class:`RAStudy` or the
    :class:`RAPointCloudCollection` via:

    .. code-block:: python

        point_cloud_1 = study.GetElement(\'Point Cloud 1\')
        point_cloud_2 = point_cloud_collection[1]
    """

    @classmethod
    def GetWrappedClass(self) -> type[PointCloud]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetFilePath(self) -> str:
        """
        Get the value of "File Path".
        """

    def SetFilePath(self, file_path: str | Path) -> None:
        """
        Set the path of the file that will be used to generate the point cloud
        described on the content of the file.

        The accepted file extensions is ".txt".
        """

    def IsTransient(self) -> bool:
        """
        Returns True if the Point Cloud is transient, False otherwise.
        """

    def GetEnablePeriodic(self) -> bool:
        """
        Get the value of "Enable Periodic".

        """

    def SetEnablePeriodic(self, value: bool) -> None:
        """
        Set the value of "Enable Periodic".

        :param value:
            The value to set.
        """

    def EnablePeriodic(self) -> None:
        """
        Set the value of "Periodic" to True.
        """

    def DisablePeriodic(self) -> None:
        """
        Set the value of "Periodic" to False.
        """

    def IsPeriodicEnabled(self) -> bool:
        """
        Check if the "Periodic" is enabled.

        """

    def GetPeriodicStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Periodic Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetPeriodicStartTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Periodic Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetPeriodicStopTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Periodic Stop Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetPeriodicStopTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Periodic Stop Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetSearchCutOff(self) -> bool:
        """
        Get the value of "Search Cut Off".

        """

    def SetSearchCutOff(self, value: bool) -> None:
        """
        Set the value of "Search Cut Off".

        :param value:
            The value to set.
        """

    def GetSearchCutOffDistance(self, unit: str | None = None) -> float:
        """
        Get the value of "Search Cut Off Distance".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetSearchCutOffDistance(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Search Cut Off Distance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """
