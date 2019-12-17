import time

from advent.draw import draw_points
from advent.draw import prepare_screen
from advent.grid import move
from advent.grid import neighbors
from advent.grid import turns
from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode

chr_to_dir = {">": 0, "^": 1, "<": 2, "v": 3, "X": None}
dir_to_chr = {v: k for k, v in chr_to_dir.items()}


class Robot:
    def __init__(self, data):
        self.interpreter = Interpreter(data, output=self)
        self.map = {}
        self.cx = self.cy = 0
        self.point = None
        self.dir = None
        self.dust = 0
        self.display = None

    def append(self, value):
        if value > 127:
            self.dust = value
            return

        value = chr(value)

        if value == "\n":
            self.cx = 0
            self.cy += 1
        else:
            point = self.cx, self.cy
            self.cx += 1

            if value in {">", "^", "<", "v", "X"}:
                self.point = point
                self.dir = chr_to_dir[value]
                self.map[point] = "#" if value != "X" else "."
            else:
                self.map[point] = value

        if self.display is not None:
            self.draw()
            time.sleep(0.1)

    def run(self, camera=None, display=False):
        if camera:
            self.interpreter[0] = 2

        with prepare_screen(display) as self.display:
            self.interpreter.run()

    def intersections(self):
        for point, value in self.map.items():
            if value != "#":
                continue

            if sum(self.map.get(n) == "#" for n in neighbors(point, False)) > 2:
                yield point

    def end_point(self):
        for point, value in self.map.items():
            if value != "#" or point == self.point:
                continue

            if sum(self.map.get(n) == "#" for n in neighbors(point)) == 1:
                return point

    def alignment(self):
        return sum(x * y for x, y in self.intersections())

    def unwind(self):
        end = self.end_point()
        point = self.point
        dir = self.dir
        steps = 0
        out = []

        while point != end:
            ahead = move(point, dir)

            if self.map.get(ahead) == "#":
                steps += 1
                point = ahead
            else:
                if steps:
                    out.append(steps)
                    steps = 0

                for i, n in enumerate(neighbors(point, False)):
                    if self.map.get(n) != "#":
                        continue

                    ts = turns(dir, i)

                    if len(ts) != 1:
                        continue

                    # TODO turns are wrong
                    out.append("R" if ts[0] == 1 else "L")
                    dir = i
                    break

        out.append(steps)
        return out

    def draw(self):
        intersections = set(self.intersections())

        def transform(point):
            if point == self.point:
                return dir_to_chr[self.dir]
            elif point in intersections:
                return "O"

            return self.map[point]

        draw_points(self.map, transform, width=1, term=self.display)


camera = Robot(read_intcode())
camera.run()
camera.draw()
print(camera.alignment())
print(camera.unwind())
# robot = Robot(read_intcode())
# robot.run(camera=camera)
# print(robot.dust)
