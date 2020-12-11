from collections import Counter

from more_itertools import pairwise

from advent.load import read_input

ratings = set(int(x) for x in read_input())
ratings.add(0)
adapter = max(ratings) + 3
ratings.add(adapter)
c = Counter(y - x for x, y in pairwise(sorted(ratings)))
print(c[1] * c[3])
