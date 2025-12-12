from . import test_utils as tu

sol = tu.import_solution(__file__)

_INPUTS = tu.get_inputs(__file__, {"p"})

test_solve_a_single = _INPUTS.get_test(sol.solve_a, {"p": 526})
