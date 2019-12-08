from more_itertools import pairwise
from more_itertools import run_length
from more_itertools import windowed

from advent.load import read_input


def is_nice(value):
    pairs = set("".join(pair) for pair in pairwise(value))
    return (
        not pairs & {"ab", "cd", "pq", "xy"}
        and any(x == y for x, y in pairs)
        and sum(1 for c in value if c in {"a", "e", "i", "o", "u"}) >= 3
    )


def is_nicer(value):
    if not any(x == z for x, y, z in windowed(value, 3)):
        return False

    seen = set()

    for pair, run in run_length.encode(pairwise(value)):
        if run > 2 or pair in seen:
            return True

        seen.add(pair)


data = read_input()
print(sum(1 for v in data if is_nice(v)))
print(sum(1 for v in data if is_nicer(v)))
