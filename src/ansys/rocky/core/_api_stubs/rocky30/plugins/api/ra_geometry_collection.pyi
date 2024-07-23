# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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

from collections.abc import Iterator

from barril.units import FixedArray as FixedArray
from coilib50.subject import Subject as Subject
from coilib50.time.time_step_interface import ITimeStep as ITimeStep
from rocky30.models.geometry.geometry_collection import (
    GeometryCollection as GeometryCollection,
)

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    CheckResults as CheckResults,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import (
    RABaseGeometry as RABaseGeometry,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAGeometryCollection(ApiElementItem):
    @classmethod
    def GetWrappedClass(cls) -> type[GeometryCollection]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetGeometryNames(self) -> list[str]: ...
    def GetGeometry(self, geometry_name): ...
    def IterInputGeometries(self) -> Iterator[RABaseGeometry]: ...
    def IterInletGeometries(self) -> Iterator[RABaseGeometry]: ...
    def IterSurfaces(self) -> Iterator[RABaseGeometry]: ...
    def IterWalls(self) -> Iterator[RABaseGeometry]: ...
    def IterSystemCouplingWalls(self) -> Iterator[RABaseGeometry]: ...
    def GetBoundingBox(
        self, time_step: Union[ITimeStep, None], force_load: bool = ...
    ) -> tuple[FixedArray, FixedArray]: ...
    def RemoveGeometry(self, geometry: Union[RABaseGeometry, str, None]) -> None: ...
    def __iter__(self) -> Iterator[ApiElementItem]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> RABaseGeometry: ...
