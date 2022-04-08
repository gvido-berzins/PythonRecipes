"""
Summary:
    Learning about sanitizing paths and bypassing it
Description:
    Small experiment to test out bypassing path sanitization methods,
    includes a few validator functions for a single given path
"""
from collections import Counter
from pathlib import Path

VALIDATORS = set()


def register(func):
    print(f"REGISTERED: {func}")
    VALIDATORS.add(func)

    def wrapper(*args):
        return func(*args)

    return wrapper


@register
def unsafe_validator(path: Path):
    path = str(path).replace("/home", "")

    if path.strip() in ["", "/"]:
        return False
    else:
        return True


@register
def file_validator(path: Path):
    try:
        if not path.exists():
            return False
    except PermissionError:
        return False

    if path.is_symlink():  # Might not reach, links get resolved
        return False

    return True


@register
def blacklist_validator(path: Path):
    BLACKLIST = ["/root", "/bin", "/sys", "/proc", "/usr"]
    NOT_ALLOWED = ["", "/", ".", "/home"]
    path = str(path.resolve()).strip()
    for item in BLACKLIST:
        if path.startswith(item) or path in NOT_ALLOWED:
            return False
    return True


# @register
def whitelist_validator(path: Path):
    """The most powerfull!"""
    WHITELIST = ["/tmp"]
    path = str(path.resolve()).strip()
    for item in WHITELIST:
        if not path.startswith(item):
            return False
    return True


class PathChecker:
    def __init__(self, *validators):
        self.validators = validators

    def validate(self, path: Path | str):
        for validator in self.validators:
            is_valid = validator(path)
            if not is_valid:
                return False
        return True


def path_iter(block):
    for path, expected in block:
        yield Path(path), expected


def main():
    paths = [
        ["/home", False],
        ["/root", False],
        ["root", False],
        ["", True],
        ["/bin", False],
        ["/bin/bash", False],
        ["/root/tmp-dir", False],
        ["/../root", False],
        # ["door", False],  # Symbolic link to /root
        # ["gend", False],  # Symbolic link to a readable file
        # ["bloot", False],  # Symbolic linkt to filesystem root
        ["/../root", False],
        [" /../root", False],
    ]
    pc = PathChecker(*VALIDATORS)
    results = []
    print("VALIDATOR TEST".center(60, "-"))
    for path, expected_validation in path_iter(paths):
        is_safe = pc.validate(path)
        has_passed = is_safe == expected_validation
        result = "PASS" if has_passed else "FAIL"
        results.append(result)
        print(str(path.resolve()).ljust(60), result)

    stats = str(Counter(results))
    print(stats.center(60, "-"))


if __name__ == "__main__":
    main()
