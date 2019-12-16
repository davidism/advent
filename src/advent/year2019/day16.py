from itertools import accumulate
from itertools import chain
from itertools import cycle
from itertools import repeat
from test.test_itertools import take

from more_itertools import dotproduct
from more_itertools import flatten

from advent.load import read_input


def next_phase(value, offset=False):
    size = len(value)
    half = size // 2
    out = take(half, (x % 10 for x in accumulate(reversed(value))))

    if offset:
        return list(chain(value[:half], reversed(out)))

    for i in range(half):
        pattern = cycle(flatten((repeat(x, half - i) for x in [0, 1, 0, -1])))
        next(pattern)
        out.append(abs(dotproduct(value, pattern)) % 10)

    return list(reversed(out))


def n_phases(value, n, offset=False):
    for _ in range(n):
        print(_)
        value = next_phase(value, offset)

    return value


data = [int(x) for x in read_input()]
print("".join(str(x) for x in n_phases(data, 100)[:8]))
offset = int("".join(str(x) for x in data[:7]))
data *= 10000
print("".join(str(x) for x in n_phases(data, 100, True)[offset : offset + 8]))
