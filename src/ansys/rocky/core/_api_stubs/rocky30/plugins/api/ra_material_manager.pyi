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

from rocky30.models.material.fluid_material import (
    FluidMaterialCollection as FluidMaterialCollection,
)
from rocky30.models.material.material import Material as Material
from rocky30.models.material.material import MaterialCollection as MaterialCollection
from rocky30.models.material.materials_interaction import (
    MaterialsInteraction as MaterialsInteraction,
)

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_fluid_material import (
    RAFluidMaterial as RAFluidMaterial,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_collection import (
    RAMaterialCollection as RAMaterialCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_interaction import (
    RAMaterialsInteraction as RAMaterialsInteraction,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAMaterialManager:
    @classmethod
    def CreateMaterialAndRelatedInteractions(
        cls,
        materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection],
        interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction],
        material_name: Union[str, None] = ...,
    ) -> Material: ...
    @classmethod
    def CreateSolidMaterialAndRelatedInteractions(
        cls,
        materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection],
        interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction],
        material_name: Union[str, None] = ...,
    ) -> Material: ...
    @classmethod
    def RemoveMaterialAndRelatedInteractions(
        cls,
        materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection],
        interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction],
        material_or_name: Union[str, Material],
    ) -> None: ...
    @classmethod
    def RemoveSolidMaterialAndRelatedInteractions(
        cls,
        materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection],
        interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction],
        material_or_name: Union[str, Material],
    ) -> None: ...
    @classmethod
    def CreateFluidMaterial(
        cls,
        fluid_material_collection: FluidMaterialCollection,
        material_name: Union[str, None] = ...,
    ) -> RAFluidMaterial: ...
    @classmethod
    def RemoveFluidMaterial(
        cls,
        fluid_material_collection: FluidMaterialCollection,
        material_or_name: Union[str, RAFluidMaterial],
    ) -> None: ...
