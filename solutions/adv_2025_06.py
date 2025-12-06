import functools
import string
import typing


def _parse_nums(in_str: list[str]) -> list[int]:
    return [int(_) for _ in in_str]


def parse_input_a(in_str: str) -> list[tuple[list[int], str]]:
    lines = in_str.strip().splitlines()
    nums = [_parse_nums(_.split()) for _ in lines[:-1]]
    operations = lines[-1].split()
    return [(list(_[:-1]), _[-1]) for _ in zip(*nums, operations, strict=True)]


def _sum(in_nums: list[int]) -> int:
    res = sum(in_nums)
    assert isinstance(res, int)
    return res


def _prod(in_nums: list[int]) -> int:
    return functools.reduce(lambda _a, _b: _a * _b, in_nums)


_OPERATIONS = {"+": _sum, "*": _prod}


def _evaluate(in_nums: list[int], operation: str) -> int:
    return _OPERATIONS[operation](in_nums)


def _extract_num(raw_nums: list[str], pos: int) -> int:
    raw_digits = [_[pos] for _ in raw_nums]
    return int("".join(raw_digits).strip())


def _contains_some_digits(raw_nums: list[str], pos: int) -> bool:
    return any(_[pos] in string.digits for _ in raw_nums)


def _block_len(raw_nums: list[str], pos: int) -> int:
    res = 0
    while pos + res < len(raw_nums[0]) and _contains_some_digits(raw_nums, pos + res):
        res += 1
    return res


def _extract_nums(raw_nums: list[str], pos: int) -> list[int]:
    block_len = _block_len(raw_nums, pos)
    return [_extract_num(raw_nums, _) for _ in reversed(range(pos, pos + block_len))]


def parse_input_b(in_str: str) -> list[tuple[list[int], str]]:
    lines = in_str.strip().splitlines()
    raw_nums = lines[:-1]
    raw_ops = lines[-1]
    res = []
    for pos, val in enumerate(raw_ops):
        if val in _OPERATIONS:
            res.append((_extract_nums(raw_nums, pos), val))
    res.reverse()
    return res


def _get_solve(
    parse_input: typing.Callable[[str], list[tuple[list[int], str]]],
) -> typing.Callable[[str], int]:
    def _solve(in_str: str) -> int:
        return sum(_evaluate(*_) for _ in parse_input(in_str))

    return _solve


solve_a = _get_solve(parse_input_a)
solve_b = _get_solve(parse_input_b)
