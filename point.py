from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Point:
    x: Optional[int]
    y: Optional[int]
    a: int
    b: int

    def __post_init__(self) -> None:
        if self.x is None and self.y is None:
            return
        assert self.x is not None
        assert self.y is not None
        assert self.y**2 == self.x**3 + self.a * self.x + self.b

    def __eq__(self, other: object):
        if not isinstance(other, Point):
            raise TypeError
        return (
            self.a == other.a
            and self.b == other.b
            and self.x == other.x
            and self.y == other.y
        )

    def __ne__(self, other: object):
        return not (self == other)

    def __add__(self, other: object) -> Point:
        if not isinstance(other, Point):
            raise TypeError
        if self.a != other.a or self.b != other.b:
            raise TypeError
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self.x == other.x:
            return Point(None, None, self.a, self.b)
        else:
            raise NotImplementedError
