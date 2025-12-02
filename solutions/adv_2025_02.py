import typing


def _parse_range(in_str: str) -> tuple[int, int]:
    start, stop = in_str.split("-")
    return int(start), int(stop)


def _parse_input(in_str: str) -> list[tuple[int, int]]:
    return [_parse_range(_) for _ in in_str.split(",")]


def _is_valid_single(in_str: str, in_len: int) -> bool:
    assert len(in_str) % in_len == 0
    piece = in_str[:in_len]
    assert len(piece) * (len(in_str) // in_len) == len(in_str)
    return all(
        in_str[_ * in_len : (_ + 1) * in_len] == piece
        for _ in range(1, len(in_str) // in_len)
    )


def is_valid_a(in_num: int) -> bool:
    in_str = str(in_num)
    if len(in_str) % 2 != 0:
        return False
    return _is_valid_single(in_str, len(in_str) // 2)


def _nontrivial_factors(in_num: int) -> typing.Iterable[int]:
    cur_div = 1
    while cur_div < in_num:
        if in_num % cur_div == 0:
            yield cur_div
        cur_div += 1


def is_valid_b(in_num: int) -> bool:
    in_str = str(in_num)
    return any(_is_valid_single(in_str, _) for _ in _nontrivial_factors(len(in_str)))


def _count_valid_in_range(
    start: int, stop: int, is_valid: typing.Callable[[int], bool]
) -> int:
    return sum(_ for _ in range(start, stop + 1) if is_valid(_))


def _count_all_valid(
    in_ranges: list[tuple[int, int]], is_valid: typing.Callable[[int], bool]
) -> int:
    return sum(
        _count_valid_in_range(start, stop, is_valid) for start, stop in in_ranges
    )


def _get_solve(is_valid: typing.Callable[[int], bool]) -> typing.Callable[[str], int]:
    def _solve(in_str: str) -> int:
        return _count_all_valid(_parse_input(in_str), is_valid)

    return _solve


solve_a = _get_solve(is_valid_a)
solve_b = _get_solve(is_valid_b)
