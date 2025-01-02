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

from typing import Union

from rocky30.plugins.sph.calculations.tagging.sph_tagging_calculator import (
    SPHTaggingCalculator as SPHTaggingCalculator,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_tagging import (
    RABaseTagging as RABaseTagging,
)

class RASPHTagging(RABaseTagging):
    @classmethod
    def GetWrappedClass(self) -> type[SPHTaggingCalculator]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetNameMask(self) -> str: ...
    def SetNameMask(self, value: str) -> None: ...
    def GetTagValue(self) -> int: ...
    def SetTagValue(self, value: Union[str, int]) -> None: ...
