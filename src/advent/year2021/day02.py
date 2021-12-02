from advent.load import read_input

data = [(a, int(b)) for a, _, b in (x.partition(" ") for x in read_input())]

x = 0
aim = 0
y = 0

for d, n in data:
    if d == "forward":
        x += n
        y += aim * n
    elif d == "down":
        aim += n
    elif d == "up":
        aim -= n

print(x, aim, x * aim)
print(x, y, x * y)
