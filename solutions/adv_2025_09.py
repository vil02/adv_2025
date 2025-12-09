import itertools

from shapely.geometry import Polygon, box
from shapely.prepared import prep

Pos = tuple[int, int]


def _parse_line(in_line: str) -> Pos:
    res = tuple(int(_) for _ in in_line.split(","))
    assert len(res) == 2
    return res


def _parse_input(in_str: str) -> list[Pos]:
    return [_parse_line(_) for _ in in_str.splitlines()]


def _min_max(val_a: int, val_b: int) -> tuple[int, int]:
    return min(val_a, val_b), max(val_a, val_b)


def _to_box(pos_a: Pos, pos_c: Pos) -> tuple[int, int, int, int]:
    min_x, max_x = _min_max(pos_a[0], pos_c[0])
    min_y, max_y = _min_max(pos_a[1], pos_c[1])
    return min_x, min_y, max_x, max_y


def _area(pos_a: Pos, pos_c: Pos) -> int:
    min_x, min_y, max_x, max_y = _to_box(pos_a, pos_c)
    return (1 + max_x - min_x) * (1 + max_y - min_y)


def solve_a(in_str: str) -> int:
    positions = sorted(_parse_input(in_str))
    return max(
        _area(pos_a, pos_c) for pos_a, pos_c in itertools.combinations(positions, 2)
    )


def solve_b(in_str: str) -> int:
    positions = _parse_input(in_str)
    all_polygon = prep(Polygon(positions))
    return max(
        _area(pos_a, pos_c)
        for pos_a, pos_c in itertools.combinations(positions, 2)
        if all_polygon.contains(box(*_to_box(pos_a, pos_c)))
    )
