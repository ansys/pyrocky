from rocky30.models.material.fluid_material import FluidMaterialCollection as FluidMaterialCollection
from rocky30.models.material.material import Material as Material, MaterialCollection as MaterialCollection
from rocky30.models.material.materials_interaction import MaterialsInteraction as MaterialsInteraction
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_fluid_material import RAFluidMaterial as RAFluidMaterial
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_collection import RAMaterialCollection as RAMaterialCollection
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_materials_interaction import RAMaterialsInteraction as RAMaterialsInteraction
from ansys.rocky.core._api_stubs.rocky30.plugins.api.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

class RAMaterialManager:
    @classmethod
    def CreateMaterialAndRelatedInteractions(cls, materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection], interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction], material_name: Union[str, None] = ...) -> Material: ...
    @classmethod
    def CreateSolidMaterialAndRelatedInteractions(cls, materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection], interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction], material_name: Union[str, None] = ...) -> Material: ...
    @classmethod
    def RemoveMaterialAndRelatedInteractions(cls, materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection], interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction], material_or_name: Union[str, Material]) -> None: ...
    @classmethod
    def RemoveSolidMaterialAndRelatedInteractions(cls, materials_api_or_subject: Union[RAMaterialCollection, MaterialCollection], interactions_api_or_subject: Union[RAMaterialsInteraction, MaterialsInteraction], material_or_name: Union[str, Material]) -> None: ...
    @classmethod
    def CreateFluidMaterial(cls, fluid_material_collection: FluidMaterialCollection, material_name: Union[str, None] = ...) -> RAFluidMaterial: ...
    @classmethod
    def RemoveFluidMaterial(cls, fluid_material_collection: FluidMaterialCollection, material_or_name: Union[str, RAFluidMaterial]) -> None: ...
