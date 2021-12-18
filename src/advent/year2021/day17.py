import dataclasses
from itertools import accumulate
from itertools import count
from itertools import takewhile
from typing import Optional

from advent.load import read_input
from advent.math import triangular


def parse_target(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    xrs, _, yrs = line.partition(", ")
    x1s, _, x2s = xrs.partition("=")[2].partition("..")
    y1s, _, y2s = yrs.partition("=")[2].partition("..")
    return (int(x1s), int(x2s)), (int(y1s), int(y2s))


@dataclasses.dataclass
class V:
    initial: int
    start: int
    end: Optional[int]

    def max_y(self) -> int:
        return triangular(self.initial)


def find_vxs(tx1: int, tx2: int) -> list[V]:
    tr = range(tx1, tx2 + 1)
    out = []

    for v in range(tx2 + 1):
        xs = list(accumulate(range(v, 0, -1)))
        hits = [s for s, x in enumerate(xs, 1) if x in tr]

        if not hits:
            continue

        out.append(V(v, hits[0], hits[-1] if xs[-1] > tx2 else None))

    return out


def find_vys(ty1: int, ty2: int, vx: V) -> list[V]:
    end = vx.end if vx.end is not None else 1_000_000_000
    ir = range(vx.start, end + 1)
    tr = range(ty1, ty2 + 1)
    out = []

    for v in range(ty1, 2 * abs(ty1) + 1):
        hits = [
            i
            for i, y in takewhile(
                lambda iy: iy[1] >= ty1, enumerate(accumulate(count(v, -1)), 1)
            )
            if i in ir and y in tr
        ]

        if not hits:
            continue

        out.append(V(v, hits[0], hits[-1]))

    return out


def main():
    (tx1, tx2), (ty1, ty2) = parse_target(read_input())
    vs = [(vx, vy) for vx in find_vxs(tx1, tx2) for vy in find_vys(ty1, ty2, vx)]
    vx, vy = max(vs, key=lambda vxy: vxy[1].initial)
    print(vy.max_y())
    print(len(vs))


if __name__ == "__main__":
    main()
