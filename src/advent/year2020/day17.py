from itertools import product

from advent.grid import neighbors
from advent.load import read_input

grid2 = {
    (x, y): c == "#" for y, line in enumerate(read_input()) for x, c in enumerate(line)
}
grid3 = {(x, y, 0): a for (x, y), a in grid2.items()}
grid4 = {(x, y, 0, 0): a for (x, y), a in grid2.items()}
min_a = min_b = max_b = 0
max_a = max(p[0] for p in grid2)


def update_point(grid, out, point):
    p_active = grid.get(point, False)
    n_active = sum(1 for np in neighbors(point) if grid.get(np, False))

    if p_active:
        if n_active not in {2, 3}:
            out[point] = False
    else:
        if n_active == 3:
            out[point] = True


for _ in range(6):
    min_a -= 1
    max_a += 1
    min_b -= 1
    max_b += 1
    ra = range(min_a, max_a + 1)
    rb = range(min_b, max_b + 1)
    out3 = grid3.copy()
    out4 = grid4.copy()

    for point in product(ra, ra, rb):
        update_point(grid3, out3, point)

    for point in product(ra, ra, rb, rb):
        update_point(grid4, out4, point)

    grid3 = out3
    grid4 = out4

print(sum(grid3.values()))
print(sum(grid4.values()))
