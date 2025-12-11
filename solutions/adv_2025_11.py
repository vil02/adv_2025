import functools


def _parse_targets(in_str: str) -> list[str]:
    return in_str.split()


def _parse_line(in_str: str) -> tuple[str, list[str]]:
    source, targets = in_str.split(": ")
    return source, _parse_targets(targets)


def _parse_input(in_str: str) -> dict[str, list[str]]:
    res = {}
    for _ in in_str.splitlines():
        source, targets = _parse_line(_)
        assert source not in res
        res[source] = targets
    return res


def _number_of_paths(graph: dict[str, list[str]], start: str, end: str) -> int:

    @functools.lru_cache(None)
    def _inner(cur_node: str) -> int:
        if cur_node == end:
            return 1
        if cur_node == "out":
            return 0
        return sum(_inner(_) for _ in graph[cur_node])

    return _inner(start)


def solve_a(in_str: str) -> int:
    return _number_of_paths(_parse_input(in_str), "you", "out")


def _number_of_paths_visiting(
    graph: dict[str, list[str]], start: str, visit_a: str, visit_b: str, end: str
) -> int:
    assert _number_of_paths(graph, visit_b, visit_a) == 0
    return (
        _number_of_paths(graph, start, visit_a)
        * _number_of_paths(graph, visit_a, visit_b)
        * _number_of_paths(graph, visit_b, end)
    )


def solve_b(in_str: str) -> int:
    return _number_of_paths_visiting(_parse_input(in_str), "svr", "fft", "dac", "out")
