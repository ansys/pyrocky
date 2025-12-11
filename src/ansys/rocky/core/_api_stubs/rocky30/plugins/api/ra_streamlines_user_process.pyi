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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_circular_surface import (
    RACircularSurface as RACircularSurface,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RASurfaceUserProcess as RASurfaceUserProcess,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_process_element import (
    RAUserProcess as RAUserProcess,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_rectangular_surface import (
    RARectangularSurface as RARectangularSurface,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_surface import (
    RASurface as RASurface,
)

SurfaceTypes = RASurface | RASurfaceUserProcess | RARectangularSurface | RACircularSurface

class RAStreamlinesUserProcess(RAUserProcess):
    @classmethod
    def GetWrappedClass(cls) -> type[StreamlinesUserProcessSubject]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def UpdateStreamlines(self) -> None: ...
    def GetSources(self) -> list[SurfaceTypes] | None: ...
    def SetSources(self, surfaces: str | SurfaceTypes | list) -> None: ...
    def GetAvailableSources(self) -> list[SurfaceTypes]: ...
    def GetDirection(self) -> str: ...
    def SetDirection(self, value: str) -> None: ...
    def GetValidDirectionValues(self) -> list[str]: ...
    def GetMaximumLength(self, unit: str | None = None) -> float: ...
    def SetMaximumLength(self, value: str | float, unit: str | None = None) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetSpacing(self, unit: str | None = None) -> float: ...
    def SetSpacing(self, value: str | float, unit: str | None = None) -> None: ...
