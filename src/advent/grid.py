from more_itertools import unzip


def manhattan(a, b=(0, 0)):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


def bounds(points, screen=False):
    xs, ys = map(set, unzip(points))
    xr = range(min(xs), max(xs) + 1)

    if screen:
        yr = range(max(ys), min(ys) - 1, -1)
    else:
        yr = range(min(ys), max(ys) + 1)

    return xr, yr


def neighbors(point, diag=True):
    x, y = point

    if diag:
        yield from (
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
        )
    else:
        yield from (
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1),
        )


def move(point, dir):
    x, y = point

    if dir == 0:
        return x + 1, y
    elif dir == 1:
        return x, y + 1
    elif dir == 2:
        return x - 1, y
    else:
        return x, y - 1


def adjacent(a, b):
    ax, ay = a
    bx, by = b

    if ay == by:
        if ax < bx:
            return 0
        elif ax > bx:
            return 2
    elif ax == bx:
        if ay < by:
            return 1
        elif ay > by:
            return 3


def turns(c, n):
    d = n - c
    m = abs(d)

    if d == 0:
        return []
    elif m == 1:
        return [d]
    elif m == 2:
        return [1, 1]
    else:
        return [-1 if d > 0 else 1]
