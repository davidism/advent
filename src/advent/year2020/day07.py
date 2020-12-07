import dataclasses
import typing as t
from collections import deque

from advent.load import read_input


@dataclasses.dataclass()
class Bag:
    name: str
    contains: t.Dict[str, int]
    contained_by: t.Dict[str, int] = dataclasses.field(
        default_factory=dict, init=False, compare=False
    )

    @classmethod
    def parse_line(cls, line):
        name, _, contains_str = line.rstrip(".").partition(" bags contain ")
        contains = {}

        if contains_str != "no other bags":
            for item in contains_str.split(", "):
                item = item[:-5] if item[-1] == "s" else item[:-4]
                n_str, item_name = item.split(" ", 1)
                contains[item_name] = int(n_str)

        return cls(name, contains)

    def populate_reverse(self, bags):
        for name, count in self.contains.items():
            bag = bags[name]
            bag.contained_by[self.name] = count


bags = {bag.name: bag for bag in (Bag.parse_line(line) for line in read_input())}

for bag in bags.values():
    bag.populate_reverse(bags)

seen = set()
q = deque(bags["shiny gold"].contained_by)

while q:
    bag = bags[q.popleft()]
    seen.add(bag.name)
    q.extend(bag.contained_by)

print(len(seen))

count = 0
q = deque(["shiny gold"])

while q:
    bag = bags[q.popleft()]

    for name, n in bag.contains.items():
        count += n
        q.extend([name] * n)

print(count)
