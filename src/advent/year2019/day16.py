from itertools import accumulate
from itertools import cycle
from itertools import repeat
from test.test_itertools import take

from more_itertools import dotproduct
from more_itertools import flatten

from advent.load import read_input


def next_phase(value, offset=False):
    back_half = (x % 10 for x in accumulate(reversed(value)))

    if offset:
        return list(reversed(list(back_half)))

    half = len(value) // 2
    out = take(half, back_half)

    for i in range(half):
        pattern = cycle(flatten((repeat(x, half - i) for x in [0, 1, 0, -1])))
        next(pattern)
        out.append(abs(dotproduct(value, pattern)) % 10)

    return list(reversed(out))


def n_phases(value, n, offset=0):
    if offset:
        value = value[offset:]

    for _ in range(n):
        value = next_phase(value, offset > 0)

    return value


data = [int(x) for x in read_input()]
print("".join(str(x) for x in n_phases(data, 100)[:8]))
offset = int("".join(str(x) for x in data[:7]))
data *= 10000
print("".join(str(x) for x in n_phases(data, 100, offset)[:8]))
