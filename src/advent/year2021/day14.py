from collections import Counter
from itertools import pairwise

from advent.load import read_input


class Polymer:
    def __init__(self, template: str, inserts: dict[str, str]) -> None:
        self.template = Counter(pairwise(template))
        self.elements = Counter(template)
        self.inserts = {(a, b): ((a, v), (v, b), v) for (a, b), v in inserts.items()}

    @classmethod
    def from_lines(cls, lines: list[str]) -> "Polymer":
        template = lines[0]
        inserts = {a: b for a, _, b in (n.partition(" -> ") for n in lines[1:])}
        return cls(template, inserts)

    def step(self) -> None:
        for pair, count in self.template.copy().items():
            a, b, e = self.inserts[pair]
            self.template[pair] -= count
            self.template[a] += count
            self.template[b] += count
            self.elements[e] += count

    def step_n(self, n: int) -> None:
        for _ in range(n):
            self.step()

    def score(self) -> int:
        order = self.elements.most_common()
        return order[0][1] - order[-1][1]


polymer = Polymer.from_lines(read_input())
polymer.step_n(10)
print(polymer.score())
polymer.step_n(30)
print(polymer.score())
