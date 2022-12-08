from advent.load import read_input

map = {(x, y): int(c) for y, row in enumerate(read_input()) for x, c in enumerate(row)}
width = max(x for x, _ in map) + 1
height = max(y for _, y in map) + 1
total_visible = 0
scenic_map = {}

for (x, y), v in map.items():
    visible = False

    if x == 0 or y == 0 or x + 1 == width or y + 1 == height:
        scenic = 0
    else:
        scenic = 1

    for x2 in range(x - 1, -1, -1):
        if map[x2, y] >= v:
            scenic *= x - x2
            break
    else:
        visible = True
        scenic *= x

    for x2 in range(x + 1, width):
        if map[x2, y] >= v:
            scenic *= x2 - x
            break
    else:
        visible = True
        scenic *= width - x - 1

    for y2 in range(y - 1, -1, -1):
        if map[x, y2] >= v:
            scenic *= y - y2
            break
    else:
        visible = True
        scenic *= y

    for y2 in range(y + 1, width):
        if map[x, y2] >= v:
            scenic *= y2 - y
            break
    else:
        visible = True
        scenic *= height - y - 1

    total_visible += visible
    scenic_map[x, y] = scenic

print(total_visible)
print(max(scenic_map.values()))
