from itertools import chain
from itertools import product

from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode


def scan(data, x=0, y=0, w=50, h=50, perimeter=False):
    out = set()

    if perimeter:
        points = chain(
            product((x, x + w - 1), range(y, y + h)),
            product(range(x + 1, x + w - 1), (y, y + h - 1)),
        )
    else:
        points = product(range(x, x + w), range(y, y + h))

    for point in points:
        c = Interpreter(data, input=point)
        c.run()

        if c.output[0]:
            out.add(point)

    return out


def fit(data, w=100, h=100):
    perimeter = 2 * w + 2 * h - 4
    x = y = 0
    beam = scan(data, x, y, w, h, True)

    while len(beam) != perimeter:
        mx = max(p[0] for p in beam)
        my = max(p[1] for p in beam)
        x = min(p[0] for p in beam if p[1] == my)
        y = min(p[1] for p in beam if p[0] == mx)
        beam = scan(data, x, y, w, h, True)

    return x, y


print(len(scan(read_intcode())))
cx, cy = fit(read_intcode())
print(cx * 10000 + cy)
