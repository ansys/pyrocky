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

from collections.abc import Sequence

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.models.regions_of_interest.roi_cube import RoiCube as RoiCube

from ansys.rocky.app._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.app.motion._with_movement_mixin import _WithMovementMixin
from ansys.rocky.app.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RARegionOfInterestCube(
    RAGridProcessElementItem, _WithMovementMixin, _RAOrientationMixin
):
    """
    Rocky PrePost Scripting wrapper for a single Cube geometry.

    This wrapper class corresponds to an individual entry under the "Regions Of Interest" item on
    the project\'s data tree. Regions Of Interest can be retrieved from the :class:`RAStudy` or the
    :class:`RARegionsOfInterestCollection` via:

    .. code-block:: python

        roi_cube_1 = study.GetElement(\'Cube <1>\')
    """

    @classmethod
    def GetWrappedClass(cls) -> type: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetCenterAfterMovement(self, timestep: int) -> Tuple3F:
        """
        Get the Region of Interest center taking motion in account.
        """

    def GetCenter(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Center".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetCenter(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Center".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
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

    def GetSize(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Size".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetSize(self, values: Sequence[str | float], unit: str | None = None) -> None:
        """
        Set the values of "Size".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """
