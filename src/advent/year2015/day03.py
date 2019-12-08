from advent.load import read_input


def visit(directions):
    x = y = 0
    visited = {(0, 0)}

    for direction in directions:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        else:
            y -= 1

        visited.add((x, y))

    return visited


data = read_input()
print(len(visit(data)))
print(len(visit(data[::2]) | visit(data[1::2])))
