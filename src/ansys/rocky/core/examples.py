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
"""Helper module to download project code examples."""
import logging
import os
from typing import Optional

try:
    import requests
except ImportError:
    raise ImportError(
        "requests library is required to download examples data. Please install it with `pip install requests`"
    )

logger = logging.getLogger("pyrocky.networking")


ANSYS_EXAMPLE_DATA_REPO = "https://github.com/ansys/example-data/raw/master"


def _get_file_url(
    file_name: str,
    directory: Optional[str] = None,
    file_host: str = ANSYS_EXAMPLE_DATA_REPO,
) -> str:
    """Get a file using a URL.

    Parameters
    ----------
    file_name : str
        Name of the file.
    directory : str, optional
        Directory in the Ansys example data repository where the file is located.
        If a directory is not specified, this method looks for the file in the root
        directory of the repository.
    file_host : str, optional
        URL where the file is hosted. The default is ``ANSYS_EXAMPLE_DATA_REPO``.

    Returns
    -------
    str
        URL of the file.
    """
    if directory:
        return f"{file_host}/{directory}/{file_name}"
    return f"{file_host}/{file_name}"


def _retrieve_file(
    url: str,
    file_name: str,
    save_path: str,
) -> str:
    """Download a file using a URL.

    Parameters
    ----------
    url : str
        URL of the file.
    file_name : str
        Name of the file.
    save_path : str
        Path to download the file to.

    Returns
    -------
    str
        Path of the downloaded file.
    """
    file_name = os.path.basename(file_name)
    save_path = os.path.abspath(save_path)
    local_path = os.path.join(save_path, file_name)

    logger.info("File does not exist. Downloading specified file...")

    # Check if save path exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Download file
    logger.info(f'Downloading URL: "{url}"')
    content = requests.get(url).content
    with open(local_path, "wb") as f:
        f.write(content)

    print(f"Download successful. File path:\n{local_path}")
    logger.info("Download successful.")

    return local_path


def download_file(
    save_path: str,
    file_name: str,
    directory: Optional[str] = None,
) -> str:
    """Download an example file from the Ansys example data repository.

    Parameters
    ----------
    save_path : str
        Path to download the file to.
    file_name : str
        Name of the file.
    directory : str, optional
        Name of the directory in the Ansys example data repository where the file
        is located. If a directory is not specified, this method looks for the file
        in the root directory of the repository.


    Returns
    -------
    str
        Path of the downloaded file.

    Examples
    --------
    >>> from ansys.rocky.core.examples import download_file
    >>> file_path = download_file('<path_to_save>', 'bracket.iges', 'geometry')
    '<path_to_save>/bracket.iges'
    """

    url = _get_file_url(file_name, directory)
    return _retrieve_file(url, file_name, save_path)
