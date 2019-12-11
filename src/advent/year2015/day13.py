from itertools import chain
from itertools import permutations

import networkx as nx
from more_itertools import windowed

from advent.load import read_input


def parse_rules(lines):
    g = nx.DiGraph()

    for line in lines:
        line = line[:-1].split()
        score = (-1 if line[2] == "lose" else 1) * int(line[3])
        g.add_edge(line[0], line[-1], h=score)

    return g


def add_apathy(g):
    out = g.copy()

    for node in g.nodes:
        out.add_edge("self", node, h=0)
        out.add_edge(node, "self", h=0)

    return out


def max_happy(g):
    max_change = 0

    for order in permutations(g.nodes):
        total = 0

        for left, person, right in windowed(chain([order[-1]], order, [order[0]]), 3):
            total += g[person][left]["h"] + g[person][right]["h"]

        if total > max_change:
            max_change = total

    return max_change


data = parse_rules(read_input())
print(max_happy(data))
print(max_happy(add_apathy(data)))
