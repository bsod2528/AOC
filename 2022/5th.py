import re
from collections import defaultdict
from typing import DefaultDict

import file_formats
from file_formats import blue, escape, red, the_arrow, white

cratemover_9000: DefaultDict = defaultdict(list)

for line in open("2022\\crates.txt"):
    if "[" in line:
        for char in range(1, len(line) - 1, 4):
            if line[char] != " ":
                cratemover_9000[(char - 1) // 4].append(line[char])
    elif line.startswith("move"):
        alpha, beta, gamma = map(int, re.findall(r"\d+", line))
        cratemover_9000[gamma - 1] = (
            cratemover_9000[beta - 1][:alpha][::-1] + cratemover_9000[gamma - 1]
        )
        cratemover_9000[beta - 1] = cratemover_9000[beta - 1][alpha:]

print(
    f"{the_arrow}{white} Therefore after rearranging using the {blue}Cratemover 9000{white} the order of crates which are at the top are: {red}"
    + "".join(cratemover_9000[i][0] for i in range(len(cratemover_9000)))
    + f"{escape}[0m"
)


cratemover_9001: DefaultDict = defaultdict(list)

for line in open("2022\\crates.txt"):
    if "[" in line:
        for i in range(1, len(line) - 1, 4):
            if line[i] != " ":
                cratemover_9001[(i - 1) // 4].append(line[i])
    elif line.startswith("move"):
        delta, epsilon, zeta = map(int, re.findall(r"\d+", line))
        cratemover_9001[zeta - 1] = (
            cratemover_9001[epsilon - 1][:delta] + cratemover_9001[zeta - 1]
        )
        cratemover_9001[epsilon - 1] = cratemover_9001[epsilon - 1][delta:]

print(
    f"{the_arrow}{white} Therefore after rearranging using the {blue}Cratemover 9001{white} the order of crates which are at the top are: {red}"
    + "".join(cratemover_9001[i][0] for i in range(len(cratemover_9001)))
    + f"{escape}[0m"
)
