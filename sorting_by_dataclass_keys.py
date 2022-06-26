"""
Summary: Variable dataclass sorting
Description: Sort dataclasses with any given sorting order
"""
import functools
import itertools
import operator
from typing import Any, Callable, Iterable, List, Tuple
from dataclasses import dataclass, field

DEFAULT_SORT_ORDER = ["type", "app", "platform", "condition"]


@dataclass
@functools.total_ordering
class Scen:
    type: str
    app: str
    platform: str
    condition: str

    sort_order: list[str] = field(default_factory=list, repr=False)

    def __post_init__(self):
        self.sort_order = DEFAULT_SORT_ORDER

    def get(self, key) -> Any:
        return self.__getattribute__(key)

    @staticmethod
    def sorted_key_method(order, scen) -> List[str]:
        return [scen.__getattribute__(key) for key in order]

    @staticmethod
    def from_tuple(t: Tuple) -> "Scen":
        return Scen(*t)

    # TODO: This method doesn't work for me as expected
    def compare(self, comparison_op, other) -> bool:
        for key in self.sort_order:
            self_attr = self.__getattribute__(key)
            other_attr = other.__getattribute__(key)
            if comparison_op(self_attr, other_attr):
                return True
            elif operator.eq(self_attr, other_attr):
                continue
        else:
            return False

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.type}, {self.app}, {self.platform}, {self.condition})"
        )

    def __lt__(self, other):
        return self.compare(operator.lt, other)

    def __gt__(self, other):
        return self.compare(operator.gt, other)

    def __le__(self, other):
        return self.compare(operator.le, other)

    def __ge__(self, other):
        return self.compare(operator.ge, other)

    def __eq__(self, other):
        return self.compare(operator.eq, other)


@dataclass
class Rule:
    key: str
    operator: Callable
    value: List[str]

    def check(self, scen: Scen) -> bool:
        other_value = scen.get(self.key)
        if other_value is None:
            raise AttributeError(f"No such key: '{self.key}'")
        return self.operator(self.value, other_value)


@dataclass
class Graph:
    x_axis: Tuple[str, Tuple[str]]
    series: str
    scens: List[Scen]

    @staticmethod
    def sorted_key_method(order, graph) -> List[str]:
        return Scen.sorted_key_method(order, graph.scens[0])


def _prepare_scens() -> List[Scen]:
    types = ("video", "audio")
    apps = ("Instagram", "Zoom")
    platforms = ("Windows", "Mac")
    conditions = ("Unlimited", "50PL", "1Mbps")

    combinations = itertools.product(types, apps, platforms, conditions)
    scens = list(map(Scen.from_tuple, combinations))
    return scens


def sort_scens_by_sort_order(scens: Iterable[Scen], sort_order) -> List[Scen]:
    custom_sort = functools.partial(Scen.sorted_key_method, sort_order)
    scens = sorted(scens, key=custom_sort, reverse=False)
    return scens


def sort_graphs_by_scen_sort_order(graphs: Iterable[Graph], sort_order) -> List[Graph]:
    custom_sort = functools.partial(Graph.sorted_key_method, sort_order)
    graphs = sorted(graphs, key=custom_sort, reverse=False)
    return graphs


def print_n(list_: Iterable[Any], reverse: bool = False) -> None:
    print("LIST".center(70, "-"))
    if reverse:
        list_ = reversed(list_)

    for item in list_:
        print(item)


def do_only_sorts(scens: Iterable[Scen]) -> None:
    scens = sort_scens_by_sort_order(scens, ["type", "app", "platform", "condition"])
    print_n(scens)
    scens = sort_scens_by_sort_order(scens, ["platform", "app", "condition"])
    print_n(scens)
    scens = sort_scens_by_sort_order(scens, ["condition"])
    print_n(scens)


def group_scens_by_sort_order(scens: Iterable[Scen], sort_order: List[str]) -> Iterable:
    sort_groups = set(tuple((key, scen.get(key)) for key in sort_order) for scen in scens)
    scen_groups = []
    for sort_group in sort_groups:
        scen_group = tuple(
            scen
            for scen in scens
            if all(scen.get(key) == value for key, value in sort_group)
        )
        scen_groups.append((sort_group, scen_group))
    return scen_groups


def check_rules(scens: Iterable[Scen]):
    rules = (
        Rule("platform", operator.contains, ["Mac"]),
        Rule("type", operator.contains, ["video", "audio"]),
    )
    for scen in scens:
        print(scen)
        if all(rule.check(scen) for rule in rules):
            print(f"Rule '{rules}' checked '{scen}'")


def create_graphs(scens: List[Scen], x_axis: str, sort_order: List[str]) -> Tuple[Graph]:
    groups = group_scens_by_sort_order(scens, sort_order)
    graphs = tuple(
        Graph(
            x_axis=(x_axis, tuple(scen.get(x_axis) for scen in scens)),
            series=",".join(v for _, v in sorts),
            scens=scens,
        )
        for sorts, scens in groups
    )
    return graphs


def main() -> int:
    scens = _prepare_scens()
    # do_only_sorts(scens)
    # group_scens_by_sort_order(scens, ["type", "app", "platform"])
    sort_order = ["app", "type", "platform"]
    # sort_order = ["type", "app", "platform"]
    scens = sort_scens_by_sort_order(scens, sort_order)
    x_axis = "condition"
    graphs = create_graphs(scens, x_axis, sort_order)
    graphs = sort_graphs_by_scen_sort_order(graphs, sort_order)
    # print_n(map(lambda x: x.series, graphs))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
