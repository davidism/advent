from attr import dataclass

from advent.load import read_input


@dataclass(slots=True, frozen=True)
class Reindeer:
    name: str
    speed: int
    fly: int
    rest: int

    @classmethod
    def from_line(cls, line):
        line = line.split()
        return cls(
            name=line[0], speed=int(line[3]), fly=int(line[6]), rest=int(line[13]),
        )

    def distance(self, t):
        chunks, remain = divmod(t, self.fly + self.rest)
        extra = min(self.fly, remain)
        return chunks * self.speed * self.fly + extra * self.speed


def new_scoring(rs, t):
    out = {r: 0 for r in rs}

    for i in range(1, t + 1):
        out[max(rs, key=lambda r: r.distance(i))] += 1

    return out


data = [Reindeer.from_line(line) for line in read_input()]
print(max(r.distance(2503) for r in data))
print(max(new_scoring(data, 2503).values()))
