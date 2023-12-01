import os.path
from pathlib import Path
import shutil
import sys


def compress_doc(name: str) -> None:
    path = Path(os.path.realpath(__file__))
    doc_build_path = path.parent / "_build/html"

    shutil.make_archive(name, "zip", doc_build_path)


if __name__ == "__main__":
    name = sys.argv[1]
    compress_doc(name)
