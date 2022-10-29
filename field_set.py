from __future__ import annotations
from dataclasses import dataclass


@dataclass
class FieldSet:
    num: int
    prime: int

    def __post_init__(self) -> None:
        if self.num < 0 or self.num >= self.prime:
            raise ValueError

    def __eq__(self, other: object) ->  bool:
        if not isinstance(other, FieldSet):
            return False
        return self.num == other.num and self.prime == other.prime
