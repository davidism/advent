from collections import Counter

from advent.load import read_input


class Group:
    def __init__(self, data):
        self.counter = Counter()
        self.number = 0

        for line in data:
            self.counter.update(line)
            self.number += 1

    def anyone(self):
        return len(self.counter)

    def everyone(self):
        return sum(1 for v in self.counter.values() if v == self.number)


groups = [Group(g) for g in read_input(group=True)]
print(sum(g.anyone() for g in groups))
print(sum(g.everyone() for g in groups))
