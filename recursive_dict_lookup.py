"""
Summary:
    Recurse into a dictionary to safely get a value.

Description:
    From a given dictionary (or JSON), return a nested value using
    the varargs in the function parameters, otherwise return
    the default value.
"""
from collections import deque
from typing import Any


def recursive_get(dict_: dict, *args, default="") -> Any:
    args = deque(list(args))
    arg = args.popleft()
    value = dict_.get(arg, default)

    if not isinstance(value, dict) and args:
        return default

    if not args:
        return value

    return recursive_get(value, *args, default=default)


if __name__ == "__main__":
    json = {"some": {"key": {"inside": "GOT ME!"}, "some other key": 1}}
    result = recursive_get(json, "some", "some", default=1)
    print(f"{result=}")

    result = recursive_get(json, "some", "key", "inside", default=2)
    print(f"{result=}")

    result = recursive_get(json, "some", "some other key", default=3)
    print(f"{result=}")
