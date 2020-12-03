import math

from advent.load import read_input

grid = [[c == "#" for c in line] for line in read_input()]
height = len(grid)
width = len(grid[0])


class Toboggan:
    def __init__(self, dy, dx):
        self.dy = dy
        self.dx = dx
        self.y = 0
        self.x = 0
        self.count = 0

    def move(self):
        if self.y >= height:
            return False

        self.count += grid[self.y][self.x]
        self.y += self.dy
        self.x = (self.x + self.dx) % width
        return True


ts = [
    Toboggan(1, 1),
    Toboggan(1, 3),
    Toboggan(1, 5),
    Toboggan(1, 7),
    Toboggan(2, 1),
]

while any(t.move() for t in ts):
    pass

print(math.prod(t.count for t in ts))
