from dataclasses import dataclass
from math import lcm

from advent.load import read_input


@dataclass
class Bus:
    id: int
    offset: int

    def at(self, ts):
        return ts % self.id

    def wait(self, ts):
        return self.id - self.at(ts)

    def part1(self, ts):
        return self.id * self.wait(ts)

    def is_departing(self, ts, offset):
        return self.at(ts - (offset - self.offset)) == 0


test1 = "17,x,13,19"
test2 = "67,7,59,61"
test3 = "67,x,7,59,61"
test4 = "67,7,x,59,61"
test5 = "1789,37,47,1889"
lines = read_input()
arrival = int(lines[0])
intervals = lines[1]
buses = [Bus(int(x), i) for i, x in enumerate(intervals.split(",")) if x.isdigit()]
# print(min(buses, key=lambda x: x.wait(arrival)).part1(arrival))

t = lcm(*(b.id for b in buses))
interval_bus = max(buses, key=lambda b: b.id)
n_buses = len(buses)

while t > 0:
    check = [(b, b.is_departing(t, interval_bus.offset)) for b in buses]

    if all(x[1] for x in check):
        print(t - (interval_bus.offset - buses[0].offset))
        break

    t -= lcm(*(x[0].id for x in check if x[1]))
