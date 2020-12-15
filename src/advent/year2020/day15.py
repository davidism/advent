from collections import defaultdict
from collections import deque
from itertools import count

data = 7, 14, 0, 17, 11, 1, 2
heard = defaultdict(
    lambda: deque(maxlen=2),
    ((x, deque([i], 2)) for i, x in enumerate(data, 1)),
)
spoke = data[-1]

for i in count(len(data) + 1):
    if len(heard[spoke]) == 1:
        spoke = 0
    else:
        spoke = heard[spoke][1] - heard[spoke][0]

    heard[spoke].append(i)

    if i == 2020:
        print(spoke)
    elif i == 30_000_000:
        print(spoke)
        break
