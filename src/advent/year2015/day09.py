from itertools import permutations

import networkx as nx
from more_itertools import pairwise

from advent.load import read_input


def build_graph(lines):
    out = nx.Graph()

    for line in lines:
        line = line.split()
        out.add_edge(line[0], line[2], d=int(line[4]))

    return out


g = build_graph(read_input())
ds = set(
    sum(g.edges[a, b]["d"] for a, b in pairwise(path)) for path in permutations(g.nodes)
)
print(min(ds))
print(max(ds))
