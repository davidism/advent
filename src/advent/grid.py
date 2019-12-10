def manhattan(a, b=(0, 0)):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)
