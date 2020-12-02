from advent.load import read_input

lines = read_input()
valid1 = []
valid2 = []

for line in lines:
    range_str, _, rest = line.partition(" ")
    start_str, _, end_str = range_str.partition("-")
    start = int(start_str)
    end = int(end_str)
    c, _, password = rest.partition(": ")

    if start <= password.count(c) <= end:
        valid1.append(password)

    a = password[start - 1]
    b = password[end - 1]

    if a != b and (a == c or b == c):
        valid2.append(password)

print(len(valid1))
print(len(valid2))
