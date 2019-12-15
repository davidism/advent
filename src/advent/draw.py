from advent.grid import bounds


def draw_points(points, transform=None, flip_y=False, width=2, term=None):
    xr, yr = bounds(points, screen=flip_y)
    out = []

    if term is not None:
        out.append(term.clear)

    if not transform:
        if isinstance(points, dict):

            def transform(point):
                return " #"[bool(points.get(point))]

        else:

            def transform(point):
                return " #"[point in points]

    for y in yr:
        for x in xr:
            out.append(transform((x, y)) * width)

        out.append("\n")

    out.pop()
    print("".join(out))
