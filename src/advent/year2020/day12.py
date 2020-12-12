from advent.grid import manhattan
from advent.load import read_input

lines = [(line[0], int(line[1:])) for line in read_input()]
x = y = dir = 0

for op, num in lines:
    if op == "N":
        y += num
    elif op == "S":
        y -= num
    elif op == "E":
        x += num
    elif op == "W":
        x -= num
    elif op == "F":
        if dir == 90:
            y += num
        elif dir == 270:
            y -= num
        elif dir == 0:
            x += num
        elif dir == 180:
            x -= num
    elif op == "L":
        dir = (dir + num) % 360
    elif op == "R":
        dir = (dir - num) % 360

print(manhattan((x, y)))

sx = sy = 0
wx = 10
wy = 1

for op, num in lines:
    if op == "N":
        wy += num
    elif op == "S":
        wy -= num
    elif op == "E":
        wx += num
    elif op == "W":
        wx -= num
    elif op == "F":
        sx += wx * num
        sy += wy * num
    elif op in "LR":
        if op == "R":
            num = {90: 270, 180: 180, 270: 90}[num]

        if num == 90:
            wx, wy = -wy, wx
        elif num == 180:
            wx, wy = -wx, -wy
        elif num == 270:
            wx, wy = wy, -wx

print(manhattan((sx, sy)))
