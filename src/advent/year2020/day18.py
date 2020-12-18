import operator
from collections import deque

from advent.load import read_input

ops = {
    "+": operator.add,
    "*": operator.mul,
}


def do_math(q):
    value = None
    op = None

    while q:
        c = q.popleft()

        if c == "(":
            if value is None:
                value = do_math(q)
            else:
                value = op(value, do_math(q))
        elif c == ")":
            return value
        elif isinstance(c, int):
            if value is None:
                value = c
            else:
                value = op(value, c)
        else:
            op = ops[c]

    return value


def line2q(line):
    return deque((int(c) if c.isdigit() else c) for c in line)


def parenthesize(line):
    out = ["(("]

    for c in line:
        if c == "(":
            out.append("(((")
        elif c == ")":
            out.append(")))")
        elif c == "+":
            out.append(")+(")
        elif c == "*":
            out.append("))*((")
        else:
            out.append(c)

    out.append("))")
    return "".join(out)


out1 = []
out2 = []

for line in read_input():
    line = line.replace(" ", "")
    out1.append(do_math(line2q(line)))
    out2.append(do_math(line2q(parenthesize(line))))

print(sum(out1))
print(sum(out2))
