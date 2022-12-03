from string import ascii_letters

from more_itertools import batched
from more_itertools import one

from advent.load import read_input


def priority(c: str) -> int:
    return ascii_letters.index(c) + 1


rucksacks = []
shared = 0

for line in read_input():
    len_line = len(line)
    rucksacks.append(set(line))
    shared += priority(
        one(set(line[: len(line) // 2]).intersection(line[len(line) // 2 :]))
    )

print(shared)
print(sum(priority(one(set.intersection(*g))) for g in batched(rucksacks, 3)))
