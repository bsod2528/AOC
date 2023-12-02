from typing import Dict, List

import file_formats
from file_formats import blue, escape, red, the_arrow, white

with open("2022\\rps.txt") as file:
    strategy_list: List[str] = [x for x in file.read().strip().split("\n")]

# Part 1
partial_outcomes: Dict[str, int] = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

total_score: int = 0
for game in strategy_list:
    total_score += partial_outcomes[game]
print(
    f"{the_arrow}{white} Therefore, we will be getting a total of {red}{total_score}{white} considering the fact we are {blue}assuming{white} the strategy.{escape}[0m"
)


# Part 2
actual_outcomes: Dict[str, int] = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

total_score: int = 0
for game in strategy_list:
    total_score += actual_outcomes[game]
print(
    f"{the_arrow}{white} Therefore, we will be getting a total of {red}{total_score}{white} considering the fact we are going as {blue}per the accurate{white} strategy.{escape}[0m"
)
