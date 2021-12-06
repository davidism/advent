from collections import Counter
from collections import defaultdict

from advent.load import read_input


class School:
    def __init__(self, ages: list[int]) -> None:
        self.ages = defaultdict(int, Counter(ages))
        self.day = 0

    def step(self, n: int = 1) -> int:
        for _ in range(n):
            current = self.ages[self.day]
            self.ages[self.day + 7] += current
            self.ages[self.day + 9] += current
            self.day += 1

        return self.total()

    def total(self) -> int:
        return sum(v for k, v in self.ages.items() if k >= self.day)


data = [int(x) for x in read_input().split(",")]
school = School(data)
print(school.step(80))
print(school.step(256 - 80))
