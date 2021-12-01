from attr import dataclass

from advent.load import read_input


@dataclass(slots=True, frozen=True)
class Present:
    l: int
    w: int
    h: int

    @classmethod
    def from_line(cls, line: str) -> "Present":
        return cls(*(int(i) for i in line.split("x")))

    @property
    def paper(self):
        areas = (self.l * self.w, self.w * self.h, self.h * self.l)
        return 2 * sum(areas) + min(areas)

    @property
    def ribbon(self):
        l, w = sorted((self.l, self.w, self.h))[:2]
        return 2 * (l + w) + self.l * self.w * self.h


data = [Present.from_line(x) for x in read_input()]
print(sum(p.paper for p in data))
print(sum(p.ribbon for p in data))
