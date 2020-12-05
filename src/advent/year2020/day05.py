from advent.load import read_input


def seat_to_int(line):
    line = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    return int(line, 2)


seats = sorted(seat_to_int(x) for x in read_input())

s_min = min(seats)
s_max = max(seats)

print(s_max)
missing = set(range(s_min, s_max + 1)) - set(seats)
print(next(iter(missing)))
