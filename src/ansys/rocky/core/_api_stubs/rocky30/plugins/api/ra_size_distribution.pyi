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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RASizeDistribution(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a single entry in a single Particle's size distribution list.

    Access this wrapper from a given :class:`RAParticle` with:

    .. code-block:: python

        size_distribution_list = particle.GetSizeDistributionList()
        distribution_1 = size_distribution_list.New()
        distribution_1.SetSize(1.0, 'm')
        distribution_1.SetCumulativePercentage(100)
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetCumulativePercentage(self) -> float:
        """
        Get the value of "Cumulative Percentage".

        """

    def SetCumulativePercentage(self, value: str | float) -> None:
        """
        Set the value of "Cumulative Percentage".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetScaleFactor(self, unit: str | None = None) -> float:
        """
        Get the value of "Scale Factor".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetScaleFactor(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Scale Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetSize(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

class RASizeDistributionList(RAList[RASizeDistribution]):
    """
    Rocky PrePost Scripting wrapper to manipulate the size properties in a single Particle.

    To get the :class:`RASizeDistributionList` from a :class:`RAParticle`, use:

    .. code-block:: python

        size_distribution_list = particle.GetSizeDistributionList()

    :class:`RASizeDistributionList` contains methods to set the size type and add, remove and
    retrieve individual size distribution entries. It corresponds to the items on a Particle\'s
    "Size" tab on the Rocky UI.

    The following examples add, remove and access individual entries in the size distribution list:

    .. code-block:: python

        # Add new items
        size_distribution = size_distribution_list.New()

        # Access and modify items
        size_distribution = size_distribution_list[0]
        size_distribution.SetSize(1.0, \'m\')

        # Remove items
        size_distribution_list.Remove(size_distribution)
        del size_distribution_list[0]
        size_distribution_list.Clear()

    Note that this list is used even if the configured particle only has a single size, such as when
    it is composed of Multiple Elements. In these cases, the single size refers to the first item
    on the list (and no other items are used).

    The :class:`RASizeDistributionList` is a list of :class:`RASizeDistribution`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetCgmScaleFactor(self) -> float:
        """
        Get the value of "Cgm Scale Factor".

        """

    def SetCgmScaleFactor(self, value: str | float) -> None:
        """
        Set the value of "Cgm Scale Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSizeType(self) -> str:
        """
        Get "Size Type" as a string.

        :return:
            The returned value will be one of [\'sieve\', \'equivalent_diameter\', \'original_size_scale\'].
        """

    def SetSizeType(self, value: str) -> None:
        """
        Set the value of "Size Type".

        :param value:
            The value to set. Must be one of [\'sieve\', \'equivalent_diameter\', \'original_size_scale\'].
        :raises RockyApiError:
            If `value` is not a valid "Size Type" option.
        """

    def GetValidSizeTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Size Type".

        :return:
            The returned list is [\'sieve\', \'equivalent_diameter\', \'original_size_scale\'].
        """
