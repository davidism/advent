import re
from collections import defaultdict
from itertools import product

from attr import attrib
from attr import dataclass

from advent.load import read_input

parse_re = re.compile(r"(?:turn )?(on|off|toggle) (\d+),(\d+) through (\d+),(\d+)")


@dataclass(slots=True, frozen=True)
class Op:
    name: str
    x1: int = attrib(converter=int)
    y1: int = attrib(converter=int)
    x2: int = attrib(converter=int)
    y2: int = attrib(converter=int)

    @classmethod
    def from_line(cls, line):
        return cls(*parse_re.match(line).groups())

    def __iter__(self):
        return product(range(self.x1, self.x2 + 1), range(self.y1, self.y2 + 1))

    def apply(self, switch, bright):
        if self.name == "on":
            for pair in self:
                switch[pair] = True
                bright[pair] += 1
        elif self.name == "off":
            for pair in self:
                switch[pair] = False

                if bright[pair] > 0:
                    bright[pair] -= 1
        else:
            for pair in self:
                switch[pair] = not switch[pair]
                bright[pair] += 2


ops = [Op.from_line(line) for line in read_input()]
switch = defaultdict(bool)
bright = defaultdict(int)

for op in ops:
    op.apply(switch, bright)

print(sum(switch.values()))
print(sum(bright.values()))
