from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    a: int
    b: int

    def __post_init__(self) -> None:
        if self.y**2 != self.x**3 + self.a * self.x + self.b:
            raise ValueError

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
