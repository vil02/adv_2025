from . import test_utils as tu

test_solve_a, test_solve_b = tu.regular_tests(
    __file__, {"small": (7, 33), "p": (494, 19235), "r_0": (1, 74)}
)
