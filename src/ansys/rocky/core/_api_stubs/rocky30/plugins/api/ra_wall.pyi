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

from collections.abc import Sequence
from typing import List, Optional, Union

from rocky30.base_types import Tuple3F as Tuple3F
from rocky30.core.geometry.rocky_document_constants import (
    UNIT_PLANE_ANGLE as UNIT_PLANE_ANGLE,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import (
    RABaseGeometry as RABaseGeometry,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import (
    RAProject as RAProject,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAWall(RABaseGeometry, ElementWithAddins):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def LoadFile(
        self, file_path: str, import_scale: float = ..., convert_yz: bool = ...
    ) -> None: ...
    def GetUseWear(self) -> bool: ...
    def SetUseWear(self, value: bool) -> None: ...
    def HasMotionFrame(self) -> bool: ...
    def GetHorizontalOffset(self, unit: Union[str, None] = ...) -> float: ...
    def SetHorizontalOffset(
        self, value: Union[str, float], unit: Union[str, None] = ...
    ) -> None: ...
    def GetVerticalOffset(self, unit: Union[str, None] = ...) -> float: ...
    def SetVerticalOffset(
        self, value: Union[str, float], unit: Union[str, None] = ...
    ) -> None: ...
    def GetOutOfPlaneOffset(self, unit: Union[str, None] = ...) -> float: ...
    def SetOutOfPlaneOffset(
        self, value: Union[str, float], unit: Union[str, None] = ...
    ) -> None: ...
    def GetOrientation(self, unit: str = ...) -> Tuple3F: ...
    def SetOrientation(self, rotation: Tuple3F, unit: str = ...) -> None: ...
    def SetOrientationFromAngles(
        self,
        rotation: Tuple3F,
        unit: str = ...,
        local_angles: bool = ...,
        order: str = ...,
    ) -> None: ...
    def SetOrientationFromAngleAndVector(
        self, angle: float, vector: Tuple3F, unit: str = ...
    ) -> None: ...
    def SetOrientationFromBasisVector(
        self, vector_x: Tuple3F, vector_y: Tuple3F, vector_z: Tuple3F
    ) -> None: ...
    def GetOrientationFromAngles(self, unit: str = ...) -> Tuple3F: ...
    def GetOrientationFromAngleAndVector(
        self, unit: str = ...
    ) -> tuple[float, Tuple3F]: ...
    def GetOrientationFromBasisVector(self) -> tuple[Tuple3F, Tuple3F, Tuple3F]: ...
    def GetDisableTime(self, unit: Optional[str] = ...) -> float: ...
    def SetDisableTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetEnableTime(self, unit: Optional[str] = ...) -> float: ...
    def SetEnableTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetPivotPoint(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetPivotPoint(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetTemperature(self, unit: Optional[str] = ...) -> float: ...
    def SetTemperature(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetThermalBoundaryConditionType(self) -> str: ...
    def SetThermalBoundaryConditionType(self, value: str) -> None: ...
    def GetValidThermalBoundaryConditionTypeValues(self) -> List[str]: ...
    def GetTranslation(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetTranslation(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetTriangleSize(self, unit: Optional[str] = ...) -> float: ...
    def SetTriangleSize(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetBoundaryMass(self, unit: Optional[str] = ...) -> float: ...
    def SetBoundaryMass(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetGravityCenter(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetGravityCenter(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetMomentXDirection(self) -> List[float]: ...
    def SetMomentXDirection(self, values: List[Union[str, float]]) -> None: ...
    def GetMomentYDirection(self) -> List[float]: ...
    def SetMomentYDirection(self, values: List[Union[str, float]]) -> None: ...
    def GetMomentZDirection(self) -> List[float]: ...
    def SetMomentZDirection(self, values: List[Union[str, float]]) -> None: ...
    def GetPrincipalMomentOfInertia(self, unit: Optional[str] = ...) -> List[float]: ...
    def SetPrincipalMomentOfInertia(
        self, values: Sequence[Union[str, float]], unit: Optional[str] = ...
    ) -> None: ...
    def GetName(self) -> str: ...
    def SetName(self, value: str) -> None: ...
    def GetPeriodicReplication(self) -> bool: ...
    def SetPeriodicReplication(self, value: bool) -> None: ...
    def GetNumberOfReplications(self) -> int: ...
    def SetNumberOfReplications(self, value: Union[str, int]) -> None: ...
    def GetReplicateGeometry(self) -> bool: ...
    def SetReplicateGeometry(self, value: bool) -> None: ...
    def GetReplicateTime(self, unit: Optional[str] = ...) -> float: ...
    def SetReplicateTime(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetSphBoundaryType(self) -> str: ...
    def SetSphBoundaryType(self, value: str) -> None: ...
    def GetValidSphBoundaryTypeValues(self) -> List[str]: ...
    def GetVolumeShearWorkRatio(self, unit: Optional[str] = ...) -> float: ...
    def SetVolumeShearWorkRatio(
        self, value: Union[str, float], unit: Optional[str] = ...
    ) -> None: ...
    def GetWearModel(self) -> str: ...
    def SetWearModel(self, value: str) -> None: ...
    def GetValidWearModelValues(self) -> List[str]: ...
    def GetMaterial(self): ...
    def SetMaterial(self, value) -> None: ...
    def GetAvailableMaterials(self): ...
