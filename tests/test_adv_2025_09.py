from . import test_utils as tu

test_solve_a, test_solve_b = tu.regular_tests(
    __file__,
    {
        "small": (50, 24),
        "p": (4760959496, 1343576598),
        "r_0": (180, 30),
        "r_1": (10 * 9, 40),
        "r_2": (10 * 9, 30),
        "r_3": (16 * 16, 66),
    },
)
