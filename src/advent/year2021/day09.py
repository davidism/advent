import operator
from collections import deque
from functools import reduce

from advent.grid import cardinal_neighbors
from advent.load import read_input

Point = tuple[int, int]
Grid = dict[Point, int]


def make_grid(lines: str) -> Grid:
    out = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            out[(x, y)] = int(c)

    return out


def is_low_point(point: Point, grid: Grid) -> bool:
    height = grid[point]
    return all(height < grid[n] for n in cardinal_neighbors(point) if n in grid)


def find_basin(point: Point, grid: Grid) -> list[Point]:
    out = []
    q = deque([point])
    seen = set()

    while q:
        point = q.popleft()

        if point in seen:
            continue

        seen.add(point)
        out.append(point)
        height = grid[point]
        q.extend(
            n
            for n in cardinal_neighbors(point)
            if n in grid and grid[n] != 9 and grid[n] > height
        )

    return out


def main() -> None:
    data = read_input()
    grid = make_grid(data)
    low_points = [p for p in grid if is_low_point(p, grid)]
    print(sum(grid[p] + 1 for p in low_points))
    basins = [find_basin(p, grid) for p in low_points]
    basins.sort(key=len, reverse=True)
    print(reduce(operator.mul, map(len, basins[:3])))


if __name__ == "__main__":
    main()
