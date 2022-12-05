import re
from copy import deepcopy

from advent.load import read_input

(*stack_lines, stack_numbers), step_lines = read_input(group=True)
stacks = [[] for _ in range(int(stack_numbers.rpartition(" ")[2]))]

for line in reversed(stack_lines):
    for stack, item in zip(stacks, re.findall(r"\[([A-Z])]| {2,5}", line)):
        if item:
            stack.append(item)

stacks2 = deepcopy(stacks)

for line in step_lines:
    n, s, d = map(int, re.match(r"move (\d+) from (\d) to (\d)", line).groups())
    s -= 1
    d -= 1

    moved, stacks[s] = stacks[s][-n:], stacks[s][:-n]
    stacks[d].extend(reversed(moved))

    moved, stacks2[s] = stacks2[s][-n:], stacks2[s][:-n]
    stacks2[d].extend(moved)

print("".join(s[-1] for s in stacks))
print("".join(s[-1] for s in stacks2))
