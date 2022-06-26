import sys
from argparse import ArgumentParser
from multiprocessing import Process
from pathlib import Path
from typing import List, Tuple

from config import settings

SUPPORTED_EXTS = [".yml", ".yaml"]

OverwriteType = Tuple[str, str]


def path_type(path_str: str) -> Path:
    path = Path(path_str)
    if not path.exists():
        sys.exit(f"No such file exists: '{path}'")

    if path.suffix not in SUPPORTED_EXTS:
        sys.exit(f"Only {SUPPORTED_EXTS} extension is supported: '{path}'")

    return path


def overwrite_type(arg: str, sep="=") -> OverwriteType:
    if sep not in arg:
        sys.exit(f"overwrite: Separator must be included '{sep}'. Given: '{arg}'")

    key, value = arg.split(sep)
    if not key.strip() or not value.strip():
        sys.exit(f"overwrite: Key and Value must not be empty. Given: '{arg}'")

    if "@" not in value:
        value += "@str"

    value, tmp_type = value.split("@")
    match tmp_type:
        case "int":
            value = int(value)
        case "float":
            value = float(value)
        case "str":
            ...
        case _:
            sys.exit(f"overwrite: Unrecognized type '{tmp_type}'")

    return key, value


def parse_args(args: List[str]):
    parser = ArgumentParser()
    parser.add_argument(
        "-o",
        action="extend",
        nargs="+",
        type=overwrite_type,
        help="Overwrites for the configuration",
    )
    return parser.parse_args(args)


def overwrite_settings(overwrites: List[OverwriteType]):
    for overwrite in overwrites:
        key, value = overwrite
        set_value = settings.get(key)
        if not set_value:
            print(f"overwrite: No such key '{key}'")
        else:
            print(f"overwrite: Settting '{key}' = {value!r}")
            settings.set(key, value)


def server():
    print("Running server in a new thread")
    print(f"settings: Other thread: {settings.get('server')}")
    print()
    print("Forced types are possible")
    port = settings.as_int("server.port")
    print(f"Raw port: {port!r}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    # Can overwrite the default configuration
    overwrite_settings(args.o)
    print(f"settings: Main thread: {settings.get('server')}")

    # Even saves the state in a child process
    Process(target=server).start()

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
