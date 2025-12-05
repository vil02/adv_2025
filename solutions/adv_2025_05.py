def _parse_id(in_str: str) -> int:
    return int(in_str)


def _parse_range(in_str: str) -> tuple[int, int]:
    start, end = (_parse_id(_) for _ in in_str.split("-"))
    assert start <= end
    return start, end


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


def _do_overlap(last_range: tuple[int, int], next_range: tuple[int, int]) -> bool:
    return last_range[0] <= next_range[0] <= last_range[1]


def _join(last_range: tuple[int, int], next_range: tuple[int, int]) -> tuple[int, int]:
    assert _do_overlap(last_range, next_range)
    return last_range[0], max(next_range[1], last_range[1])


def _merge(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    res = []
    sorted_ranges = sorted(ranges)
    last_range = sorted_ranges[0]
    for cur_range in sorted_ranges[1:]:
        if _do_overlap(last_range, cur_range):
            last_range = _join(last_range, cur_range)
        else:
            res.append(last_range)
            last_range = cur_range
    res.append(last_range)
    return res


def solve_a(in_str: str) -> int:
    ranges, ids = _parse_input(in_str)
    ranges = _merge(ranges)
    return sum(1 for id in ids if _is_contained_in_any(ranges, id))


def _number_of_elements(start: int, end: int) -> int:
    assert start <= end
    return end - start + 1


def _assert_merged(merged_ranges: list[tuple[int, int]]) -> None:
    assert merged_ranges == sorted(merged_ranges)
    for _prev, _next in zip(merged_ranges[:-1], merged_ranges[1:], strict=True):
        assert _prev[1] < _next[0]


def _number_of_elements_in_merged(merged_ranges: list[tuple[int, int]]) -> int:
    _assert_merged(merged_ranges)
    return sum(_number_of_elements(*_) for _ in merged_ranges)


def solve_b(in_str: str) -> int:
    return _number_of_elements_in_merged(_merge(_parse_input(in_str)[0]))
