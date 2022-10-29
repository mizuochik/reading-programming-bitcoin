import pytest
from field_set import FieldSet


class TestField:
    @pytest.mark.parametrize("lhs,rhs,expected", [
        ((1, 3), (1,2), False),
        ((1, 3), (1,3), True),
        ((1, 3), (2,3), False),
    ])
    def test_eq(self, lhs: tuple[int,int], rhs: tuple[int,int], expected: bool) -> None:
        actual = FieldSet(*lhs) == FieldSet(*rhs)
        assert actual == expected
