from collections import defaultdict
from typing import DefaultDict, List

import file_formats
from file_formats import blue, escape, red, the_arrow, white

with open("2022\\directory.txt") as file:
    lines: List = [commands for commands in file.read().split("\n")]

path: List = []
directory: DefaultDict = defaultdict(int)

for command in lines:
    cli_input = command.strip().split()

    if cli_input[1] == "cd":
        if cli_input[2] == "..":
            path.pop()
        else:
            path.append(cli_input[2])

    elif cli_input[1] == "ls":
        continue

    elif cli_input[0] == "dir":
        continue

    else:
        size: int = int(cli_input[0])
        for alpha in range(1, len(path) + 1):
            directory["/".join(path[:alpha])] += size

max_used: int = 70000000 - 30000000
total_used: int = directory["/"]
need_to_free: int = total_used - max_used

used_space: int = 0
smallest_dir: int = 1e9

for key, value in directory.items():
    if value <= 100000:
        used_space += value
    if value >= need_to_free:
        smallest_dir = min(smallest_dir, value)

print(
    f"{the_arrow}{white} The amount of used space {blue}before freeing up{white} the disk was: {red}{used_space}{escape}[0m"
)
print(
    f"{the_arrow}{white} The amount of space occupied by the {blue}smallest directory{white} was: {red}{smallest_dir}{escape}[0m"
)
