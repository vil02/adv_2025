import collections
import typing

import numpy as np
import scipy


def _parse_button(in_str: str) -> list[int]:
    assert in_str.startswith("(")
    assert in_str.endswith(")")
    positions = in_str[1:-1].split(",")
    return [int(_) for _ in positions]


def _parse_buttons(buttons: list[str]) -> list[list[int]]:
    return [_parse_button(_) for _ in buttons]


def _parse_target(in_str: str) -> str:
    assert in_str.startswith("[")
    assert in_str.endswith("]")
    return in_str[1:-1]


def _parse_joltages(in_str: str) -> tuple[int, ...]:
    assert in_str.startswith("{")
    assert in_str.endswith("}")
    return tuple(int(_) for _ in in_str[1:-1].split(","))


def _assert_fit(buttons: list[list[int]], target_len: int) -> None:
    assert all(0 <= max(_) < target_len for _ in buttons)


def _parse_machine(
    in_str: str,
) -> tuple[str, list[list[int]], tuple[int, ...]]:
    pieces = in_str.split()
    target = _parse_target(pieces[0])
    buttons = _parse_buttons(pieces[1:-1])
    joltages = _parse_joltages(pieces[-1])
    _assert_fit(buttons, min(len(target), len(joltages)))
    return target, buttons, joltages


def _parse_input(
    in_str: str,
) -> list[tuple[str, list[list[int]], tuple[int, ...]]]:
    return [_parse_machine(_) for _ in in_str.splitlines()]


def _toggle_single(in_str: str) -> str:
    return {".": "#", "#": "."}[in_str]


def _toggle(state: str, button: list[int]) -> str:
    res = list(state)
    for _ in button:
        res[_] = _toggle_single(res[_])
    return "".join(res)


def _new_states(state: str, buttons: list[list[int]]) -> typing.Iterator[str]:
    for _ in buttons:
        yield _toggle(state, _)


def _get_start_state(size: int) -> str:
    return "".join("." for _ in range(size))


def _early_exit_bsf(target: str, buttons: list[list[int]]) -> int | None:
    start = _get_start_state(len(target))
    assert start != target
    visited = set()
    queue = collections.deque([(start, 0)])
    while queue:
        cur_state, moves = queue.popleft()
        for new_state in _new_states(cur_state, buttons):
            if new_state == target:
                return moves + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves + 1))
    return None


def _minimal_number_of_presses_a(target: str, buttons: list[list[int]]) -> int:
    res = _early_exit_bsf(target, buttons)
    assert res is not None
    return res


def solve_a(in_str: str) -> int:
    data = _parse_input(in_str)
    return sum(
        _minimal_number_of_presses_a(target, buttons) for target, buttons, _ in data
    )


def _get_matrix_a(buttons: list[list[int]], target_size: int) -> np.ndarray:
    res = np.zeros((target_size, len(buttons)), dtype=float)

    for button_num, button in enumerate(buttons):
        for pos in button:
            res[pos][button_num] = 1
    return res


def _get_matrix_b(target: tuple[int, ...]) -> np.ndarray:
    return np.array([[_] for _ in target], dtype=float)


def _safe_round(in_val: float | None) -> int:
    assert isinstance(in_val, float)
    res = round(in_val)
    assert abs(res - in_val) < 0.0000001
    return res


def _minimal_number_of_presses_b(
    target: tuple[int, ...], buttons: list[list[int]]
) -> int:
    mat_a = _get_matrix_a(buttons, len(target))
    mat_b = _get_matrix_b(target)
    sol = scipy.optimize.linprog(
        c=np.ones(len(buttons), dtype=float), A_eq=mat_a, b_eq=mat_b, integrality=1
    )
    assert sol.success
    return _safe_round(sol.fun)


def solve_b(in_str: str) -> int:
    data = _parse_input(in_str)
    return sum(
        _minimal_number_of_presses_b(target, buttons) for _, buttons, target in data
    )
