from . import test_utils as tu

sol = tu.import_solution(__file__)


test_solve_a, test_solve_b = tu.get_inputs(__file__, {"small", "p"}).get_tests(
    (sol.solve_a, sol.solve_b), {"small": (50, 24), "p": (4760959496, 1343576598)}
)
