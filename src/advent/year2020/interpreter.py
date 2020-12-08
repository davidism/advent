from collections import Callable
from typing import Dict


def find_ops(p):
    out = {}

    for name in dir(p):
        if name.startswith("op_"):
            out[name[3:]] = name

    p._op_to_name = out
    return p


@find_ops
class Program:
    _op_to_name: Dict[str, str]
    ops: Dict[str, Callable[..., None]]
    pos: int
    acc: int

    def __init__(self, lines):
        self.ops = {}

        for op, name in self._op_to_name.items():
            self.ops[op] = getattr(self, name)

        self.lines = lines
        self.length = len(lines)
        self.reset()

    def reset(self):
        self.pos = 0
        self.acc = 0

    @classmethod
    def parse(cls, lines):
        out = []

        for line in lines:
            name, *values = line.split(" ")
            values = [int(v) for v in values]
            out.append((name, values))

        return cls(out)

    def run(self):
        while self.run_step():
            pass

    def run_step(self):
        if self.pos >= self.length:
            return False

        name, values = self.lines[self.pos]
        f = self.ops[name]
        f(*values)
        self.pos += 1
        return True

    def op_acc(self, value):
        self.acc += value

    def op_jmp(self, value):
        self.pos += value - 1

    def op_nop(self, value):
        pass
