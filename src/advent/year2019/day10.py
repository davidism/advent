from collections import defaultdict
from functools import partial
from math import atan2
from math import gcd
from math import pi
from math import tau

from more_itertools import interleave_longest

from advent.grid import manhattan
from advent.load import read_input


def parse_points(lines):
    return [
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"
    ]


def sight(points, point):
    slopes = defaultdict(list)

    for other in sorted(points, key=partial(manhattan, point)):
        if other == point:
            continue

        dx = other[0] - point[0]
        dy = other[1] - point[1]
        scale = gcd(dx, dy)
        slopes[dx // scale, dy // scale].append(other)

    return slopes


def sweep_angle(point):
    return (atan2(point[1], point[0]) + tau + pi / 2) % tau


def laser_order(slopes):
    sweep = [slopes[slope] for slope in sorted(slopes, key=sweep_angle)]
    return list(interleave_longest(*sweep))


data = parse_points(read_input())
sights = {point: sight(data, point) for point in data}
location = max(sights, key=lambda x: len(sights[x]))
sight = sights[location]
print(len(sight))
hit = laser_order(sight)[199]
print(hit[0] * 100 + hit[1])
