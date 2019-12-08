from itertools import permutations

from advent.year2019.intcode import Interpreter
from advent.year2019.intcode import InterpreterGroup
from advent.year2019.intcode import read_intcode


def find_max(data, signal_range, feedback=False):
    max_signal = 0

    for phase, *phases in permutations(signal_range):
        group = InterpreterGroup()
        group.attach(Interpreter(data, [phase, 0]))

        for phase in phases:
            group.attach(Interpreter(data, [phase]))

        if feedback:
            group.feedback()

        group.run()
        signal = group.output[0]

        if signal > max_signal:
            max_signal = signal

    return max_signal


data = read_intcode()
print(find_max(data, range(5)))
print(find_max(data, range(5, 10), True))
