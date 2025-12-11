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

from rocky30.models.material.fluid_material import (
    FluidMaterialCollection as FluidMaterialCollection,
)
from rocky30.models.material.fluid_material import FluidMaterial as FluidMaterial
from rocky30.models.material.material import Material as Material
from rocky30.models.material.material import MaterialCollection as MaterialCollection
from rocky30.models.naming import CreateNewName as CreateNewName

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_fluid_material import (
    RAFluidMaterial as RAFluidMaterial,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_interaction_collection import (
    RAMaterialsInteractionCollection as RAMaterialsInteractionCollection,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_solid_material import (
    RASolidMaterial as RASolidMaterial,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import (
    ApiDeprecated as ApiDeprecated,
)

class RAMaterialCollection(RAList):
    """
    Rocky PrePost Scripting wrapper for the collection of materials in a project.

    This wrapper corresponds to the "Materials" item on the project\'s data tree. Retrieve the
    :class:`RAMaterialCollection` from a :class:`RAStudy` via:

    .. code-block:: python

        material_collection = study.GetMaterialCollection()

    Instances of the :class:`RAMaterialCollection` class act as regular Python lists and can be
    iterated on, individual materials accessed and deleted via index, etc:

    .. code-block:: python

        material_1 = material_collection.AddSolidMaterial()
        material_2 = material_collection.AddFluidMaterial()
        material_2 = material_collection[3]
        del material_collection[2]

    Items in this list are of type :class:`RASolidMaterial` and :class:`RAFluidMaterial`.
    """

    @classmethod
    def GetWrappedClass(cls) -> type["MaterialCollection"]: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def __delitem__(self, index: int) -> None: ...
    def Remove(self, item: ApiElementItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> ApiElementItem: ...
    def __getitem__(self, index: int) -> ApiElementItem: ...
    def Clear(self) -> None: ...
    def New(self) -> RASolidMaterial:
        """
        Deprecated: Use :meth:`Add{Solid, Fluid}Material()` instead.
        """

    def AddSolidMaterial(self, name: str | None = None) -> RASolidMaterial: ...
    def AddFluidMaterial(self, name: str | None = None) -> RAFluidMaterial: ...
    def GetDefaultSolidMaterials(self) -> list["RASolidMaterial"]:
        """
        Get a list with the default solid materials, in order of Particle, Belt and Boundary.
        """

    def GetDefaultParticleMaterial(self) -> RASolidMaterial: ...
    def GetDefaultBeltMaterial(self) -> RASolidMaterial: ...
    def GetDefaultBoundaryMaterial(self) -> RASolidMaterial: ...
    def GetSolidMaterial(self, material_name: str) -> RASolidMaterial:
        """
        Get the solid material with the given name.
        """

    def GetDefaultFluidMaterial(self) -> RAFluidMaterial: ...
    def GetFluidMaterial(self, material_name: str) -> RAFluidMaterial:
        """
        Get the fluid material with the given name.
        """

    def GetMaterialsInteractionCollection(self) -> RAMaterialsInteractionCollection:
        """
        Get the study's Materials Interaction Collection.
        """

    def GetBulkSolidFraction(self) -> float:
        """
        Get the value of "Bulk Solid Fraction".

        """

    def SetBulkSolidFraction(self, value: str | float) -> None:
        """
        Set the value of "Bulk Solid Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """
