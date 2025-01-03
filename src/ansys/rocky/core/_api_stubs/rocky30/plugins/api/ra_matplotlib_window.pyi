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

from _typeshed import Incomplete
from coilib50.subject import Subject
from esss_qt10 import qt_traits
from kraken20.plugins.api.ka_workspace_window import KAWorkspaceWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D as Axes3D
from plugins10.plugins.mainwindow.mainwindowplugins.centralwidget import (
    DefaultCentralEditor,
)
from plugins10.plugins.workspace.workspace_editor_subjects.workspace_editor_subjects import (
    WorkspaceEditorSubject,
)

class MplCanvas(FigureCanvas):
    figure: Incomplete
    def __init__(self) -> None: ...

class MplWindow(qt_traits.QWidget, DefaultCentralEditor):
    frame: Incomplete
    canvas: Incomplete
    mpltoolbar: Incomplete
    vbl: Incomplete
    def __init__(self, parent, central_editor_id) -> None: ...
    def GetFigure(self): ...

class MplWindowSubject(WorkspaceEditorSubject):
    def GetGUIClass(self): ...
    def GetIgnoreChanges(self): ...
    def GetIgnoreAddRemove(self): ...
    def GetIgnoreAdd(self): ...

class RAMplWindow(KAWorkspaceWindow):
    def GetFigure(self): ...
    def GetCanvas(self): ...
    def Redraw(self): ...

class UserWindowSubjectContainer(Subject):
    app: Incomplete
    def __init__(self, app) -> None: ...
    def GetIgnoreChanges(self): ...
    def GetIgnoreAddRemove(self): ...
    def GetIgnoreAdd(self): ...
    def Add(self, window_subject): ...
    def __iter__(self): ...
