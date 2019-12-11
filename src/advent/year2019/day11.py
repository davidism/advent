from collections import defaultdict
from collections import deque

from advent.grid import bounds
from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode


class Robot:
    def __init__(self, data, start_white=False):
        self.interpreter = Interpreter(data, input=self, output=self)
        self.x = self.y = 0
        self.dir = deque([1, 2, 3, 0], 4)
        self.panels = defaultdict(int, [((0, 0), start_white)])
        self.do_move = False

    def popleft(self):
        return self.panels[self.x, self.y]

    def append(self, value):
        if not self.do_move:
            self.panels[self.x, self.y] = value
        else:
            self.dir.rotate(1 if value else -1)
            dir = self.dir[0]

            if dir == 0:
                self.x += 1
            elif dir == 1:
                self.y += 1
            elif dir == 2:
                self.x -= 1
            else:
                self.y -= 1

        self.do_move = not self.do_move

    def run(self):
        self.interpreter.run()

    def draw(self):
        xr, yr = bounds(self.panels, True)

        for y in yr:
            print("".join(["  ", "##"][self.panels[x, y]] for x in xr))


data = read_intcode()
robot = Robot(data)
robot.run()
print(len(robot.panels))

robot = Robot(data, start_white=True)
robot.run()
robot.draw()
