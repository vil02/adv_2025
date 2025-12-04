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


def _remove_accessible(rolls: Rolls) -> tuple[Rolls, bool]:
    removed = False
    res = {}
    for pos, val in rolls.items():
        if val == _FREE:
            res[pos] = val
        else:
            assert val == _ROLL
            if _is_accessible(rolls, pos):
                res[pos] = _FREE
                removed = True
            else:
                res[pos] = _ROLL
    return res, removed


def _remove_all(rolls: Rolls) -> Rolls:
    res, removed = _remove_accessible(rolls)
    while removed:
        res, removed = _remove_accessible(res)
    return res


def solve_b(in_str: str) -> int:
    rolls = _parse_input(in_str)
    removed = _remove_all(rolls)
    return sum(
        1
        for val_a, val_b in zip(rolls.values(), removed.values(), strict=True)
        if val_a != val_b
    )
