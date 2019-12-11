import operator
import re

from advent.load import read_input

detect = {
    "children": (3, operator.eq),
    "cats": (7, operator.gt),
    "samoyeds": (2, operator.eq),
    "pomeranians": (3, operator.lt),
    "akitas": (0, operator.eq),
    "vizslas": (0, operator.eq),
    "goldfish": (5, operator.lt),
    "trees": (3, operator.gt),
    "cars": (2, operator.eq),
    "perfumes": (1, operator.eq),
}
data = list(
    enumerate(
        (
            [(k, int(v)) for k, v in re.findall(r" (\w+): (\d+)", line)]
            for line in read_input()
        ),
        1,
    )
)
print(next(i for i, things in data if all(detect[k][0] == v for k, v, in things)))
print(
    next(
        i for i, things in data if all(detect[k][1](v, detect[k][0]) for k, v in things)
    )
)
