import solutions.adv_2025_07 as sol

from . import test_utils as tu

_INPUTS = tu.get_inputs(7, {"small", "p"})


test_solve_a, test_solve_b = _INPUTS.get_tests(
    (sol.solve_a, sol.solve_b), {"small": (21, 40), "p": (1660, 305999729392659)}
)
