# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

from typing import Iterable

from rocky30.models.sph.sph_refinement_criteria import (
    ROIRefinementItem as ROIRefinementItem,
)
from rocky30.models.sph.sph_refinement_criteria import (
    ROIRefinementItemList as ROIRefinementItemList,
)
from rocky30.models.sph.sph_refinement_criteria import (
    SPHRefinementCriteria as SPHRefinementCriteria,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.conveyors.ra_feed_conveyor import RAFeedConveyor as RAFeedConveyor
from ansys.rocky.app.conveyors.ra_receiving_conveyor import (
    RAReceivingConveyor as RAReceivingConveyor,
)
from ansys.rocky.app.ra_list import RAList as RAList
from ansys.rocky.app.ra_region_of_interest_cube import (
    RARegionOfInterestCube as RARegionOfInterestCube,
)
from ansys.rocky.app.ra_region_of_interest_cylinder import (
    RARegionOfInterestCylinder as RARegionOfInterestCylinder,
)
from ansys.rocky.app.ra_system_coupling_wall import (
    RASystemCouplingWall as RASystemCouplingWall,
)
from ansys.rocky.app.ra_wall import RAWall as RAWall

class RARoiRefinementItem(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for one Adaptive SPH Sizing ROI refinement row.

    This wrapper corresponds to one item inside
    ``RASphAdaptiveSizing.RARoiRefinementItemList``.

    Access individual roi level via a :class:`RASphAdaptiveSizing`'s roi level list:

    .. code-block:: python

        roi_ref_levels = sph_adaptive_sizing.GetRoiRefinementLevels()
        roi_level_1 = roi_ref_levels[0]
        roi_level_2 = roi_ref_levels.New()

    Every :class:`RARoiRefinementItem` contains two properties that define a ROI refinement level:
    the Region of Interest and the level value:

    .. code-block:: python

        roi_level = roi_ref_levels.New()
        roi_level.SetRoi('MyRoiCube')
        roi_level.SetLevelOfRefinement(2)

    """

    @classmethod
    def GetWrappedClass(cls) -> type[ROIRefinementItem]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetLevelOfRefinement(self) -> int:
        """
        Get the value of "Level of Refinement".

        """

    def SetLevelOfRefinement(self, value: str | int) -> None:
        """
        Set the value of "Level of Refinement".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetRoi(self) -> None | RARegionOfInterestCube | RARegionOfInterestCylinder:
        """
        Get the "Roi".

        :rtype: :class:`RARegionOfInterestCube`, :class:`RARegionOfInterestCylinder`
        """

    def SetRoi(
        self, value: str | RARegionOfInterestCube | RARegionOfInterestCylinder
    ) -> None:
        """
        Set the "Roi".

        :param unicode, :class:`RARegionOfInterestCube`, :class:`RARegionOfInterestCylinder` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableRois(
        self,
    ) -> list[RARegionOfInterestCube | RARegionOfInterestCylinder]:
        """
        Get all available Rois.

        :rtype: List[:class:`RARegionOfInterestCube`, :class:`RARegionOfInterestCylinder`]
            A list of :class:`RARegionOfInterestCube`, :class:`RARegionOfInterestCylinder`.
        """

class RARoiRefinementItemList(RAList[RARoiRefinementItem]):
    """
    Rocky PrePost Scripting wrapper for the Adaptive SPH Sizing ROI refinement table.

    To get the :class:`RARoiRefinementItemList` from a :class:`RASphAdaptiveSizing`, use:

    .. code-block:: python

        roi_ref_levels = sph_adaptive_sizing.GetRoiRefinementLevels()

    The :class:`RARoiRefinementItemList` class acts as a regular Python list, with the usual methods to iterate
    and access individual motions:

    .. code-block:: python

        roi_level_1 = roi_ref_levels.New()
        roi_level_2 = roi_ref_levels.New()

        for roi_level in roi_ref_levels:
            roi_level.SetLevelOfRefinement(2)

        del roi_ref_levels[0]
        roi_ref_levels.Clear()

    The items in the roi level list are of type :class:`RARoiRefinementItem`.
    """

    @classmethod
    def GetWrappedClass(cls) -> type[ROIRefinementItemList]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def New(self, index: int | None = None) -> RARoiRefinementItem:
        """
        Add a new ROI refinement row.

        :param index:
            Optional insertion index.
        """

class RASphAdaptiveSizing(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for the SPH Adaptive Sizing.

    .. code-block:: python

        sph_settings = study.GetSphSettings()
        sph_adaptive_sizing = sph_settings.GetAdaptiveSizing()

    """

    @classmethod
    def GetWrappedClass(self) -> type[SPHRefinementCriteria]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetGeometries(
        self,
    ) -> list[RAWall | RAFeedConveyor | RAReceivingConveyor | RASystemCouplingWall]:
        """
        Get the "Adaptive Sph Sizing Geometries".

        :rtype: List[:class:`RAWall`, :class:`RAFeedConveyor`, :class:`RAReceivingConveyor`, :class:`RASystemCouplingWall`]
            A list of :class:`RAWall`, :class:`RAFeedConveyor`, :class:`RAReceivingConveyor`, :class:`RASystemCouplingWall`.
        """

    def SetGeometries(
        self,
        values: Iterable[
            RAWall | RAFeedConveyor | RAReceivingConveyor | RASystemCouplingWall | str
        ],
    ) -> None:
        """
        Set the "Adaptive Sph Sizing Geometries".

        :param List[str, :class:`RAWall`, :class:`RAFeedConveyor`, :class:`RAReceivingConveyor`, :class:`RASystemCouplingWall`] values:
            A list with names, :class:`RAWall`, :class:`RAFeedConveyor`, :class:`RAReceivingConveyor`, :class:`RASystemCouplingWall`.
        """

    def GetAvailableGeometries(
        self,
    ) -> list[RAWall | RAFeedConveyor | RAReceivingConveyor | RASystemCouplingWall]:
        """
        Get all available Adaptive Sph Sizing Geometries.

        :rtype: List[:class:`RAWall`, :class:`RAFeedConveyor`, :class:`RAReceivingConveyor`, :class:`RASystemCouplingWall`]
            A list of :class:`RAWall`, :class:`RAFeedConveyor`, :class:`RAReceivingConveyor`, :class:`RASystemCouplingWall`.
        """

    def GetRoiRefinementLevels(self) -> RARoiRefinementItemList:
        """
        Get the Adaptive SPH Sizing ROI refinement levels table.
        """

    def GetEnabled(self) -> bool:
        """
        Get the value of "Enabled".

        """

    def SetEnabled(self, value: bool) -> None:
        """
        Set the value of "Enabled".

        :param value:
            The value to set.
        """

    def Enable(self) -> None:
        """
        Set the value of "" to True.
        """

    def Disable(self) -> None:
        """
        Set the value of "" to False.
        """

    def IsEnabled(self) -> bool:
        """
        Check if the "" is enabled.

        """

    def GetGeometriesLevelOfRefinement(self) -> int:
        """
        Get the value of "Geometries Level of Refinement".

        """

    def SetGeometriesLevelOfRefinement(self, value: str | int) -> None:
        """
        Set the value of "Geometries Level of Refinement".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetGeometriesRefinementDistanceFactor(self) -> float:
        """
        Get the value of "Geometries Refinement Distance Factor".

        """

    def SetGeometriesRefinementDistanceFactor(self, value: str | float) -> None:
        """
        Set the value of "Geometries Refinement Distance Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """
