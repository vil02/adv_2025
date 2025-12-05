def _parse_range(in_str: str) -> tuple[int, int]:
    start, end = in_str.split("-")
    return int(start), int(end)


def _parse_id(in_str: str) -> int:
    return int(in_str)


def _parse_ranges(in_str: str) -> list[tuple[int, int]]:
    return [_parse_range(_) for _ in in_str.splitlines()]


def _parse_ids(in_str: str) -> list[int]:
    return [_parse_id(_) for _ in in_str.splitlines()]


def _parse_input(in_str: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges, ids = in_str.split("\n\n")
    return _parse_ranges(ranges), _parse_ids(ids)


def _is_contained(in_range: tuple[int, int], in_id: int) -> bool:
    return in_range[0] <= in_id <= in_range[1]


def _is_contained_in_any(ranges: list[tuple[int, int]], in_id: int) -> bool:
    return any(_is_contained(_, in_id) for _ in ranges)


def solve_a(in_str: str) -> int:
    ranges, ids = _parse_input(in_str)
    return sum(1 for id in ids if _is_contained_in_any(ranges, id))


def _number_of_elements(start: int, end: int) -> int:
    assert start <= end
    return end - start + 1


def _number_of_elements_in_union(ranges: list[tuple[int, int]]) -> int:
    cur_start = 1
    cur_end = 1
    res = -1
    for start, end in sorted(ranges):
        if cur_start <= start <= cur_end:
            cur_end = max(end, cur_end)
        else:
            res += _number_of_elements(cur_start, cur_end)
            cur_start = start
            cur_end = end
    res += _number_of_elements(cur_start, cur_end)
    return res


def solve_b(in_str: str) -> int:
    return _number_of_elements_in_union(_parse_input(in_str)[0])
