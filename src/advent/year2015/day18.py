from more_itertools import iterate
from more_itertools import nth
from more_itertools import quantify

from advent.grid import neighbors
from advent.load import read_input


def parse_grid(lines):
    return {
        (x, y): c == "#" for y, line in enumerate(lines) for x, c in enumerate(line)
    }


def step(lights, stuck=False):
    out = lights.copy()

    for point, state in lights.items():
        if stuck and point in stuck_points:
            continue

        sample = sum(lights.get(p, False) for p in neighbors(point))
        out[point] = sample in {2, 3} if state else sample == 3

    return out


def animate(lights, steps, stuck=False):
    if stuck:
        lights.update((k, True) for k in stuck_points)

    return quantify(nth(iterate(lambda x: step(x, stuck=stuck), data), steps).values())


stuck_points = {(0, 0), (99, 0), (0, 99), (99, 99)}

data = parse_grid(read_input())
print(animate(data, 100))
print(animate(data, 100, True))
