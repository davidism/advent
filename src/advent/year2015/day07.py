from collections import deque
from functools import partial

from advent.load import read_input


def maybe_int(value):
    try:
        return int(value)
    except ValueError:
        return value


def getter(signals, value):
    if isinstance(value, int):
        return lambda: value

    return lambda: signals[value]


def setter(signals, key):
    def f(value):
        signals[key] = value

    return f


op_func = {
    "INPUT": lambda s, a: s(a()),
    "AND": lambda s, a, b: s(a() & b()),
    "OR": lambda s, a, b: s(a() | b()),
    "NOT": lambda s, a: s(~a()),
    "LSHIFT": lambda s, a, b: s(a() << b()),
    "RSHIFT": lambda s, a, b: s(a() >> b()),
}


def run(lines, override=None):
    ops = deque()
    s = {}

    for line in lines:
        op, d = line.split(" -> ")
        tokens = [maybe_int(x) for x in op.split()]

        if override and d == "b":
            tokens = [override]

        if len(tokens) == 1:
            op = op_func["INPUT"]
            args = tokens
        elif len(tokens) == 2:
            op = op_func[tokens[0]]
            args = tokens[1:]
        else:
            op = op_func[tokens[1]]
            args = (tokens[0], tokens[2])

        ops.append(partial(op, *([setter(s, d)] + [getter(s, a) for a in args])))

    while ops:
        op = ops.popleft()

        try:
            op()
        except KeyError:
            ops.append(op)

    return s["a"]


data = read_input()
wire = run(data)
print(wire)
print(run(data, wire))
