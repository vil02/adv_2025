from . import test_utils as tu

test_solve_a, test_solve_b = tu.regular_tests(
    __file__, {"small": (40, 25272), "p": (244188, 8361881885)}
)
