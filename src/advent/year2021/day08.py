from itertools import groupby

from advent.load import read_input


def parse_line(line: str) -> tuple[list[frozenset[str]], list[frozenset[str]]]:
    x, _, y = line.partition(" | ")
    return (
        [frozenset(d) for d in x.split(" ")],
        [frozenset(d) for d in reversed(y.split(" "))],
    )


data = [parse_line(line) for line in read_input()]
part1 = 0
part2 = 0

for patterns, output in data:
    by_len = {k: list(vs) for k, vs in groupby(sorted(patterns, key=len), key=len)}
    known = {1: by_len[2][0], 4: by_len[4][0], 7: by_len[3][0], 8: by_len[7][0]}
    one = known[1]
    four_arm = known[4] - known[1]

    for item in by_len[5]:
        if one <= item:
            known[3] = item
        elif four_arm <= item:
            known[5] = item
        else:
            known[2] = item

    for item in by_len[6]:
        if not one <= item:
            known[6] = item
        elif four_arm <= item:
            known[9] = item
        else:
            known[0] = item

    to_digit = {v: k for k, v in known.items()}

    for i, v in enumerate(output):
        d = to_digit[v]
        part2 += 10 ** i * d

        if d in {1, 4, 7, 8}:
            part1 += 1

print(part1, part2)
