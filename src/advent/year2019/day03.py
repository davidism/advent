from advent.load import read_input


def follow_path(data):
    path = [(p[0], int(p[1:])) for p in data.strip().split(",")]
    x = y = 0
    steps = 0
    out = {}

    for bearing, distance in path:
        for _ in range(distance):
            steps += 1

            if bearing == "R":
                x += 1
            elif bearing == "L":
                x -= 1
            elif bearing == "U":
                y += 1
            else:
                y -= 1

            out[x, y] = steps

    return out


def manhattan(point):
    return abs(point[0]) + abs(point[1])


data = read_input()
p1 = follow_path(data[0])
p2 = follow_path(data[1])
common_points = p1.keys() & p2.keys()
print(manhattan(min(common_points, key=manhattan)))
shortest = min(common_points, key=lambda x: p1[x] + p2[x])
print(p1[shortest] + p2[shortest])
