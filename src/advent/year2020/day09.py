from collections import deque
from itertools import combinations

from advent.load import read_input


def sum_window(numbers):
    return set(x + y for x, y in combinations(numbers, 2) if x != y)


numbers = [int(x) for x in read_input()]
window = deque(numbers[:25], 25)
sums = sum_window(window)
invalid = 0

for number in numbers[25:]:
    if number not in sums:
        invalid = number
        break

    window.append(number)
    sums = sum_window(window)

print(invalid)

for i in range(len(numbers)):
    acc = deque()

    for number in numbers[i:]:
        acc.append(number)
        s = sum(acc)

        if s > invalid:
            acc.clear()

        if s >= invalid:
            break

    if acc:
        print(min(acc) + max(acc))
        break
