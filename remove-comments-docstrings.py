"""
Summary:
    Remove all comments and docstrings from a Python file
Description:
    Thanks to StackOverflow user SurpriseDog, https://stackoverflow.com/a/56285204
    for the strip function
Disclaimer:
    Currently will break a mutli-line docstring, example `f-string.py`,
    the error will be "Unterminated string literal"
"""
import ast
import re
import sys
from argparse import ArgumentParser
from pathlib import Path

import astunparse

EXCLUDE_DIRS = ["venv", "dist", "build"]
MODULE_PATH = Path(__file__).resolve()


def parse_args():
    parser = ArgumentParser(
        description="Remove all comments and docstrings from a python file"
    )
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit("\n! No arguments provided.")

    parser.add_argument(
        "-i",
        "--inplace",
        action="store_true",
        default=False,
        help="Overwrite the files",
    )
    subparsers = parser.add_subparsers(dest="action")

    recur = subparsers.add_parser(
        "recursive", help="Recursivelly change files by a regex pattern"
    )
    recur.add_argument(
        "patterns", nargs="*", help="Regex pattern for python files", default=[".*[.]py"]
    )

    files = subparsers.add_parser("files")
    files.add_argument("files", nargs="+", type=Path, help="List of files to change")
    return parser.parse_args()


def get_stripped_contents(path: Path) -> str:
    """Parse the abstract syntax tree and return file contents excluding
    comments and docstrings"""
    results = []
    try:
        with path.open("r") as f:
            lines = astunparse.unparse(ast.parse(f.read())).split("\n")
            for line in lines:
                if line.lstrip()[:1] not in ("'", '"'):
                    results.append(line)
    except SyntaxError:
        print(f"{path} Syntax error. Code might be broken.")
        return path.read_text("utf-8")
    except AttributeError:
        print(f"{path} Something went wrong. Attribut error.")
        return path.read_text("utf-8")
    return "\n".join(results)


def overwrite_file(file: Path, contents: str) -> None:
    """Overwrite file contents if they are changed"""
    before_contents = file.read_text()
    if before_contents != contents:
        file.write_text(contents)
        print(f"{file}: File contents overwritten")
    else:
        print(f"{file}: Nothing changed")


def validate_path(path: Path) -> bool:
    """Check if the path directories contain a blacklisted directory name
    and if the currently running script, has the same path as the target script"""
    path = path.resolve()
    path_parts = path.parts
    for dir in EXCLUDE_DIRS:
        if dir in path_parts:
            return False
    if path == MODULE_PATH:
        return False
    return True


def strip_files(files: list[Path], inplace: bool = False) -> None:
    """Strip comments/docstrings for all given file Path objects"""
    for file in files:
        if not validate_path(file):
            print(f"{file}: File not allowed to change")
            continue
        try:
            contents = get_stripped_contents(file)

            if inplace:
                overwrite_file(file, contents)
            else:
                print(f"{file.absolute()}".center(60, "-"))
                print(contents)
                print("EOF".center(60, "-"))

        except FileNotFoundError:
            print(f"{file}: No such file.")

        except UnicodeDecodeError:
            print(f"{file} Something went wrong. Unicode exception.")


def find_files_by_patterns(patterns: list[str]) -> list[Path]:
    """Recursively find all files and filter by given patterns"""
    found_files = []
    cwd = Path()
    files = cwd.rglob("*")
    for pattern in patterns:
        files = list(filter(lambda x: re.match(pattern, x.name), files))
        found_files.extend(files)
    return found_files


def strip_pattern_matched_files(patterns: list[str], inplace: bool = False) -> None:
    """Recursively find files by a pattern and strip comments/docstrings from them"""
    files = find_files_by_patterns(patterns)
    strip_files(files, inplace)


def main() -> None:
    print(args)
    match args.action:
        case "files":
            print(args.files)
            strip_files(args.files, inplace=args.inplace)
        case "recursive":
            print(args.patterns)
            strip_pattern_matched_files(args.patterns, inplace=args.inplace)
        case _:
            raise ValueError(f"Action not supported: {args.action}")


if __name__ == "__main__":
    args = parse_args()
    main()
