from advent.load import read_input

data = [[int(x) for x in g] for g in read_input(group=True)]
totals = sorted((sum(g) for g in data), reverse=True)
print(totals[0])
print(sum(totals[:3]))
