from kraken20.plugins.api.ka_workspace_window import KAWorkspaceWindow
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_contacts_data_mesh_coloring import RAContactsDataMeshColoring as RAContactsDataMeshColoring
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_joints_data_mesh_coloring import RAJointsDataMeshColoring as RAJointsDataMeshColoring
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_mesh_coloring import RAMeshColoring as RAMeshColoring

ColorType = tuple[float, float, float]

class _RASubjectWithColoringMixin:
    def GetMeshColoring(self, window: Union[str, type['KAWorkspaceWindow']]) -> RAMeshColoring: ...
