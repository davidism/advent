from statistics import median_low

from advent.load import read_input

lines = read_input()
corrupt_score = 0
incomplete_scores = []
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

for line in lines:
    stack = []
    corrupt = False

    for c in line:
        if c in pairs:
            stack.append(c)
        else:
            match = stack.pop()

            if pairs[match] != c:
                corrupt_score += {")": 3, "]": 57, "}": 1197, ">": 25137}[c]
                corrupt = True
                break

    if corrupt or not stack:
        continue

    incomplete = 0

    for c in reversed(stack):
        incomplete *= 5
        incomplete += {"(": 1, "[": 2, "{": 3, "<": 4}[c]

    incomplete_scores.append(incomplete)

print(corrupt_score, median_low(incomplete_scores))
