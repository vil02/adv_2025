import solutions.adv_2025_05 as sol

from . import test_utils as tu

_INPUTS = tu.get_inputs(5, {"small", "p"})

test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (3, 14), "p": (690, 344323629240733)}
)
