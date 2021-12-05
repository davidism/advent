import dataclasses
from collections import Counter
from functools import cache

from more_itertools import quantify

from advent.load import read_input


def dir_range(a1: int, a2: int) -> range:
    if a1 <= a2:
        return range(a1, a2 + 1)

    return range(a1, a2 - 1, -1)


@dataclasses.dataclass(frozen=True)
class Segment:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    @property
    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    @property
    def is_flat(self) -> bool:
        return self.is_horizontal or self.is_vertical

    @cache
    def covered(self) -> list[tuple[int, int]]:
        xr = dir_range(self.x1, self.x2)
        yr = dir_range(self.y1, self.y2)

        if self.is_horizontal:
            return [(x, self.y1) for x in xr]

        if self.is_vertical:
            return [(self.x1, y) for y in yr]

        return list(zip(xr, yr))

    @classmethod
    def from_str(cls, line: str) -> "Segment":
        a, _, b = line.partition(" -> ")
        x1, y1 = [int(v) for v in a.split(",", 1)]
        x2, y2 = [int(v) for v in b.split(",", 2)]
        return cls(x1, y1, x2, y2)


def main() -> None:
    data = read_input(back=2)
    segments = [Segment.from_str(line) for line in data]
    grid_flat = Counter()
    grid = Counter()

    for segment in segments:
        grid.update(segment.covered())

        if segment.is_flat:
            grid_flat.update(segment.covered())

    print(quantify(grid_flat.values(), lambda v: v > 1))
    print(quantify(grid.values(), lambda v: v > 1))


if __name__ == "__main__":
    main()
