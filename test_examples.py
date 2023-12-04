from pathlib import Path
import subprocess
import sys

import pytest

EXAMPLES_DIR = Path(__file__).parent / "examples"


@pytest.mark.parametrize("example_path", list(EXAMPLES_DIR.glob("*.py")))
def test_examples(example_path: Path) -> None:
    subprocess.check_call([sys.executable, str(example_path.absolute())])
