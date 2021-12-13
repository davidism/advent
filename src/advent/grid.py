from functools import lru_cache
from itertools import product

from more_itertools import unzip

TPoint2 = tuple[int, int]
TGrid2 = dict[TPoint2, int]


def manhattan(p1, p2=None):
    if p2 is None:
        return sum(abs(n) for n in p1)

    return sum(abs(n2 - n1) for n1, n2 in zip(p1, p2))


def bounds(points, screen=False):
    xs, ys = map(set, unzip(points))
    xr = range(min(xs), max(xs) + 1)

    if screen:
        yr = range(max(ys), min(ys) - 1, -1)
    else:
        yr = range(min(ys), max(ys) + 1)

    return xr, yr


@lru_cache()
def neighbor_deltas(d=2):
    out = []

    for np in product(range(-1, 2), repeat=d):
        if all(n == 0 for n in np):
            continue

        out.append(np)

    return tuple(out)


@lru_cache()
def neighbors(point):
    d = len(point)
    out = []

    for ds in neighbor_deltas(d):
        out.append(tuple(n + nx for n, nx in zip(point, ds)))

    return tuple(out)


@lru_cache()
def cardinal_neighbors(point):
    x, y = point
    return (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)
