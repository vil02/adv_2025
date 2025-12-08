import pytest

from . import test_utils as tu

sol = tu.import_solution(__file__)


@pytest.mark.parametrize(
    ("bank", "size", "expected"),
    [
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 2, 98),
        ([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 2, 89),
        ([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 2, 78),
        ([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 2, 92),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 12, 987654321111),
        ([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 12, 811111111119),
        ([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 12, 434234234278),
        ([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 12, 888911112111),
    ],
)
def test_max_joltage(bank: list[int], size: int, expected: int) -> None:
    assert sol.max_joltage(bank, size) == expected


test_solve_a, test_solve_b = tu.get_inputs(__file__, {"small", "p"}).get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (357, 3121910778619), "p": (16858, 167549941654721)},
)
