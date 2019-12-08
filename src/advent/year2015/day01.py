from advent.load import read_input

data = read_input()
total = 0
basement = None

for i, c in enumerate(data, 1):
    total += 1 if c == "(" else -1

    if total < 0 and basement is None:
        basement = i

print(total)
print(basement)
