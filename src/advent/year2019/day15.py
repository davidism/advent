import time
from contextlib import ExitStack

import networkx as nx
from blessings import Terminal

from advent.draw import draw_points
from advent.grid import neighbors
from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode


def _move(point, dir):
    x, y = point

    if dir == 4:
        return x + 1, y
    elif dir == 1:
        return x, y + 1
    elif dir == 3:
        return x - 1, y
    else:
        return x, y - 1


def _adjacent_dir(cp, gp):
    cx, cy = cp
    gx, gy = gp

    if cx == gx:
        if cy + 1 == gy:
            return 1

        if cy - 1 == gy:
            return 2

    if cy == gy:
        if cx == gx - 1:
            return 4

        if cx == gx + 1:
            return 3


class Robot:
    def __init__(self, data):
        self.interpreter = Interpreter(data, input=self, output=self)
        self.point = 0, 0
        self.dir = 4
        self.to_explore = []
        self.path = []
        self.backtracking = False
        self.map = {}
        self.display = None

    def popleft(self):
        if self.dir is None:
            raise IndexError

        return self.dir

    def append(self, status):
        point = _move(self.point, self.dir)
        self.map[point] = {0: "#", 1: " ", 2: "O"}[status]

        if status:
            if not self.backtracking:
                self.path.append(self.point)
            else:
                self.backtracking = False

            self.point = point

        self.to_explore.extend(
            p for p in neighbors(self.point, False) if p not in self.map
        )

        while self.to_explore and self.to_explore[-1] in self.map:
            self.to_explore.pop()

        if self.to_explore:
            point = self.to_explore.pop()
            dir = _adjacent_dir(self.point, point)
        else:
            point = dir = None

        if dir is None and self.path:
            if point is not None:
                self.to_explore.append(point)

            self.backtracking = True
            point = self.path.pop()
            dir = _adjacent_dir(self.point, point)

        self.dir = dir

        if self.display is not None:
            self.draw()
            time.sleep(0.01)

    def run(self, display=False):
        with ExitStack() as exit_stack:
            if display:
                self.display = Terminal()
                exit_stack.enter_context(self.display.fullscreen())
                exit_stack.enter_context(self.display.hidden_cursor())

            self.interpreter.run()

        if display:
            self.draw()

    def oxygen(self):
        g = nx.Graph()
        g.add_nodes_from(self.map)
        g.add_edges_from(
            (p1, p2)
            for p1, f1 in self.map.items()
            if f1 != "#"
            for p2 in neighbors(p1, False)
            if p2 in self.map and self.map[p2] != "#"
        )
        o = next(p for p, f in self.map.items() if f == "O")
        return (
            nx.shortest_path_length(g, (0, 0), o),
            max(nx.shortest_path_length(g, o).values()),
        )

    def draw(self):
        def transform(point):
            flag = self.map.get(point, "?")

            if flag == "O":
                return "O"
            elif point == self.point:
                return "D"
            elif point == (0, 0):
                return "S"

            return flag

        draw_points(self.map, transform, flip_y=True, term=self.display)


robot = Robot(read_intcode())
robot.run()
print(*robot.oxygen(), sep="\n")
