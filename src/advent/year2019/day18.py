from itertools import product

import networkx as nx

from advent.grid import neighbors
from advent.load import read_input


class MapInfo:
    def __init__(self, lines):
        if isinstance(lines, str):
            lines = lines.splitlines(False)

        w = len(lines[0])
        h = len(lines)
        self.keys = keys = {}
        self.doors = doors = {}
        walls = set()

        for y, line in enumerate(lines, 1):
            y = h - y

            for x, c in enumerate(line):
                point = x, y

                if c == "@":
                    self.pos = point
                elif c == "#":
                    walls.add(point)
                elif c.islower():
                    keys[point] = c
                elif c.isupper():
                    doors[point] = c.lower()

        self.g = g = nx.Graph()

        for point in product(range(w), range(h)):
            if point in walls:
                g.add_node(point, type="wall")
            else:
                if point in keys:
                    g.add_node(point, type="key", id=keys[point])
                elif point in doors:
                    g.add_node(point, type="door", id=doors[point])
                else:
                    g.add_node(point)

                g.add_edges_from(
                    (point, n) for n in neighbors(point, False) if n not in walls
                )

    def available(self):
        out = {}

        for point, key in self.keys.items():
            try:
                out[key] = nx.shortest_path_length(self.g, self.pos, point)
            except nx.NetworkXNoPath:
                pass

        return out


info = MapInfo(read_input())
info = MapInfo(
    """#########
#b.A.@.a#
#########"""
)
print(info.available())
