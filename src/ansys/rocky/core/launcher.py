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

import contextlib
import os
from pathlib import Path
import subprocess
import time
from typing import Optional

from Pyro5.errors import CommunicationError

from ansys.rocky.core.client import RockyClient, connect_to_rocky
from ansys.rocky.core.exceptions import RockyLaunchError


def launch_rocky(
    rocky_exe: Optional[Path] = None,
    headless: bool = True,
) -> RockyClient:
    """
    Launch Rocky executable with PyRocky server enabled, wait Rocky to start up and
    return a `RockyClient` instance.

    Parameters
    ----------
    rocky_exe : Optional[Path], optional
        Path to Rocky executable. If not specified, will try to find it in the
        environment variables `AWP_ROOT241` and `AWP_ROOT232`.
    headless : bool, optional
        Whether to launch Rocky in headless mode. Default is `True`.

    Returns
    -------
    RockyClient
        A `RockyClient` instance connected to the launched Rocky application.
    """
    if rocky_exe is None:
        for awp_root in ["AWP_ROOT241", "AWP_ROOT232"]:
            if awp_root not in os.environ:
                continue

            rocky_exe = Path(os.environ[awp_root]) / "Rocky/bin/Rocky.exe"
            if rocky_exe.is_file():
                break
        else:
            raise FileNotFoundError("Rocky executable not found")
    else:
        if not rocky_exe.is_file():
            raise FileNotFoundError(f"Rocky executable not found at {rocky_exe}")

    cmd = [rocky_exe, "--pyrocky"]
    if headless:
        cmd.append("--headless")
    with contextlib.suppress(subprocess.TimeoutExpired):
        rocky_process = subprocess.Popen(cmd)
        rocky_process.wait(timeout=3)

    # Rocky.exe call returned to soon, something happen
    if rocky_process.returncode is not None:
        raise RockyLaunchError(f"Error launching Rocky:\n  {' '.join(cmd)}")

    client = connect_to_rocky()

    # TODO: A more elegant way to find out that Rocky Pyro server started.
    for _ in range(_WAIT_ROCKY_START):
        try:
            client.api.GetProject()
        except CommunicationError:
            time.sleep(1)
        else:
            break
    else:
        raise RockyLaunchError("Could not connect Rocky remote server: timed out")

    client._process = rocky_process
    return client


_WAIT_ROCKY_START = 60
