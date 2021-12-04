from advent.load import read_input


def make_win_conditions() -> list[tuple[int, ...]]:
    positions = range(25)
    out = []

    for i in range(5):
        out.append(tuple(positions[i * 5 : (i * 5) + 5]))
        out.append(tuple(positions[i::5]))

    return out


win_conditions = make_win_conditions()


class Board:
    def __init__(self, numbers: list[int]) -> None:
        self.n_to_p: dict[int, int] = {n: i for i, n in enumerate(numbers)}
        self.p_to_n: dict[int, int] = {i: n for i, n in enumerate(numbers)}

    @classmethod
    def from_group(cls, group: list[str]) -> "Board":
        return cls([int(x) for x in " ".join(group).split()])

    @classmethod
    def from_groups(cls, groups: list[list[str]]) -> list["Board"]:
        return [cls.from_group(group) for group in groups]

    def play(self, order: list[int]) -> tuple[int, int]:
        marks: dict[int, int] = {i: False for i in range(25)}

        for i, n in enumerate(order):
            if n in self.n_to_p:
                marks[self.n_to_p[n]] = True

            if any(all(marks[p] for p in c) for c in win_conditions):
                score = sum(self.p_to_n[p] for p in range(25) if not marks[p])
                return i, score * n

        return len(order), 0


data = read_input(group=True)
order = [int(x) for x in data[0][0].split(",")]
boards = Board.from_groups(data[1:])
results = [b.play(order) for b in boards]
print(min(results), max(results))
