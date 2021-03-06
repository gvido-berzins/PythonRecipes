"""
Summary:
    Return the path object based on the currently used system
"""
import sys
from pathlib import Path, PosixPath, WindowsPath

path = "This/Is/Some OS Path/file.txt"


def main():
    if sys.platform.startswith("win"):
        path = WindowsPath(path)
    elif sys.platform.startswith("darwin") or sys.platform.startswith("linux"):
        path = PosixPath(path)
    else:
        raise Exception("Something went wrong")

    print(path)
    print(str(path))
    print(path.absolute())


if __name__ == "__main__":
    main()
