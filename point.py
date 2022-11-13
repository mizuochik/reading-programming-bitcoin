from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Point:
    x: Optional[float]
    y: Optional[float]
    a: float
    b: float

    def __post_init__(self) -> None:
        if self.x is None and self.y is None:
            return
        assert self.x is not None
        assert self.y is not None
        assert self.y**2 == self.x**3 + self.a * self.x + self.b

    def __eq__(self, other: object):
        assert isinstance(other, Point)
        return (
            self.a == other.a
            and self.b == other.b
            and self.x == other.x
            and self.y == other.y
        )

    def __ne__(self, other: object):
        return not (self == other)

    def __add__(self, other: object) -> Point:
        assert isinstance(other, Point)
        if self.a != other.a or self.b != other.b:
            raise TypeError
        if self.x is None:
            return other
        if other.x is None:
            return self
        assert self.y is not None
        assert other.y is not None
        if self.x == other.x:
            return Point(None, None, self.a, self.b)
        s = (other.y - self.y) / (other.x - self.x)
        x = s**2 - self.x - other.x
        y = s * (self.x - x) - self.y
        return Point(x, y, self.a, self.b)
