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
import sys

import pytest

import ansys.rocky.core as pyrocky

VERSION = int(os.getenv("ANSYS_VERSION", "261"))
RUN_DOCKER_TESTS = int(os.getenv("RUN_DOCKER_TESTS", "0"))

if not RUN_DOCKER_TESTS or VERSION != 261 or sys.platform == "win32":
    pytest.skip(
        "Docker tests must be explicitly enabled by setting RUN_DOCKER_TESTS=1"
        " and only supports Ansys version 26.1.0 in linux for now.",
        allow_module_level=True,
    )


@pytest.mark.parametrize("variant", ["freeflow", "rocky"])
def test_launch_container(variant, request):
    """
    Minimal test to check if it is possible to launch a Rocky and Freeflow container
    and communicate with it.
    """
    client = pyrocky.launch_container(variant)
    request.addfinalizer(client.close)

    project = client.api.CreateProject()

    study = project.GetStudy()
    assert study is not None
