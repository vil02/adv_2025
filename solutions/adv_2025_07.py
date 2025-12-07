import collections


def _parse_input(
    in_str: str,
) -> tuple[set[tuple[int, int]], tuple[int, int], int]:
    lines = in_str.splitlines()
    splitters = set()
    start_pos = None
    for y_pos, line in enumerate(lines):
        for x_pos, char in enumerate(line):
            if char == "S":
                assert start_pos is None
                start_pos = (x_pos, y_pos)
            elif char == "^":
                assert 0 < x_pos < len(line) - 1
                splitters.add((x_pos, y_pos))
    assert start_pos is not None
    return splitters, start_pos, len(lines)


def _next_beam_a(
    splitters: set[tuple[int, int]], beams: set[int], y_pos: int
) -> tuple[set[int], int, int]:
    new_y = y_pos + 1
    new_beams = set()
    splits = 0
    for beam in beams:
        if (beam, new_y) in splitters:
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
            splits += 1
        else:
            new_beams.add(beam)
    return new_beams, splits, new_y


def solve_a(in_str: str) -> int:
    splitters, start_pos, y_size = _parse_input(in_str)
    y_pos = start_pos[1]
    beams = {start_pos[0]}
    splits = 0
    while y_pos < y_size:
        beams, new_splits, y_pos = _next_beam_a(splitters, beams, y_pos)
        splits += new_splits
    return splits


def _next_beam_b(
    splitters: set[tuple[int, int]], beams: dict[int, int], y_pos: int
) -> tuple[dict[int, int], int]:
    new_y = y_pos + 1
    new_beams: dict[int, int] = collections.defaultdict(int)
    for beam, val in beams.items():
        if (beam, new_y) in splitters:
            new_beams[beam - 1] += val
            new_beams[beam + 1] += val
        else:
            new_beams[beam] += val

    return new_beams, new_y


def solve_b(in_str: str) -> int:
    splitters, start_pos, y_size = _parse_input(in_str)
    y_pos = start_pos[1]
    beams = {start_pos[0]: 1}
    while y_pos < y_size:
        beams, y_pos = _next_beam_b(splitters, beams, y_pos)
    return sum(beams.values())
