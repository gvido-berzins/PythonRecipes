"""
Summary:
    Dataclass usage examples
"""
from dataclasses import dataclass, field


@dataclass
class Person:
    """Simple dataclass representing a person"""

    name: str
    surname: str
    age: int


@dataclass(order=True)
class SortablePerson:
    """Dataclass with a custom sort index field.

    Required:
    - @dataclass(order=True)
    - sort_index: int = field(init=False, repr=False)
    - def __post_init__(self):
          self.sort_index = self.age
    """

    sort_index: int = field(init=False, repr=False)
    name: str
    surname: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age


@dataclass
class TestCase:
    """Dataclass with default factories

    - mutable objects need to be in a factory (otherwise ValueError)
    - `repr=False` used for data that we don't want to see when using `print`
    """

    title: str
    steps: list[str] = field(default_factory=list)
    comments: list[str] = field(default_factory=list, repr=False)


def sortable_example():
    p1 = SortablePerson("John", "Lemon", 20)
    p2 = SortablePerson("John", "Zemon", 22)
    p3 = SortablePerson("John", "Demon", 21)
    p4 = SortablePerson("John", "Aemon", 90)
    p = sorted([p1, p2, p3, p4])
    print(p)


def factory_example():
    t1 = TestCase(
        title="Super test",
        steps=["Login", "Analyze", "Validate"],
        comments=["The steps are too generic, please use more context"],
    )
    print(t1)


def main() -> int:
    # sortable_example()
    factory_example()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
