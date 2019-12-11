from more_itertools import map_reduce
from more_itertools import powerset

from advent.load import read_input

containers = [int(x) for x in read_input()]
groups = map_reduce((s for s in powerset(containers) if sum(s) == 150), len)
print(sum(len(v) for v in groups.values()))
print(len(groups[min(groups)]))
