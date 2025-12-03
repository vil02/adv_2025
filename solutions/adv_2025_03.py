import functools
import typing


def _parse_line(in_str: str) -> tuple[int, ...]:
    return tuple(int(_) for _ in in_str)


def _parse_input(in_str: str) -> list[tuple[int, ...]]:
    return [_parse_line(_) for _ in in_str.splitlines()]


def _join_joltages(first: int, rest: int, size: int) -> int:
    res = first * 10 ** (size - 1) + rest
    assert isinstance(res, int)
    return res


@functools.lru_cache(None)
def max_joltage(bank: tuple[int, ...], size: int) -> int:
    assert len(bank) >= size
    if size == 0:
        return 0
    return max(
        _join_joltages(
            bank[first_pos], max_joltage(tuple(bank[first_pos + 1 :]), size - 1), size
        )
        for first_pos in range(len(bank) - size + 1)
    )


def _get_solve(joltage_size: int) -> typing.Callable[[str], int]:
    def _solve(in_str: str) -> int:
        return sum(max_joltage(_, joltage_size) for _ in _parse_input(in_str))

    return _solve


solve_a = _get_solve(2)
solve_b = _get_solve(12)
