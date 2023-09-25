import contextlib
import os
from pathlib import Path
import subprocess
import time
from typing import Optional

from Pyro5.errors import CommunicationError

from ansys.rocky.prepost.client import RockyClient, connect_to_rocky
from ansys.rocky.prepost.exceptions import PyRockyError


def launch_rocky(
    rocky_exe: Optional[Path] = None,
    headless: bool = True,
) -> RockyClient:
    """
    Launch Rocky executable with PyRocky server enabled, wait Rocky to start up and
    return a `RockyClient` instance.
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


class RockyLaunchError(PyRockyError):
    """Raised for errors occurred during Rocky application launch"""
