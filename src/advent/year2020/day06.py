from collections import Counter
from pathlib import Path


class Group:
    def __init__(self, data):
        self.counter = Counter()
        self.number = 0

        for line in data.splitlines():
            self.counter.update(line)
            self.number += 1

    def anyone(self):
        return len(self.counter)

    def everyone(self):
        return sum(1 for v in self.counter.values() if v == self.number)


groups = [
    Group(g) for g in (Path(__file__).parent / "day06.txt").read_text().split("\n\n")
]

print(sum(g.anyone() for g in groups))
print(sum(g.everyone() for g in groups))
