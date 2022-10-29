import pytest
from field_set import FieldElement


class TestFieldElement:
    @pytest.mark.parametrize(
        "lhs,rhs,expected",
        [
            ((1, 3), (1, 2), False),
            ((1, 3), (1, 3), True),
            ((1, 3), (2, 3), False),
        ],
    )
    def test_eq(
        self, lhs: tuple[int, int], rhs: tuple[int, int], expected: bool
    ) -> None:
        actual = FieldElement(*lhs) == FieldElement(*rhs)
        assert actual == expected

    @pytest.mark.parametrize(
        "lhs,rhs,expected",
        [
            (
                FieldElement(1, 2),
                FieldElement(1, 2),
                FieldElement(0, 2),
            ),
        ],
    )
    def test_add(
        self, lhs: FieldElement, rhs: FieldElement, expected: FieldElement
    ) -> None:
        assert lhs + rhs == expected
