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

import argparse
from pathlib import Path
import re
import subprocess
import sys


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=("Build a docker image for Rocky or FreeFlow."),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-t",
        "--tag",
        required=True,
        help="Tag in the form <product>:<version> (e.g. rocky:24.1.0)",
    )
    parser.add_argument(
        "-f", "--dockerfile", help="Path to the Dockerfile to use for building the image."
    )
    parser.add_argument(
        "-n",
        "--network",
        default=None,
        help="Optional network mode to pass to `docker build`"
        " (e.g. host, none, bridge, <network-name>).",
    )

    return parser.parse_args()


def _compute_version_number(version: str) -> str:
    """Computes the Ansys version as <major><minor> (e.g. 24.1.0 -> 241)"""
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if not m:
        raise ValueError(f"version must be <major>.<minor>.<patch> (got: {version})")
    major, minor, _patch = m.groups()
    return f"{major}{minor}"


def build_docker_image() -> int:
    """
    Build a docker image for Rocky or FreeFlow.
    """
    args = _parse_args()
    product, version = args.tag.split(":")

    if product not in ("rocky", "freeflow"):
        raise ValueError(f"product must be 'rocky' or 'freeflow' (got: {product})")

    version_number = _compute_version_number(version)
    ansys_install_dir = Path("/ansys_inc") / f"v{version_number}"

    if args.dockerfile:
        dockerfile_path = Path(args.dockerfile)
    else:
        # Use the default Dockerfile in the repository if not provided via arguments.
        dockerfile_path = Path(__file__).parent / version_number / product / "Dockerfile"

    if not dockerfile_path.is_file():
        raise FileNotFoundError(f"Dockerfile not found: {dockerfile_path}")

    if not ansys_install_dir.is_dir():
        raise FileNotFoundError(
            f"Ansys installation directory not found: {ansys_install_dir}"
        )

    cmd = [
        "docker",
        "build",
        "--tag",
        f"{product}:{version}",
        "--file",
        str(dockerfile_path.resolve()),
    ]

    if args.network:
        # Might be needed for WSL
        cmd.extend(["--network", args.network])

    cmd.append(".")

    try:
        subprocess.run(cmd, cwd=str(ansys_install_dir), check=True)
        return 0
    except subprocess.CalledProcessError as e:
        return e.returncode


if __name__ == "__main__":
    sys.exit(build_docker_image())
