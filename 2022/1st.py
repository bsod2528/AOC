from os import system
from typing import Dict, List, Any

escape: str = "\x1b"
red: str = f"{escape}[0;1;31m"
blue: str = f"{escape}[0;1;34m"
white: str = f"{escape}[0;1;37m"
the_arrow: str = f"{escape}[0;1;37;40m > "

# All hail Zeus432 for this part :worship:
with open("2022\\elves.txt") as file:
    elf_dict: Dict[int,
                   List[Any]] = {i + 1: [int(f) for f in x.split("\n")] for i,
                                 x in enumerate(file.read().strip().split("\n\n"))}

calorie_list: List[int] = []

for calories in elf_dict.values():
    calorie_list.append(sum(calories))

calorie_list.sort()
highest_calorie: int = calorie_list[-1]

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
