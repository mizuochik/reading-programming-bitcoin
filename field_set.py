from __future__ import annotations
from dataclasses import dataclass


@dataclass
class FieldElement:
    num: int
    prime: int

    def __post_init__(self) -> None:
        if self.num < 0 or self.num >= self.prime:
            raise ValueError

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FieldElement):
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __add__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError
        return FieldElement((self.num + other.num) % self.prime, self.prime)

    def __sub__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError
        return FieldElement((self.num - other.num) % self.prime, self.prime)

    def __mul__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError
        return FieldElement((self.num * other.num) % self.prime, self.prime)

    def __truediv__(self, other: FieldElement) -> FieldElement:
        if self.prime != other.prime:
            raise TypeError
        return FieldElement(
            num=(self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime,
            prime=self.prime,
        )

    def __pow__(self, exp: int) -> FieldElement:
        while exp < 0:
            exp += self.prime - 1
        return FieldElement(pow(self.num, exp, self.prime), self.prime)
