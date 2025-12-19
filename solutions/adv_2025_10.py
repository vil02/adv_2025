import z3  # type: ignore


def _parse_button(in_str: str) -> list[int]:
    assert in_str.startswith("(")
    assert in_str.endswith(")")
    positions = in_str[1:-1].split(",")
    return [int(_) for _ in positions]


def _parse_buttons(buttons: list[str]) -> list[list[int]]:
    return [_parse_button(_) for _ in buttons]


def _parse_target(in_str: str) -> str:
    assert in_str.startswith("[")
    assert in_str.endswith("]")
    return in_str[1:-1]


def _parse_joltages(in_str: str) -> tuple[int, ...]:
    assert in_str.startswith("{")
    assert in_str.endswith("}")
    return tuple(int(_) for _ in in_str[1:-1].split(","))


def _assert_fit(buttons: list[list[int]], target_len: int) -> None:
    assert all(0 <= max(_) < target_len for _ in buttons)


def _parse_machine(
    in_str: str,
) -> tuple[str, list[list[int]], tuple[int, ...]]:
    pieces = in_str.split()
    target = _parse_target(pieces[0])
    buttons = _parse_buttons(pieces[1:-1])
    joltages = _parse_joltages(pieces[-1])
    _assert_fit(buttons, min(len(target), len(joltages)))
    return target, buttons, joltages


def _parse_input(
    in_str: str,
) -> list[tuple[str, list[list[int]], tuple[int, ...]]]:
    return [_parse_machine(_) for _ in in_str.splitlines()]


def _minimal_number_of_presses_a(target: str, buttons: list[list[int]]) -> int:
    opt = z3.Optimize()
    presses = []
    for b_num in range(len(buttons)):
        press = z3.Int(f"p_{b_num}")
        opt.add(press >= 0)
        presses.append(press)
    opt.minimize(sum(presses))

    for num, goal in enumerate(target):
        this_sum = []
        for b_num, button in enumerate(buttons):
            if num in button:
                this_sum.append(presses[b_num])
        opt.add(sum(this_sum) % 2 == {".": 0, "#": 1}[goal])

    assert opt.check() == z3.sat
    model = opt.model()
    return sum(model[press].as_long() for press in presses)


def solve_a(in_str: str) -> int:
    data = _parse_input(in_str)
    return sum(
        _minimal_number_of_presses_a(target, buttons) for target, buttons, _ in data
    )


def _minimal_number_of_presses_b(
    target: tuple[int, ...], buttons: list[list[int]]
) -> int:
    opt = z3.Optimize()
    presses = []
    for b_num in range(len(buttons)):
        press = z3.Int(f"p_{b_num}")
        opt.add(press >= 0)
        presses.append(press)
    opt.minimize(sum(presses))

    for num, goal in enumerate(target):
        this_sum = []
        for b_num, button in enumerate(buttons):
            if num in button:
                this_sum.append(presses[b_num])
        opt.add(sum(this_sum) == goal)

    assert opt.check() == z3.sat
    model = opt.model()
    return sum(model[press].as_long() for press in presses)


def solve_b(in_str: str) -> int:
    data = _parse_input(in_str)
    return sum(
        _minimal_number_of_presses_b(target, buttons) for _, buttons, target in data
    )
