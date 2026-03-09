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

from kraken20.plugins.api.ka_workspace_window import KAWorkspaceWindow

from ansys.rocky.app.ra_contacts_data_mesh_coloring import (
    RAContactsDataMeshColoring as RAContactsDataMeshColoring,
)
from ansys.rocky.app.ra_joints_data_mesh_coloring import (
    RAJointsDataMeshColoring as RAJointsDataMeshColoring,
)
from ansys.rocky.app.ra_mesh_coloring import RAMeshColoring as RAMeshColoring

ColorType = tuple[float, float, float]

class _RASubjectWithColoringMixin:
    """
    Mixin to be used for RASubjects that can have coloring.
    """

    def GetMeshColoring(self, window: str | KAWorkspaceWindow) -> RAMeshColoring:
        """
        Get the RAMeshColoring related to the current object and a window.

        :param window:
            The window that the coloring is acting. The window must be a str of the name of the
            window or a KAWorkspaceWindow.
        :raises RockyApiError:
            If window is not a str or KAWorkspaceWindow. Additionally, raises an error if no window
            is found or no coloring for the given item exists.

        """
