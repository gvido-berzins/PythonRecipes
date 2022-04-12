"""
Summary:
    Testing Python zip and unzip functionality
References: |
    - [Python docs](https://docs.python.org/3/library/zipfile.html)
"""
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ZIP_PATH = Path("wut.zip")
OUT_DIR = SCRIPT_DIR / "out"


def add_python_files_to_zip(zf: zipfile.ZipFile):
    for path in SCRIPT_DIR.glob("*"):
        if path.name.endswith(".py"):
            zf.write(path)


def show_members(zf: zipfile.ZipFile):
    for member in zf.namelist():
        print(member)


def main():
    zf = zipfile.ZipFile(ZIP_PATH, "w")
    add_python_files_to_zip(zf)

    zf.extractall(OUT_DIR)

    show_members(zf)


if __name__ == "__main__":
    main()
