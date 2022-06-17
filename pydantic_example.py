"""
Summray:
    Simple example of using pydantic
"""
# from dataclasses import dataclass
from pydantic import BaseModel
from pydantic import (
    StrictInt, StrictFloat, PositiveInt, Field
)
from typing_extensions import Annotated
from typing import Union


class TestData(BaseModel):
    filename: Annotated[str, Field(min_length=4)]


class Resolution(BaseModel):
    width: StrictInt
    height: PositiveInt

    def __str__(self) -> str:
        return f"{self.width}x{self.height}"


class VideoTestData(TestData):
    fps: Union[StrictInt, StrictFloat]
    resolution: Resolution

    def __str__(self) -> str:
        return f"{self.fps} FPS for resolution {self.resolution}"


def main() -> int:
    resolution = Resolution(width=1920, height=1080)
    td = VideoTestData(filename=".mov", fps=30, resolution=resolution)
    print(f"__str__: {td}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
