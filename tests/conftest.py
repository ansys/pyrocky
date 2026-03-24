# Copyright (C) 2023 - 2026 ANSYS, Inc. and/or its affiliates.
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

import os

import pytest

import ansys.rocky.core as pyrocky


@pytest.fixture(scope="session")
def version() -> int:
    return int(os.getenv("ANSYS_VERSION", "261"))


@pytest.fixture(scope="module")
def rocky_session(version):
    rocky = pyrocky.launch_rocky(rocky_version=version, headless=False, server_port=22039)
    yield rocky
    rocky.close()


@pytest.fixture()
def freeflow_session(version):
    freeflow = pyrocky.launch_freeflow(freeflow_version=version)
    yield freeflow
    freeflow.close()


@pytest.fixture()
def rocky_api(rocky_session):
    yield rocky_session.api
    if rocky_session.api.GetProject() is not None:
        # Make sure "Exit" won't be blocked by the "Unsaved Changes" dialog.
        rocky_session.api.CloseProject(check_save_state=False)
