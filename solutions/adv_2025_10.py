import heapq
import typing

import scipy


def _parse_button(in_str: str) -> list[int]:
    assert in_str.startswith("(")
    assert in_str.endswith(")")
    positions = in_str[1:-1].split(",")
    return [int(_) for _ in positions]


def _parse_buttons(buttons: list[str]) -> list[list[int]]:
    return [_parse_button(_) for _ in buttons]


def _parse_target(in_str: str) -> tuple[str, ...]:
    assert in_str.startswith("[")
    assert in_str.endswith("]")
    return tuple(in_str[1:-1])


def _parse_joltages(in_str: str) -> tuple[int, ...]:
    assert in_str.startswith("{")
    assert in_str.endswith("}")
    return tuple(int(_) for _ in in_str[1:-1].split(","))


def _parse_machine(
    in_str: str,
) -> tuple[tuple[str, ...], list[list[int]], tuple[int, ...]]:
    pieces = in_str.split()
    target = _parse_target(pieces[0])
    buttons = _parse_buttons(pieces[1:-1])
    joltages = _parse_joltages(pieces[-1])
    assert all(0 <= max(_) < len(target) for _ in buttons)
    assert all(0 <= max(_) < len(joltages) for _ in buttons)
    return target, buttons, joltages


def _parse_input(
    in_str: str,
) -> list[tuple[tuple[str, ...], list[list[int]], tuple[int, ...]]]:
    return [_parse_machine(_) for _ in in_str.splitlines()]


def _toggle_single(in_str: str) -> str:
    return {".": "#", "#": "."}[in_str]


def _toggle(state: tuple[str, ...], button: list[int]) -> tuple[str, ...]:
    res = list(state)
    for _ in button:
        res[_] = _toggle_single(res[_])
    return tuple(res)


def _new_states(
    state: tuple[str, ...], buttons: list[list[int]]
) -> typing.Iterator[tuple[str, ...]]:
    for _ in buttons:
        yield _toggle(state, _)


def _get_start_state(size: int) -> tuple[str, ...]:
    return tuple("." for _ in range(size))


def _dijkstra(
    initial_state: tuple[str, ...], buttons: list[list[int]]
) -> dict[tuple[str, ...], tuple[int, tuple[str, ...] | None]]:
    active: list[tuple[int, tuple[str, ...], tuple[str, ...] | None]] = []
    heapq.heappush(active, (0, initial_state, None))
    visited = set()
    res: dict[tuple[str, ...], tuple[int, tuple[str, ...] | None]] = {}
    while active:
        moves, cur_state, prev_state = heapq.heappop(active)
        if cur_state in visited:
            continue
        visited.add(cur_state)
        if cur_state not in res or moves < res[cur_state][0]:
            res[cur_state] = (moves, prev_state)
            for new_state in _new_states(cur_state, buttons):
                heapq.heappush(active, (moves + 1, new_state, cur_state))
    return res


def _minimal_number_of_presses(
    target: tuple[str, ...], buttons: list[list[int]]
) -> int:
    return _dijkstra(_get_start_state(len(target)), buttons)[target][0]


def solve_a(in_str: str) -> int:
    data = _parse_input(in_str)
    return sum(
        _minimal_number_of_presses(target, buttons) for target, buttons, _ in data
    )


def _get_matrix(buttons: list[list[int]], target_size: int) -> list[list[int]]:
    res = [[0 for _ in buttons] for _ in range(target_size)]

    for button_num, button in enumerate(buttons):
        for pos in button:
            res[pos][button_num] = 1
    return res


def _get_matrix_b(target: tuple[int, ...]) -> list[list[int]]:
    return [[_] for _ in target]


def _minimal_number_of_presses_b(
    target: tuple[int, ...], buttons: list[list[int]]
) -> int:
    mat_a = _get_matrix(buttons, len(target))
    mat_b = _get_matrix_b(target)
    sol = scipy.optimize.linprog(
        c=[1] * len(buttons), A_eq=mat_a, b_eq=mat_b, integrality=1
    )  # type: ignore
    res = round(sol.fun)
    assert abs(res - sol.fun) < 0.00001
    assert isinstance(res, int)
    return res


def solve_b(in_str: str) -> int:
    data = _parse_input(in_str)
    return sum(
        _minimal_number_of_presses_b(target, buttons) for _, buttons, target in data
    )
