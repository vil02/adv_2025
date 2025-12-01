def _parse_instruction(in_str: str) -> tuple[str, int]:
    direction = in_str[0]
    step = int(in_str[1:])
    return direction, step


def _parse_input(in_str: str) -> list[tuple[str, int]]:
    return [_parse_instruction(_) for _ in in_str.splitlines()]


def _step_to_shift(in_dir: str, in_step: int) -> int:
    if in_dir == "R":
        return in_step
    assert in_dir == "L"
    return -in_step


_START_POS = 50
_LOCK_SIZE = 100


def _simulate_moves(in_moves: list[tuple[str, int]]) -> int:
    pos = _START_POS
    res = 0
    for direction, step in in_moves:
        pos = (pos + _step_to_shift(direction, step)) % _LOCK_SIZE
        if pos == 0:
            res += 1
    return res


def solve_a(in_str: str) -> int:
    return _simulate_moves(_parse_input(in_str))


def _count_clicks_r(in_pos: int, in_steps: int) -> int:
    pos = in_pos
    res = 0
    for _ in range(in_steps):
        pos += 1
        if pos == _LOCK_SIZE:
            pos = 0
        if pos == 0:
            res += 1
    return res


def _count_clicks_l(in_pos: int, in_steps: int) -> int:
    pos = in_pos
    res = 0
    for _ in range(in_steps):
        pos -= 1
        if pos == 0:
            res += 1
        if pos == -1:
            pos = 99
    return res


def _count_clicks(in_pos: int, in_dir: str, in_steps: int) -> int:
    if in_dir == "R":
        return _count_clicks_r(in_pos, in_steps)
    assert in_dir == "L"
    return _count_clicks_l(in_pos, in_steps)


def _simulate_moves_b(in_moves: list[tuple[str, int]]) -> int:
    pos = _START_POS
    res = 0
    for direction, step in in_moves:
        res += _count_clicks(pos, direction, step)
        pos = (pos + _step_to_shift(direction, step)) % _LOCK_SIZE
    return res


def solve_b(in_str: str) -> int:
    return _simulate_moves_b(_parse_input(in_str))
