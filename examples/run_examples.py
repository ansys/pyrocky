import os.path
from pathlib import Path
import subprocess
import sys


def run_examples() -> None:
    path = Path(os.path.realpath(__file__))
    examples_path = path.parent
    example_files = list(examples_path.rglob("*.py"))
    example_files.remove(path)

    example_failed = False
    for f in example_files:
        try:
            subprocess.run(["python", f], check=True)
        except subprocess.CalledProcessError:
            print(f"Example has failed: {f.name}")
            example_failed = True

    if example_failed:
        sys.exit(1)


if __name__ == "__main__":
    run_examples()
