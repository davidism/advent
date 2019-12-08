from more_itertools import sliced

from advent.load import read_input

data = [int(x) for x in read_input()]
layers = list(sliced(data, 25 * 6))
layer = min(layers, key=lambda x: x.count(0))
print(layer.count(1) * layer.count(2))
canvas = [2] * 25 * 6

for layer in layers:
    for i, c in enumerate(layer):
        if c != 2 and canvas[i] == 2:
            canvas[i] = c

for row in sliced(canvas, 25):
    print("".join(" +"[p] for p in row))
