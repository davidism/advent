from itertools import pairwise

from more_itertools import windowed

from advent.load import read_input

data = [int(x) for x in read_input()]
print(sum(y > x for x, y in pairwise(data)))
print(sum(y > x for x, y in pairwise(sum(items) for items in windowed(data, 3))))
