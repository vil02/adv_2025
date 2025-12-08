import itertools

Pos = tuple[int, int, int]


def _parse_line(in_str: str) -> Pos:
    res = tuple(int(_) for _ in in_str.split(","))
    assert len(res) == 3
    return res


def _parse_input(in_str: str) -> list[Pos]:
    return [_parse_line(_) for _ in in_str.splitlines()]


def _dist_2(pos_a: Pos, pos_b: Pos) -> int:
    return sum((_a - _b) ** 2 for _a, _b in zip(pos_a, pos_b, strict=True))


def _sort_by_dist(positions: list[Pos]) -> list[tuple[Pos, Pos]]:
    return sorted(itertools.combinations(positions, 2), key=lambda _: _dist_2(*_))


def _connect(
    circuits: dict[Pos, int], components: dict[int, list[Pos]], pos_a: Pos, pos_b: Pos
) -> None:
    if circuits[pos_a] != circuits[pos_b]:
        circuit_a = circuits[pos_a]
        circuit_b = circuits[pos_b]
        for pos in components[circuit_b]:
            circuits[pos] = circuit_a
        components[circuits[pos_a]].extend(components[circuit_b])
        del components[circuit_b]


def _top_3(components: dict[int, list[Pos]]) -> tuple[list[Pos], list[Pos], list[Pos]]:
    comp_a, comp_b, comp_c = sorted(components.values(), key=len, reverse=True)[:3]
    return comp_a, comp_b, comp_c


def _score_a(components: dict[int, list[Pos]]) -> int:
    comp_a, comp_b, comp_c = _top_3(components)
    return len(comp_a) * len(comp_b) * len(comp_c)


def _limit(positions: list[Pos]) -> int:
    if len(positions) == 20:
        return 10
    return 1000


def _initial_info(positions: list[Pos]) -> tuple[dict[Pos, int], dict[int, list[Pos]]]:
    circuits = {_p: _n for _n, _p in enumerate(positions)}
    components = {_n: [_p] for _n, _p in enumerate(positions)}
    return circuits, components


def solve_a(in_str: str) -> int:
    positions = _parse_input(in_str)
    circuits, components = _initial_info(positions)
    for _ in _sort_by_dist(positions)[: _limit(positions)]:
        _connect(circuits, components, *_)
    return _score_a(components)


def _are_connected(components: dict[int, list[Pos]]) -> bool:
    return len(components) == 1


def _score_b(pos_a: Pos, pos_b: Pos) -> int:
    return pos_a[0] * pos_b[0]


def solve_b(in_str: str) -> int:
    positions = _parse_input(in_str)
    circuits, components = _initial_info(positions)
    connecting = None
    for _ in _sort_by_dist(positions):
        _connect(circuits, components, *_)
        if _are_connected(components):
            connecting = _
            break
    assert connecting is not None
    return _score_b(*connecting)
