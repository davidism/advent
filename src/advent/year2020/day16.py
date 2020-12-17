from collections import defaultdict
from math import prod

from advent.load import read_input

lines = iter(read_input())
field_ranges = {}
all_ranges = []

for line in lines:
    if line == "your ticket:":
        break

    key, _, desc = line.partition(": ")
    r1s, _, r2s = desc.partition(" or ")
    r1ls, _, r1rs = r1s.partition("-")
    r2ls, _, r2rs = r2s.partition("-")
    r1 = range(int(r1ls), int(r1rs) + 1)
    r2 = range(int(r2ls), int(r2rs) + 1)
    field_ranges[key] = (r1, r2)
    all_ranges.append(r1)
    all_ranges.append(r2)

ours = [int(x) for x in next(lines).split(",")]
next(lines)
other_tickets = [[int(x) for x in line.split(",")] for line in lines]
invalid_values = []
valid_tickets = []

for ticket in other_tickets:
    ivs = [v for v in ticket if not any(v in r for r in all_ranges)]
    invalid_values.extend(ivs)

    if not ivs:
        valid_tickets.append(ticket)

print(sum(invalid_values))

positions = defaultdict(set)

for i, group in enumerate(zip(*valid_tickets)):
    for name, (r1, r2) in field_ranges.items():
        if all(v in r1 or v in r2 for v in group):
            positions[name].add(i)

seen = set()
field_position = {}

for name, ps in sorted(positions.items(), key=lambda i: len(i[1])):
    p = next(iter(ps - seen))
    field_position[name] = p
    seen.add(p)

departure = [ours[i] for k, i in field_position.items() if "departure" in k]
print(prod(departure))
