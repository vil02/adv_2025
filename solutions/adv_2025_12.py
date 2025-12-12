Present = set[tuple[int, int]]


def _parse_present_index(in_str: str) -> int:
    assert in_str.endswith(":")
    return int(in_str[:-1])


def _parse_present_shape(in_lines: list[str]) -> Present:
    res = set()
    for y_pos, line in enumerate(in_lines):
        for x_pos, char in enumerate(line):
            if char == "#":
                res.add((x_pos, y_pos))
    return res


def _parse_present(in_str: str) -> tuple[int, Present]:
    pieces = in_str.splitlines()
    return _parse_present_index(pieces[0]), _parse_present_shape(pieces[1:])


def _parse_presents(in_presents: list[str]) -> dict[int, Present]:
    return dict(_parse_present(_) for _ in in_presents)


def _parse_presents_list(in_str: str) -> list[int]:
    return [int(_) for _ in in_str.split()]


def _parse_size_str(in_str: str) -> tuple[int, int]:
    x_size, y_size = in_str.split("x")
    return int(x_size), int(y_size)


def _parse_region(in_str: str) -> tuple[tuple[int, int], list[int]]:
    size_str, presents = in_str.split(": ")
    return _parse_size_str(size_str), _parse_presents_list(presents)


def _parse_regions(in_str: str) -> list[tuple[tuple[int, int], list[int]]]:
    return [_parse_region(_) for _ in in_str.splitlines()]


def _parse_input(
    in_str: str,
) -> tuple[dict[int, Present], list[tuple[tuple[int, int], list[int]]]]:
    pieces = in_str.split("\n\n")
    return _parse_presents(pieces[:-1]), _parse_regions(pieces[-1])


def _present_area(in_present: Present) -> int:
    return len(in_present)


def _area(size: tuple[int, int]) -> int:
    return size[0] * size[1]


def _needed_area(needed_presents: list[int], presents: dict[int, Present]) -> int:
    return sum(
        _n * _present_area(presents[_p]) for _p, _n in enumerate(needed_presents)
    )


def _does_fit_simple(
    size: tuple[int, int], needed_presents: list[int], presents: dict[int, Present]
) -> bool:
    return _needed_area(needed_presents, presents) <= _area(size)


def solve_a(in_str: str) -> int:
    presents, regions = _parse_input(in_str)
    return sum(1 for region in regions if _does_fit_simple(*region, presents))
