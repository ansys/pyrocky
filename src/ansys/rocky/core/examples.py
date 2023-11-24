import logging
import os
from typing import Optional

import requests

logger = logging.getLogger("pyrocky.networking")


ANSYS_EXAMPLE_DATA_REPO = 'https://github.com/ansys/example-data/raw/master'

def _get_file_url(file_name: str, directory: Optional[str] = None) -> str:
    """Get file URL."""
    if directory:
        return (
            f"{ANSYS_EXAMPLE_DATA_REPO}/{directory}/{file_name}"
        )
    return f"{ANSYS_EXAMPLE_DATA_REPO}/{file_name}"


def _retrieve_file(
    url: str,
    file_name: str,
    save_path: str,
) -> str:
    """Download specified file from specified URL."""
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
    """Download specified example file from the Ansys example data repository.

    Parameters
    ----------
    save_path : str
        Path to download the specified file to.
    file_name : str
        File to download.
    directory : str, optional
        Ansys example data repository directory where specified file is located. If not
        specified, looks for the file in the root directory of the repository.


    Returns
    -------
    str
        file path of the downloaded file.

    Examples
    --------
    >>> from ansys.rocky.core.examples import download_file
    >>> file_path = download_file('<path_to_save>', 'bracket.iges', 'geometry')
    '<path_to_save>/bracket.iges'
    """

    url = _get_file_url(file_name, directory)
    return _retrieve_file(url, file_name, save_path)
