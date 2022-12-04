from string import ascii_uppercase, ascii_lowercase
from typing import List, Set

import file_formats
from file_formats import blue, red, white, the_arrow, escape

letters: str = ascii_uppercase + ascii_lowercase

with open("2022\\rucksack.txt") as file:
    rucksacks: List[str] = [
        content for content in file.read().strip().split("\n")]

total_sum: int = 0
common_items: Set[str] = {}

# Part 1
for items in rucksacks:
    first_compartment: str = items[:len(items) // 2]
    second_compartment: str = items[len(items) // 2:]
    common_items = set(first_compartment).intersection(second_compartment)

    for item in common_items:
        if item in ascii_lowercase:
            total_sum += ord(item) - ord("a") + 1
        if item in ascii_uppercase:
            total_sum += ord(item) - ord("A") + 27

print(
    f"{the_arrow}{white} The sum of the {blue}priorities{white} of the items are: {red}{total_sum}{escape}[0m")


# Part 2
with open("2022\\rucksack.txt") as file:
    data = file.read().split("\n")

group_sum: int = 0

for alpha in range(0, len(data), 3):
    group: Set[str] = set(letters)
    for beta in range(alpha, alpha + 3):
        group = group.intersection(set(data[beta]))

    for letter in group:
        if letter in ascii_lowercase:
            group_sum += ord(letter) - ord("a") + 1
        if letter in ascii_uppercase:
            group_sum += ord(letter) - ord("A") + 27

print(
    f"{the_arrow}{white} The sum of the {blue}group priorities{white} of the items are: {red}{group_sum}{escape}[0m")
