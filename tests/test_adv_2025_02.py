import pytest

import solutions.adv_2025_02 as sol

from . import test_utils as tu


@pytest.mark.parametrize(
    ("in_num"),
    [11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859],
)
def test_is_valid_a_positive(in_num: int) -> None:
    assert sol.is_valid_a(in_num)


@pytest.mark.parametrize(
    ("in_num"),
    [111, 121, 123123123],
)
def test_is_valid_a_negative(in_num: int) -> None:
    assert not sol.is_valid_a(in_num)


@pytest.mark.parametrize(
    ("in_num"),
    [
        11,
        22,
        99,
        111,
        999,
        1010,
        1188511885,
        222222,
        446446,
        38593859,
        565656,
        824824824,
        2121212121,
    ],
)
def test_is_valid_b_positive(in_num: int) -> None:
    assert sol.is_valid_b(in_num)


@pytest.mark.parametrize(
    ("in_num"),
    [123, 12121],
)
def test_is_valid_b_negative(in_num: int) -> None:
    assert not sol.is_valid_b(in_num)


_INPUTS = tu.get_inputs(2, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (1227775554, 4174379265), "p": (41294979841, 66500947346)},
)
