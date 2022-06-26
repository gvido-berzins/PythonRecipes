"""
Summary:
    Simple docker wrapper example
Description:
    Idea taken from Anthony Sottile video https://github.com/anthonywritescode
"""
import os
import sys


def main() -> int:
    cmd = (
        "docker",
        "run",
        "-e",
        f"HOST_USER={os.getuid()}",
        "-e",
        f"HOST_GROUP={os.getgid()}",
        *sys.argv[1:],
    )
    os.execvp(cmd[0], cmd)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
