from os import system
from typing import Dict, List, Any

import file_formats
from file_formats import the_arrow, white, escape, red, blue


# All hail Zeus432 for this part :worship:
with open("2022\\elf_calorie.txt") as file:
    print(type(file))
    elf_dict: Dict[int,
                   List[Any]] = {i + 1: [int(f) for f in x.split("\n")] for i,
                                 x in enumerate(file.read().strip().split("\n\n"))}

calorie_list: List[int] = []

for calories in elf_dict.values():
    calorie_list.append(sum(calories))

calorie_list.sort()
highest_calorie: int = calorie_list[-1]

second_highest: int = calorie_list[-2]
third_highest: int = calorie_list[-3]

system("cls")

for key, value in elf_dict.items():
    suffix: str
    stringed_key: str = str(key)
    if stringed_key.endswith("1"):
        suffix = "st"
    if stringed_key.endswith("2"):
        suffix = "nd"
    if stringed_key.endswith("3"):
        suffix = "rd"
    if stringed_key.endswith(("4", "5", "6", "7", "8", "9", "0")):
        suffix = "nd"
    if sum(value) == highest_calorie:
        print(
            f"{the_arrow}{white} Therefore, the Elves should go and ask {blue}{key}{suffix} Elf{escape}[0m{white} as they have the highest calorie of: {red}{highest_calorie} {escape}[0m")
    if sum(value) == second_highest:
        print(
            f"{the_arrow}{white} Therefore, the Elves should go and ask {blue}{key}{suffix} Elf{escape}[0m{white} as they have the highest calorie of: {red}{second_highest} {escape}[0m")
    if sum(value) == third_highest:
        print(
            f"{the_arrow}{white} Therefore, the Elves should go and ask {blue}{key}{suffix} Elf{escape}[0m{white} as they have the highest calorie of: {red}{third_highest} {escape}[0m")

print(f"{the_arrow}{white} And the total calories by those three is {red}{highest_calorie + second_highest + third_highest}{escape}[0m")

