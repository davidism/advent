from advent.load import read_input

dir_delta = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1),
}
tail_delta = {
    (2, 0): (1, 0),
    (2, 1): (1, 1),
    (2, 2): (1, 1),
    (1, 2): (1, 1),
    (0, 2): (0, 1),
    (-1, 2): (-1, 1),
    (-2, 2): (-1, 1),
    (-2, 1): (-1, 1),
    (-2, 0): (-1, 0),
    (-2, -1): (-1, -1),
    (-2, -2): (-1, -1),
    (-1, -2): (-1, -1),
    (0, -2): (0, -1),
    (1, -2): (1, -1),
    (2, -2): (1, -1),
    (2, -1): (1, -1),
}


def next_tail_position(head, tail):
    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    dy = hy - ty

    if (dx, dy) not in tail_delta:
        return tail

    dtx, dty = tail_delta[dx, dy]
    return tx + dtx, ty + dty


def track_tail(count):
    head = (0, 0)
    knots = [(0, 0) for _ in range(count - 1)]
    tail_seen = set()

    for line in read_input():
        direction, _, distance = line.partition(" ")
        dx, dy = dir_delta[direction]

        for _ in range(int(distance)):
            current = head = head[0] + dx, head[1] + dy

            for i, knot in enumerate(knots):
                current = knots[i] = next_tail_position(current, knot)

            tail_seen.add(current)

    return len(tail_seen)


print(track_tail(2))
print(track_tail(10))
