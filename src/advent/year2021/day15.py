from itertools import pairwise

import networkx as nx

from advent.load import read_input

lines = read_input()
width = len(lines[0])
height = len(lines)
g: nx.DiGraph = nx.grid_2d_graph(width * 5, height * 5, create_using=nx.DiGraph)

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        risk = int(c)

        for ty in range(5):
            for tx in range(5):
                q, r = divmod(risk + tx + ty, 10)
                g.nodes[x + tx * width, y + ty * height]["risk"] = r + bool(q)

for node, risk in g.nodes(data="risk"):
    for _, _, data in g.in_edges(node, data=True):
        data["risk"] = risk

g_single = nx.subgraph_view(g, lambda n: n[0] < width and n[1] < height)
path = nx.shortest_path(g_single, (0, 0), (width - 1, height - 1), "risk")
print(sum(g[a][b]["risk"] for a, b in pairwise(path)))
path = nx.shortest_path(g, (0, 0), (width * 5 - 1, height * 5 - 1), "risk")
print(sum(g[a][b]["risk"] for a, b in pairwise(path)))
