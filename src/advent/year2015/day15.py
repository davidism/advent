import re
from functools import reduce
from itertools import product
from operator import mul

from more_itertools import dotproduct

from advent.load import read_input


def max_score(lines):
    *props, cals = zip(*(map(int, re.findall(r"-?\d+", line)) for line in lines))
    best = 0
    best_cals = 0

    for sizes in (x for x in product(range(101), repeat=4) if sum(x) == 100):
        score = reduce(mul, (max(0, dotproduct(sizes, prop)) for prop in props))

        if score > best:
            best = score

        if score > best_cals and dotproduct(sizes, cals) == 500:
            best_cals = score

    return best, best_cals


best, best_cals = max_score(read_input())
print(best)
print(best_cals)
