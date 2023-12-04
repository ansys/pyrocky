from pathlib import Path
import subprocess
import sys

import pytest

EXAMPLES_DIR = Path(__file__).parent / "basic_examples"
EXAMPLE_FILES = EXAMPLES_DIR


@pytest.mark.parametrize("example_path", list(EXAMPLE_FILES.glob("*.py")))
def test_examples(example_path: Path) -> None:
    subprocess.check_call([sys.executable, str(example_path.absolute())])
