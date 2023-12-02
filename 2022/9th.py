from typing import Any, Dict, List, Literal, Set, TextIO, Tuple

import file_formats
from file_formats import blue, escape, red, the_arrow, white


def assertions() -> None:
    head: Tuple[Literal, Literal] = (0, 0)

    assert move((0, 0), (1, 1)) == (1, 1)
    assert move((3, 5), (2, 4)) == (5, 9)

    assert (v := get_updated_position((0, 0), head)) == (0, 0), v
    assert (v := get_updated_position((-1, 0), head)) == (-1, 0), v
    assert (v := get_updated_position((0, 1), head)) == (0, 1), v

    assert (v := get_updated_position((2, 1), head)) == (1, 0), v
    assert (v := get_updated_position((-2, -1), head)) == (-1, 0), v
    assert (v := get_updated_position((-1, -2), head)) == (0, -1), v

    assert (v := get_updated_position((2, 0), head)) == (1, 0), v
    assert (v := get_updated_position((-2, 0), head)) == (-1, 0), v
    assert (v := get_updated_position((0, -2), head)) == (0, -1), v

    assert (v := get_updated_position((0, 0), (2, 0))) == (1, 0), v
    assert (v := get_updated_position((8, 10), (10, 10))) == (9, 10), v

    assert iterate_rope([3, 3, 3, 3]) == ((2, 3), (1, 2), (0, 1))


def iterate_rope(rope: List) -> Tuple:
    return tuple((i - 1, i) for i in range(len(rope) - 1, 0, -1))


def get_updated_position(updating_node: Tuple, target_node: Tuple) -> Tuple:
    ux, uy = updating_node
    tx, ty = target_node

    delta_x = tx - ux
    delta_y = ty - uy

    if abs(delta_x) <= 1 and abs(delta_y) <= 1:
        return updating_node

    if delta_y == 0:
        return (ux + delta_x // 2, uy)

    if delta_x == 0:
        return (ux, uy + delta_y // 2)
    return (ux + 1 * delta_x / abs(delta_x), uy + 1 * delta_y / abs(delta_y))


def get_instructions(path: TextIO) -> List:
    instructions: List[Any] = []
    deltas: Dict[str, Any] = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    with open(path) as file:
        for line in file.read().strip().split("\n"):
            direction, quantity = line.split(" ")
            instructions.append((deltas[direction], int(quantity)))
    return instructions


def return_answer(instructions: List, rope_length: int) -> int:
    visited: Set[Tuple[Literal, Literal]] = {(0, 0)}
    rope: List[Tuple[Literal, Literal]] = [(0, 0)]

    for delta, quantity in instructions:
        for x in range(quantity):
            rope[-1] = move(rope[-1], delta)

            for p1, p2 in iterate_rope(rope):
                rope[p1] = get_updated_position(rope[p1], rope[p2])

            if rope[0] != (0, 0) and len(rope) < rope_length:
                rope = [(0, 0)] + rope

            visited.add(rope[0])
    return len(visited)


def move(vector1: Tuple, vector2: Tuple) -> Tuple:
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])


plank_length: List[str] = get_instructions("2022\\plank_length.txt")
assertions()


print(
    f"{the_arrow}{white} Therefore, the number of positions in which the tail of the rope visited once is{blue} hypothetically{white}: {red}{return_answer(plank_length, 2)}{escape}[0m"
)
print(
    f"{the_arrow}{white} Therefore, the number of positions in which the tail of the rope visited once {blue}with a larger rope with more than 10 knots{white} is: {red}{return_answer(plank_length, 10)}{escape}[0m"
)
