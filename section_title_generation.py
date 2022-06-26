"""
Summary:
    Section title generator algorithm
Description:
    From a list of scenarios and given section keys, generate an ordered list of
    titles where before each section key a new title is created.
"""
import itertools
from typing import Any, Iterable


def print_n(list_: Iterable[Any], reverse: bool = False) -> None:
    print("LIST".center(70, "-"))
    if reverse:
        list_ = reversed(list_)

    for item in list_:
        print(item)


def _prepare_scenarios():
    types = ("video", "audio")
    apps = ("instagram", "messenger")
    platforms = ("winChrome", "macSafari", "ios", "android")
    conditions = ("Unlimited", "50PL", "100k")

    combinations = itertools.product(types, apps, platforms, conditions)
    combinations = tuple(
        map(
            lambda x: (
                ("call_type", x[0]),
                ("app", x[1]),
                ("platform", x[2]),
                ("condition", x[3]),
            ),
            combinations,
        )
    )
    return sorted(combinations)


def prepare_titles(scenarios, section_keys):
    final_list = []
    for i, scen in enumerate(scenarios):
        if i == 0:
            for ck, cv in scen:
                if ck in section_keys:
                    final_list.append(f"Section - {cv.upper()}")
        else:
            prev = scenarios[i - 1]
            targets = (
                ((ck, cv), (pk, pv))
                for (ck, cv), (pk, pv) in zip(scen, prev)
                if ck in section_keys and pk in section_keys
            )
            change_following = False
            for current_tuple, prev_tuple in targets:
                if current_tuple != prev_tuple or change_following:
                    final_list.append(f"Section - {current_tuple[1].upper()}")
                    change_following = True

        title = " - ".join(v for _, v in scen)
        final_list.append(title)
    return final_list


def main() -> int:
    scenarios = _prepare_scenarios()
    section_keys = ("call_type", "app", "platform")
    titles = prepare_titles(scenarios, section_keys)

    print_n(titles)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
