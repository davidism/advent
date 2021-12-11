from collections import deque

from advent.grid import neighbors
from advent.load import read_input

Point = tuple[int, int]
Grid = dict[Point, int]


class Octo:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.now = 0
        self.flashes = 0
        self.sync = 0

    @classmethod
    def from_lines(cls, lines: list[str]) -> "Octo":
        grid = {}

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                grid[(x, y)] = int(c)

        return cls(grid)

    def step(self) -> None:
        for p in self.grid:
            self.grid[p] += 1

        flashed = set()
        q = deque(p for p, v in self.grid.items() if v > 9)

        while q:
            p = q.popleft()

            if p in flashed:
                continue

            flashed.add(p)

            for n in neighbors(p):
                if n in self.grid:
                    self.grid[n] += 1

            q.extend(p for p, v in self.grid.items() if p not in flashed and v > 9)

        for p in flashed:
            self.grid[p] = 0

        self.now += 1
        flashes = len(flashed)
        self.flashes += flashes

        if flashes == len(self.grid) and self.sync == 0:
            self.sync = self.now

    def steps(self, n: int) -> int:
        for _ in range(n):
            self.step()

        return self.flashes

    def find_sync(self) -> int:
        while self.sync == 0:
            self.step()

        return self.sync


lines = read_input()
octo = Octo.from_lines(lines)
print(octo.steps(100))
print(octo.find_sync())
