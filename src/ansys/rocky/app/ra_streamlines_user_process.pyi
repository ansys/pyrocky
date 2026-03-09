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

from rocky30.plugins.sph.streamlines_user_process.streamlines_user_process import (
    StreamlinesUserProcessSubject as StreamlinesUserProcessSubject,
)

from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_circular_surface import RACircularSurface as RACircularSurface
from ansys.rocky.app.ra_process_element import (
    RASurfaceUserProcess as RASurfaceUserProcess,
)
from ansys.rocky.app.ra_process_element import RAUserProcess as RAUserProcess
from ansys.rocky.app.ra_rectangular_surface import (
    RARectangularSurface as RARectangularSurface,
)
from ansys.rocky.app.ra_surface import RASurface as RASurface

SurfaceTypes = RASurface | RASurfaceUserProcess | RARectangularSurface | RACircularSurface

class RAStreamlinesUserProcess(RAUserProcess):
    @classmethod
    def GetWrappedClass(cls) -> type[StreamlinesUserProcessSubject]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def UpdateStreamlines(self) -> None:
        """
        Recompute the streamlines from the current values of sources, spacing, direction and
        maximum length.

        Since computing the streamlines is potentially slow when the spacing is small, this method
        must be explicitly called in order to update the streamlines.
        """

    def GetSources(self) -> list[SurfaceTypes] | None:
        """
        Get the surfaces defined as sources to generate Streamlines.
        """

    def SetSources(self, surfaces: str | SurfaceTypes | list) -> None:
        """
        Set the surfaces as sources to generate Streamlines.
        """

    def GetAvailableSources(self) -> list[SurfaceTypes]:
        """
        Get available planar surfaces that can be used to generate Streamlines.
        """

    def GetDirection(self) -> str:
        """
        Get "Direction" as a string.

        :return:
            The returned value will be one of [\'forward\', \'backward\', \'both\'].
        """

    def SetDirection(self, value: str) -> None:
        """
        Set the value of "Direction".

        :param value:
            The value to set. Must be one of [\'forward\', \'backward\', \'both\'].
        :raises RockyApiError:
            If `value` is not a valid "Direction" option.
        """

    def GetValidDirectionValues(self) -> list[str]:
        """
        Get a list of all possible values for "Direction".

        :return:
            The returned list is [\'forward\', \'backward\', \'both\'].
        """

    def GetMaximumLength(self, unit: str | None = None) -> float:
        """
        Get the value of "Maximum Length".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMaximumLength(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Maximum Length".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
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

    def GetSpacing(self, unit: str | None = None) -> float:
        """
        Get the value of "Spacing".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetSpacing(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Spacing".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """
