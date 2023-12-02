import enum
from itertools import product
from typing import List, Set

import file_formats
from file_formats import blue, escape, red, the_arrow, white

matrix = List[List[int]]

with open(f"2022\\tree_heights.txt") as file:
    heights: str = file.read()


class Location(enum.Enum):
    TOP = enum.auto()
    RIGHT = enum.auto()
    BOTTOM = enum.auto()
    LEFT = enum.auto()


def return_list(data: str) -> matrix:
    return [list(map(int, list(row))) for row in data.split("\n")]


def item_visibility(matrix: matrix, x: int, y: int) -> Set[Location]:
    row: List[int] = matrix[y]
    column: List[int] = [s[x] for s in matrix]
    cell: int = row[x]

    visible_from: Set[Location] = set()

    if x == 0:
        visible_from.add(Location.LEFT)

    if x == len(matrix[0]) - 1:
        visible_from.add(Location.RIGHT)

    if y == 0:
        visible_from.add(Location.TOP)

    if y == len(matrix) - 1:
        visible_from.add(Location.BOTTOM)

    if all(c < cell for c in row[:x]):
        visible_from.add(Location.LEFT)

    if all(c < cell for c in row[x + 1 :]):
        visible_from.add(Location.RIGHT)

    if all(c < cell for c in column[:y]):
        visible_from.add(Location.TOP)

    if all(c < cell for c in column[y + 1 :]):
        visible_from.add(Location.BOTTOM)
    return visible_from


def visibile_items(matrix: matrix) -> int:
    rows: int = len(matrix)
    columns: int = len(matrix[0])
    coordinates = product(range(rows), range(columns))
    return len([(x, y) for x, y in coordinates if item_visibility(matrix, x, y)])


def scenic_score(matrix: matrix, x: int, y: int) -> int:
    row: List[int] = matrix[y]
    column: List[int] = [s[x] for s in matrix]
    cell: int = row[x]

    def calculate_score(trees: list[int]) -> int:
        score = 0
        for item in trees:
            score += 1
            if item >= cell:
                break
        return score

    left_score: int = calculate_score(row[:x][::-1])
    right_score: int = calculate_score(row[x + 1 :])
    top_score: int = calculate_score(column[:y][::-1])
    bottom_score: int = calculate_score(column[y + 1 :])
    return top_score * right_score * bottom_score * left_score


def return_scenic_score(matrix: matrix) -> List[int]:
    rows: int = len(matrix)
    columns: int = len(matrix[0])
    coordinates = product(range(rows), range(columns))
    return [scenic_score(matrix, x, y) for x, y in coordinates]


print(
    f"{the_arrow}{white} Therefore, the total number of trees visible {blue}from outside the grid{white} is: {red}{visibile_items(return_list(heights))}{escape}[0m"
)
print(
    f"{the_arrow}{white} Therefore, the highest possible {blue}scenic score{white} is: {red}{max(return_scenic_score(return_list(heights)))}{escape}[0m"
)
