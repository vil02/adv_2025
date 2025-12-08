from . import test_utils as tu

sol = tu.import_solution(__file__)


test_solve_a, test_solve_b = tu.get_inputs(__file__, {"small", "p"}).get_tests(
    (sol.solve_a, sol.solve_b), {"small": (3, 14), "p": (690, 344323629240733)}
)
