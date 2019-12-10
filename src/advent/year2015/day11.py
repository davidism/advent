from more_itertools import pairwise
from more_itertools import windowed


def inc(value):
    cs = [ord(c) - 97 for c in reversed(value)]

    for i, c in enumerate(cs):
        carry, cs[i] = divmod(c + 1, 26)

        if not carry:
            break

    return "".join(chr(c + 97) for c in reversed(cs))


def is_valid(value):
    return (
        not set(value) & {"i", "o", "l"}
        and any(x + 1 == y and y + 1 == z for x, y, z in windowed(map(ord, value), 3))
        and len(set(x for x, y in pairwise(value) if x == y)) > 1
    )


def next_valid(value):
    while True:
        value = inc(value)

        if is_valid(value):
            return value


p1 = next_valid("hepxcrrq")
print(p1)
print(next_valid(p1))
