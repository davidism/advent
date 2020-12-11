from advent.grid import neighbor_deltas
from advent.grid import neighbors
from advent.load import read_input


def visible_neighbors(grid, point):
    x, y = point

    for dx, dy in neighbor_deltas():
        nx, ny = x, y

        while True:
            nx, ny = nx + dx, ny + dy
            np = nx, ny

            if np not in grid:
                break

            if grid[np] != floor:
                yield np
                break


floor = "."
empty = "L"
occupied = "#"
grid = {}
check_direct = {}
check_visible = {}

for y, line in enumerate(read_input()):
    for x, c in enumerate(line):
        grid[x, y] = c

for point in grid:
    check_direct[point] = [np for np in neighbors(point) if np in grid]
    check_visible[point] = list(visible_neighbors(grid, point))


def step(grid, check, tolerance):
    out = grid.copy()

    for point in grid:
        if grid[point] == empty:
            if all(grid[np] in {floor, empty} for np in check[point] if np in grid):
                out[point] = occupied
        elif grid[point] == occupied:
            if (
                sum(grid[np] == occupied for np in check[point] if np in grid)
                >= tolerance
            ):
                out[point] = empty

    return out


def run(grid, check, tolerance):
    while True:
        new_grid = step(grid, check, tolerance)

        if new_grid == grid:
            return sum(v == occupied for v in new_grid.values())

        grid = new_grid


print(run(grid, check_direct, 4))
print(run(grid, check_visible, 5))
