from advent.draw import draw_points
from advent.grid import TPoint2
from advent.load import read_input


class Paper:
    def __init__(self, points: set[TPoint2], folds: list[tuple[bool, int]]) -> None:
        self.points = points
        self.folds = folds

    @classmethod
    def from_lines(cls, pls: list[str], fls: list[str]) -> "Paper":
        return cls(
            {(int(x), int(y)) for x, _, y in (n.partition(",") for n in pls)},
            [(a[-1] == "y", int(b)) for a, _, b in (n.partition("=") for n in fls)],
        )

    def fold_one(self) -> None:
        over_y, axis_str = self.folds.pop(0)
        axis = int(axis_str)
        flip_const = 2 * axis
        out = self.points.copy()

        for p in self.points:
            current = p[1] if over_y else p[0]

            if current > axis:
                out.remove(p)
                new = flip_const - current
                out.add((p[0], new) if over_y else (new, p[1]))

        self.points = out

    def fold_all(self) -> None:
        while self.folds:
            self.fold_one()

    def draw(self) -> None:
        draw_points(self.points)


paper = Paper.from_lines(*read_input(group=True))
paper.fold_one()
print(len(paper.points))
paper.fold_all()
paper.draw()
