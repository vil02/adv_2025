import collections
import functools
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


def _connect(circuits: dict[Pos, int], pos_a: Pos, pos_b: Pos) -> None:
    if circuits[pos_a] != circuits[pos_b]:
        circuit_b = circuits[pos_b]
        for pos in circuits:
            if circuits[pos] == circuit_b:
                circuits[pos] = circuits[pos_a]


def _top_3(circuits: dict[Pos, int]) -> list[int]:
    counter = collections.Counter(circuits.values())
    x = sorted(counter.values(), reverse=True)

    return x[:3]


def _score(circuits: dict[Pos, int]) -> int:
    return functools.reduce(lambda _a, _b: _a * _b, _top_3(circuits))


def _limit(positions: list[Pos]) -> int:
    if len(positions) == 20:
        return 10
    return 1000


def solve_a(in_str: str) -> int:
    positions = _parse_input(in_str)
    circuits = {_p: _n for _n, _p in enumerate(positions)}
    connections = _sort_by_dist(positions)[: _limit(positions)]
    for _ in connections:
        _connect(circuits, *_)

    return _score(circuits)


def _are_connected(circuits: dict[Pos, int]) -> bool:
    return len(set(circuits.values())) == 1


def solve_b(in_str: str) -> int:
    positions = _parse_input(in_str)
    circuits = {_p: _n for _n, _p in enumerate(positions)}
    connections = _sort_by_dist(positions)
    connecting = None
    for _ in connections:
        _connect(circuits, *_)
        if _are_connected(circuits):
            connecting = _
            break
    assert connecting is not None
    return connecting[0][0] * connecting[1][0]
