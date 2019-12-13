import time
from contextlib import ExitStack

from blessings import Terminal
from more_itertools import quantify

from advent.grid import bounds
from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode


class Game:
    def __init__(self, data):
        self.interpreter = Interpreter(data, input=self, output=self)
        self.pixels = {}
        self.buffer = []
        self.paddle = 0
        self.ball = 0
        self.score = 0
        self.display = None

    @property
    def bricks(self):
        return quantify(self.pixels.values(), lambda x: x == 2)

    def popleft(self):
        if self.display is not None:
            self.draw()
            time.sleep(0.01)

        if self.paddle == self.ball:
            return 0
        elif self.paddle < self.ball:
            return 1
        elif self.paddle > self.ball:
            return -1

    def append(self, value):
        self.buffer.append(value)

        if len(self.buffer) == 3:
            x, y, value = self.buffer
            self.buffer.clear()

            if x == -1 and y == 0:
                self.score = value
            else:
                self.pixels[x, y] = value

                if value == 3:
                    self.paddle = x
                elif value == 4:
                    self.ball = x

    def run(self):
        self.interpreter.run()

    def play(self, display=False):
        with ExitStack() as exit_stack:
            if display:
                self.display = Terminal()
                exit_stack.enter_context(self.display.fullscreen())
                exit_stack.enter_context(self.display.hidden_cursor())

            self.interpreter[0] = 2
            self.interpreter.run()

            while self.bricks:
                self.interpreter.run()

    def draw(self):
        if self.display is not None:
            print(self.display.clear)

        xr, yr = bounds(self.pixels)

        for y in yr:
            print("".join(" #0=o"[self.pixels[x, y]] for x in xr))

        print(self.score)


game = Game(read_intcode())
game.run()
print(game.bricks)

game = Game(read_intcode())
game.play()
print(game.score)
