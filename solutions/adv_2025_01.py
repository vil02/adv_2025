import enum
import typing


class Direction(enum.Enum):
    LEFT = 1
    RIGHT = 2


def _parse_instruction(in_str: str) -> tuple[Direction, int]:
    direction = in_str[0]
    step = int(in_str[1:])
    return {"L": Direction.LEFT, "R": Direction.RIGHT}[direction], step


def _parse_input(in_str: str) -> list[tuple[Direction, int]]:
    return [_parse_instruction(_) for _ in in_str.splitlines()]


def _step_to_shift(in_dir: Direction, in_step: int) -> int:
    return {Direction.RIGHT: 1, Direction.LEFT: -1}[in_dir] * in_step


_START_POS = 50
_LOCK_SIZE = 100


def _next_pos(in_pos: int, in_direction: Direction, in_step: int) -> int:
    return (in_pos + _step_to_shift(in_direction, in_step)) % _LOCK_SIZE


def _count_clicks_a(in_pos: int, in_dir: Direction, in_steps: int) -> int:
    if _next_pos(in_pos, in_dir, in_steps) == 0:
        return 1
    return 0


def _count_total_clicks(
    in_moves: list[tuple[Direction, int]],
    count_clicks: typing.Callable[[int, Direction, int], int],
) -> int:
    pos = _START_POS
    res = 0
    for direction, step in in_moves:
        res += count_clicks(pos, direction, step)
        pos = _next_pos(pos, direction, step)
    return res


def _count_clicks_r(in_pos: int, in_steps: int) -> int:
    return (in_pos + in_steps) // _LOCK_SIZE - in_pos // _LOCK_SIZE


def _count_clicks_l(in_pos: int, in_steps: int) -> int:
    return (in_pos - 1) // _LOCK_SIZE - (in_pos - in_steps - 1) // _LOCK_SIZE


def _count_clicks_b(in_pos: int, in_dir: Direction, in_steps: int) -> int:
    return {
        Direction.LEFT: _count_clicks_l,
        Direction.RIGHT: _count_clicks_r,
    }[
        in_dir
    ](in_pos, in_steps)


def _get_solve(
    count_clicks: typing.Callable[[int, Direction, int], int],
) -> typing.Callable[[str], int]:
    def _solve(in_str: str) -> int:
        return _count_total_clicks(_parse_input(in_str), count_clicks)

    return _solve


solve_a = _get_solve(_count_clicks_a)
solve_b = _get_solve(_count_clicks_b)
