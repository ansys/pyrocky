from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_point_cloud import RAPointCloud as RAPointCloud

class RAPointCloudCollection(RAList[RAPointCloud]):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
