import statistics

from advent.load import read_input

data = [int(x) for x in read_input().split(",")]
lin = statistics.median(data)
print(lin, sum(abs(x - lin) for x in data))
tri = int(statistics.mean(data))
print(tri, sum(x * (x + 1) / 2 for x in (abs(x - tri) for x in data)))

# fuel = [
#     (
#         i,
#         sum(abs(x - i) for x in data),
#         sum(x * (x + 1) / 2 for x in (abs(x - i) for x in data)),
#     )
#     for i in range(max(data))
# ]
# print(min(fuel, key=lambda x: x[1]))  # median
# print(min(fuel, key=lambda x: x[2]))  # int(mean)
