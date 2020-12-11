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


def neighbor_deltas(diag=True):
    if diag:
        yield from (
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        )
    else:
        yield from (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        )
