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

from collections.abc import Iterable

from rocky30.plugins.preferences.additional_features import (
    AdditionalFeature as AdditionalFeature,
)
from rocky30.plugins.preferences.additional_features import (
    GetAdditionalFeatureValue as GetAdditionalFeatureValue,
)
from rocky30.plugins.preferences.additional_features import (
    SetAdditionalFeatureValue as SetAdditionalFeatureValue,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_project import (
    RAProject as RAProject,
)

class RAAdditionalFeatures:
    def GetBetaFeaturesEnabled(self) -> bool:
        """
        Get whether 'beta features' are enabled in the application preferences.
        """

    def SetBetaFeaturesEnabled(self, enable: bool) -> None:
        """
        Set whether 'beta features' are enabled in the application preferences.
        """

    def GetAdvancedFeaturesEnabled(self) -> bool:
        """
        Get whether 'advanced features' are enabled in the application preferences.
        """

    def SetAdvancedFeaturesEnabled(self, enable: bool) -> None:
        """
        Set whether 'advanced features' are enabled in the application preferences.
        """

    def GetCustomFeatures(self) -> list[str]:
        """
        Get a list with all enabled features in application preferences.
        """

    def SetCustomFeatures(self, features: Iterable[str]) -> None:
        """
        Use a list of custom features to enable them in the application preferences.

        :param features:
            A list of names that represents the custom features.
        """
