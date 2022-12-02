from advent.load import read_input


def move_score(move: str) -> int:
    return {"A": 1, "B": 2, "C": 3}[move]


def outcome_score(opponent: str, player: str) -> int:
    if player == opponent:
        return 3
    elif (
        (player == "A" and opponent == "B")
        or (player == "B" and opponent == "C")
        or (player == "C" and opponent == "A")
    ):
        return 0
    else:
        return 6


def score_part1(strategy: list[list[str, str]]) -> int:
    move = {"X": "A", "Y": "B", "Z": "C"}
    return sum(
        move_score(p) + outcome_score(o, p)
        for o, p in ((o, move[p]) for o, p in strategy)
    )


def score_part2(strategy: list[list[str, str]]) -> int:
    translate = {
        ("A", "X"): "C",
        ("A", "Y"): "A",
        ("A", "Z"): "B",
        ("B", "X"): "A",
        ("B", "Y"): "B",
        ("B", "Z"): "C",
        ("C", "X"): "B",
        ("C", "Y"): "C",
        ("C", "Z"): "A",
    }
    return sum(
        move_score(p) + outcome_score(o, p)
        for o, p in ((o, translate[o, p]) for o, p in strategy)
    )


strategy = [line.split() for line in read_input()]
print(score_part1(strategy))
print(score_part2(strategy))
