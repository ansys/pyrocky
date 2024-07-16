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

from _typeshed import Incomplete
from coilib50.element_function.semantic_association import (
    SemanticAssociation as SemanticAssociation,
)
from coilib50.units import IQuantity as IQuantity
from coilib50.units import Quantity as Quantity

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)

VALID_TYPES: Incomplete
VALID_SCOPE: Incomplete

class RACustomCurveAndGridProperty:
    def AddCustomCurve(
        self,
        name: str,
        curve_type: str = ...,
        output_unit: str = ...,
        domain: str = ...,
        scope: str = ...,
        associations: Union[dict[str, str], None] = ...,
        expression: str = ...,
    ) -> None: ...
    def EditCustomCurve(
        self,
        edit_curve: str,
        new_name: Union[str, None] = ...,
        associations: Union[dict[str, str], None] = ...,
        expression: Union[str, None] = ...,
    ) -> None: ...
    def RemoveCustomCurve(self, name: str) -> None: ...
    def AddCustomProperty(
        self,
        name: str,
        property_type: str = ...,
        output_unit: str = ...,
        scope: str = ...,
        associations: Union[dict[str, str], None] = ...,
        expression: str = ...,
    ) -> None: ...
    def EditCustomProperty(
        self,
        edit_property: str,
        new_name: Union[str, None] = ...,
        associations: Union[dict[str, str], None] = ...,
        expression: Union[str, None] = ...,
    ) -> None: ...
    def RemoveCustomProperty(self, name: str) -> None: ...
