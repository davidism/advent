from contextlib import contextmanager
from contextlib import ExitStack

from blessings import Terminal

from advent.grid import bounds


@contextmanager
def prepare_screen(draw=True):
    if not draw:
        yield None
    else:
        term = Terminal()

        with ExitStack() as exit_stack:
            exit_stack.enter_context(term.fullscreen())
            exit_stack.enter_context(term.hidden_cursor())
            yield term


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
