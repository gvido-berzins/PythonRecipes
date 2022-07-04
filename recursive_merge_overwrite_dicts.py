"""
Summary: Merge overwrite a default dictionary with a targeted one.
Description:
    Useful when dealing with parsing a configuration file and having overwrite
    logic in some levels.
References:
    - (StackOverflow - How to merge dictionaries of dictionaries?)[https://stackoverflow.com/a/71700270]
"""

from copy import copy
from pprint import pprint


def _merge_dicts(src: dict = {}, dst: dict = {}) -> dict:
    return _merge_dicts_recursive(src, dst, copy(src))


def _merge_dicts_recursive(src: dict, dst: dict, final: dict) -> dict:
    for key in dst:
        # if the key doesn't exist in `src`, add the `dst` element to `src`
        if key not in src:
            final[key] = dst[key]

        else:
            # if the key value is a dict, both in `src` and in `dst`, merge the dicts
            if isinstance(src[key], dict) and isinstance(dst[key], dict):
                _merge_dicts_recursive(src[key], dst[key], final[key])

            # if the key value is the same in `src` and in `dst`, ignore
            elif src[key] == dst[key]:
                pass

            # if the key value differs in `src` and in `dst`, overwrite with `dst`
            else:
                final[key] = dst[key]

    return final


def main() -> int:
    profile = dict(
        name="default",
        mappings=dict(a="A", b="B"),
        links=["1", "2", "3"],
        plugins=dict(validator=dict(name="val1", enabled=True)),
    )
    extended_plugin = dict(
        name="extend_plugin", plugins=dict(validator=dict(targets=["numbers"]))
    )
    target = _merge_dicts(profile, extended_plugin)
    pprint(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
