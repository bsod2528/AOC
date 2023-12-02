import re
from os import name, system
from typing import Dict, List

import file_formats
from file_formats import blue, red, the_arrow, white

system("cls" if name == "nt" else "clear")


def digit_converter(word: str) -> str:
    return number_dict.get(word, word)


number_dict: Dict[str, str] = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


with open("2023\\day_1.txt") as file:
    calib_list: List[str] = [num for num in file.read().split("\n")]

num_list: List[int] = [re.findall("[0-9]+", x) for x in calib_list]
first: List[str] = [x[0][0] for x in num_list]
last: List[str] = [x[-1][-1] for x in num_list]
total: List[int] = [int(x + y) for x, y in zip(first, last)]

actual_total: int = 0

for line in calib_list:
    iterator = re.finditer(r"(?=(\d|" + "|".join(number_dict) + r"))", line)

    first_match, *rest = iterator
    last_match = rest[-1] if rest else first_match

    first: str = digit_converter(first_match.group(1))
    last: str = digit_converter(last_match.group(1))

    actual_total += int(first + last)

print(f"{the_arrow}{white} sum of all calibration values is: {red}{sum(total)}")
print(f"{the_arrow}{white} actual sum of all calibration value is: {red}{actual_total}")
