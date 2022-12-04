import re

from advent.load import read_input

fully_contained = 0
overlaps = 0

for line in read_input():
    ax, ay, bx, by = map(int, re.split("[,-]", line))
    ar = set(range(ax, ay + 1))
    br = set(range(bx, by + 1))

    if ar <= br or br <= ar:
        fully_contained += 1
        overlaps += 1
    elif ar & br:
        overlaps += 1

print(fully_contained)
print(overlaps)
