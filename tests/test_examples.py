import os
from pathlib import Path
import subprocess
import sys

import pytest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES_DIR = Path(os.path.join(ROOT_DIR, "examples"))

@pytest.mark.parametrize("example_path", list(EXAMPLES_DIR.rglob("*.py")))
def test_examples(example_path: Path) -> None:
    subprocess.check_call([sys.executable, str(example_path.absolute())])
