"""
Summary: 
    Pythonic string enum
Description:
    Enum boilerplate that's been useful for my scripts.
References:
    - https://www.cosmicpython.com/blog/2020-10-27-i-hate-enums.html
"""
from enum import Enum, auto
from typing import List, Any


class BetterStrEnum(str, Enum):
    """Enum Subclass providing methods for casing operations"""

    def __str__(self) -> str:
        return str.__str__(self)

    def as_lower(self) -> str:
        """Get enum value in lowercase"""
        return self.value.lower()

    def as_upper(self) -> str:
        """Get enum value in uppercase"""
        return self.value.upper()

    @classmethod
    def keys(cls) -> list[str]:
        """return all enum key names in lower case"""
        return [enum for enum in cls.__members__.keys()]

    @classmethod
    def values(cls) -> list[str]:
        """return all enum key names in lower case"""
        return [enum.value for enum in cls.__members__.values()]

    @classmethod
    def keys_as_lower(cls) -> list[str]:
        """return all enum key names in lower case"""
        return [key.lower() for key in cls.keys()]

    @classmethod
    def values_as_lower(cls) -> List[str]:
        """Return all enum values in lower case"""
        return [value.lower() for value in cls.values()]

    @classmethod
    def get(cls, key, default=None) -> Any:
        """Dictionary get method"""
        return cls.__dict__.get(key, default)

    @classmethod
    def get_u(cls, key, default=None) -> "BetterStrEnum":
        """Dictionary get, but the key is uppercased, useful because of the enum naming"""
        return cls.__dict__.get(key.upper(), default)


class SectionType(BetterStrEnum):
    CUSTOM = "custom"
    INCLUDE = "include"
    UNNAMED = auto()

    @classmethod
    def detect(cls, type_) -> str:
        """Detect the Section Type, return UNNAMED by default"""
        return cls.get_u(type_, cls.UNNAMED)


def main() -> int:
    print("ENUM == string:", SectionType.CUSTOM == "custom")
    print("string in ENUM values:", "custom" in SectionType.values())
    print("get_u(custom):", SectionType.get_u("custom"))
    print("get_u(something):", SectionType.get_u("something"))
    print("All keys:", SectionType.keys_as_lower())
    print("All keys in lower:", SectionType.keys())
    print("All values:", SectionType.values())
    print("All members:", SectionType.values)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
