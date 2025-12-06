import solutions.adv_2025_06 as sol

from . import test_utils as tu

_INPUTS = tu.get_inputs(6, {"small", "p"})

_DATA_SMALL = _INPUTS.inputs["small"]


def test_parse_input_a() -> None:
    assert _DATA_SMALL is not None
    assert sol.parse_input_a(_DATA_SMALL) == [
        ([123, 45, 6], "*"),
        ([328, 64, 98], "+"),
        ([51, 387, 215], "*"),
        ([64, 23, 314], "+"),
    ]


def test_parse_input_b() -> None:
    assert _DATA_SMALL is not None
    assert sol.parse_input_b(_DATA_SMALL) == [
        ([4, 431, 623], "+"),
        ([175, 581, 32], "*"),
        ([8, 248, 369], "+"),
        ([356, 24, 1], "*"),
    ]


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b),
    {"small": (4277556, 3263827), "p": (6209956042374, 12608160008022)},
)
