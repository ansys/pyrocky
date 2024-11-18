from ben10.foundation.decorators import Override as Override
from rocky30.models.geometry.conveyors.conveyor_belt_profile import BELT_PROFILE_STRING_TO_CAPTION as BELT_PROFILE_STRING_TO_CAPTION, BeltProfileCaptionFromString as BeltProfileCaptionFromString, BeltProfileStringFromCaption as BeltProfileStringFromCaption, SetupNewBeltProfile as SetupNewBeltProfile
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_base_geometry import RABaseGeometry as RABaseGeometry

class RABaseConveyor(RABaseGeometry):
    def GetBeltProfileName(self): ...
    def GetBeltProfile(self): ...
    def SetBeltProfile(self, belt_profile_name): ...
    def GetValidBeltProfileNames(self): ...
