from pathlib import Path
import tempfile

from ansys.rocky.core import examples


def test_examples_download():
    # Create a temp directory to save the downloaded file.
    save_path = tempfile.mkdtemp(prefix="pyrocky_")

    file_name = "bracket.iges"

    file_path = examples.download_file(save_path, file_name, "geometry")

    file_path = Path(file_path)

    assert file_path == Path(save_path) / file_name
    assert file_path.is_file()
    assert file_path.exists()
