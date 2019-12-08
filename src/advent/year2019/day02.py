from itertools import product

from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import read_intcode

data = read_intcode()


def run_input(a, b):
    c = Interpreter(data)
    c[1] = a
    c[2] = b
    c.run()
    return c[0]


print(run_input(12, 2))


for b, a in product(range(100), repeat=2):
    if run_input(a, b) == 19690720:
        print(a * 100 + b)
        break
