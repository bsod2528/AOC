
from typing import List

import file_formats
from file_formats import blue, red, white, the_arrow, escape

with open("2022\\assignments.txt") as file:
    pairs: List[str] = [pair.strip() for pair in file.read().split("\n")]


ranges_contained: int = 0
ranges_overlapped: int = 0


for pair in pairs:
    range_one, range_two = pair.split(",")
    left_one, left_two = range_one.split("-")
    right_one, right_two = range_two.split("-")

    left_one, left_two, right_one, right_two = [
        int(integer) for integer in [left_one, left_two, right_one, right_two]]

    if (left_one <= right_one and right_two <= left_two) or (
            right_one <= left_one and left_two <= right_two):
        ranges_contained += 1

    if not (left_two < right_one or right_two < left_one):
        ranges_overlapped += 1

print(
    f"{the_arrow}{white} In {red}{ranges_contained}{white} assignment pairs, the ranges are {blue}fully contained{escape}[0m")
print(
    f"{the_arrow}{white} In {red}{ranges_overlapped}{white} assignment pairs, the ranges are {blue}overlapped{escape}[0m")
