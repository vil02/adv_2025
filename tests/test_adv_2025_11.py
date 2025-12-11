from . import test_utils as tu

sol = tu.import_solution(__file__)

_INPUTS = tu.get_inputs(__file__, {"small", "small_2", "p"})

test_solve_a = _INPUTS.get_test(sol.solve_a, {"small": 5, "p": 652})

test_solve_b = _INPUTS.get_test(sol.solve_b, {"small_2": 2, "p": 362956369749210})
