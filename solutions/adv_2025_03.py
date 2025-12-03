import typing


def _parse_line(in_str: str) -> list[int]:
    return [int(_) for _ in in_str]


def _parse_input(in_str: str) -> list[list[int]]:
    return [_parse_line(_) for _ in in_str.splitlines()]


def _join_joltages(first: int, rest: int, size: int) -> int:
    res = first * 10 ** (size - 1) + rest
    assert isinstance(res, int)
    return res


def _pos_and_max(bank: list[int]) -> tuple[int, int]:
    max_val = max(bank)
    return bank.index(max_val), max_val


def max_joltage(bank: list[int], size: int) -> int:
    assert size > 0
    assert len(bank) >= size
    if size == 1:
        return max(bank)
    cur_pos, cur_best = _pos_and_max(bank[: len(bank) - size + 1])
    return _join_joltages(cur_best, max_joltage(bank[cur_pos + 1 :], size - 1), size)


def _total_joltage(banks: list[list[int]], joltage_size: int) -> int:
    return sum(max_joltage(_, joltage_size) for _ in banks)


def _get_solve(joltage_size: int) -> typing.Callable[[str], int]:
    def _solve(in_str: str) -> int:
        return _total_joltage(_parse_input(in_str), joltage_size)

    return _solve


solve_a = _get_solve(2)
solve_b = _get_solve(12)
