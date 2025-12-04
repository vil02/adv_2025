Pos = tuple[int, int]
Rolls = dict[Pos, str]


def _parse_input(in_str: str) -> Rolls:
    res = {}
    for y_cur, line in enumerate(in_str.splitlines()):
        for x_cur, value in enumerate(line):
            res[x_cur, y_cur] = value
    return res


_FREE = "."
_ROLL = "@"


def _is_roll(rolls: Rolls, pos: Pos) -> bool:
    return rolls.get(pos, "") == _ROLL


def _shift(pos: Pos, shift: Pos) -> Pos:
    res = tuple(sum(_) for _ in zip(pos, shift, strict=True))
    assert len(res) == 2
    return res


_DIRS = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)}

assert len(_DIRS) == 8


def _count_rolls_around(rolls: Rolls, pos: Pos) -> int:
    return sum(1 for _ in _DIRS if _is_roll(rolls, _shift(pos, _)))


def _is_accessible(rolls: Rolls, pos: Pos) -> bool:
    assert rolls[pos] == _ROLL
    return _count_rolls_around(rolls, pos) < 4


def _count_accessible(rolls: Rolls) -> int:
    return sum(1 for _ in rolls if rolls[_] == _ROLL and _is_accessible(rolls, _))


def solve_a(in_str: str) -> int:
    return _count_accessible(_parse_input(in_str))


def _remove_accessible(rolls: Rolls) -> int:
    removed = 0
    for pos, val in rolls.items():
        if val == _ROLL and _is_accessible(rolls, pos):
            rolls[pos] = _FREE
            removed += 1
    return removed


def _remove_all(rolls: Rolls) -> int:
    total_removed = 0
    while (removed := _remove_accessible(rolls)) > 0:
        total_removed += removed
    return total_removed


def solve_b(in_str: str) -> int:
    return _remove_all(_parse_input(in_str))
