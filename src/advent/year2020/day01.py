from itertools import combinations

from advent.load import read_input

lines = [int(x) for x in read_input()]

for x, y in combinations(lines, 2):
    if x + y == 2020:
        print(x * y)
        break

for x, y, z in combinations(lines, 3):
    if x + y + z == 2020:
        print(x * y * z)
        break
