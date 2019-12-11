from collections import defaultdict
from collections import deque
from typing import Deque
from typing import Dict
from typing import Iterable
from typing import List

from advent.load import read_input


def op(code: int, size: int, write=False):
    def wrapper(f):
        f.op = code
        f.size = size
        f.write = size - 1 if write else -1
        return f

    return wrapper


def find_ops(cls):
    for key, value in vars(cls).items():
        if key.startswith("op_"):
            cls._op_to_name[value.op] = key

    return cls


@find_ops
class Interpreter:
    _op_to_name: Dict[int, str] = {}

    def __init__(self, data: List[int], input=None, output=None):
        self.data = defaultdict(int, enumerate(data))
        self.pos = 0
        self.ops = {k: getattr(self, v) for k, v in self._op_to_name.items()}
        self.input = prepare_io(input)
        self.output = prepare_io(output, output=True)
        self.halted = False
        self.rel = 0

    def __getitem__(self, item: int) -> int:
        return self.data[item]

    def __setitem__(self, item: int, value: int):
        self.data[item] = value

    def run(self):
        if self.halted:
            return False

        while True:
            modes, op = divmod(self.data[self.pos], 100)
            self.pos += 1
            op = self.ops[op]
            args = [self.data[self.pos + i] for i in range(op.size)]
            self.pos += op.size

            for i, arg in enumerate(args):
                modes, mode = divmod(modes, 10)

                if mode == 0:
                    if i != op.write:
                        args[i] = self.data[arg]
                if mode == 2:
                    if i == op.write:
                        args[i] = self.rel + arg
                    else:
                        args[i] = self.data[self.rel + arg]

            try:
                op(*args)
            except HaltExecution:
                self.halted = True
                break
            except WaitInput:
                self.pos -= 1 + op.size
                break

        return True

    @op(99, 0)
    def op_halt(self):
        raise HaltExecution

    @op(1, 3, True)
    def op_add(self, a, b, dest):
        self.data[dest] = a + b

    @op(2, 3, True)
    def op_mul(self, a, b, dest):
        self.data[dest] = a * b

    @op(3, 1, True)
    def op_read(self, dest):
        try:
            value = self.input.popleft()
        except IndexError:
            raise WaitInput

        self.data[dest] = value

    @op(4, 1)
    def op_write(self, value):
        self.output.append(value)

    @op(5, 2)
    def op_jnz(self, test, goto):
        if test:
            self.pos = goto

    @op(6, 2)
    def op_jz(self, test, goto):
        if not test:
            self.pos = goto

    @op(7, 3, True)
    def op_lt(self, a, b, dest):
        self.data[dest] = int(a < b)

    @op(8, 3, True)
    def op_eq(self, a, b, dest):
        self.data[dest] = int(a == b)

    @op(9, 1)
    def op_rel(self, delta):
        self.rel += delta


class InterpreterGroup:
    def __init__(self):
        self.group: List[Interpreter] = []

    @property
    def output(self) -> deque:
        return self.group[-1].output

    def attach(self, interpreter: Interpreter):
        if not self.group:
            self.group.append(interpreter)
        else:
            self.output.extendleft(reversed(interpreter.input))
            interpreter.input = self.output
            self.group.append(interpreter)

    def feedback(self):
        self.output.extend(self.group[0].input)
        self.group[0].input = self.output

    def run(self):
        while True:
            for interpreter in self.group:
                interpreter.run()

            if any(interpreter.halted for interpreter in self.group):
                break


def prepare_io(value: Iterable[int] = None, output=False) -> Deque[int]:
    if value is None:
        return deque()

    if not (
        hasattr(value, "append" if output else "popleft") or isinstance(value, deque)
    ):
        return deque(value)

    return value


class HaltExecution(Exception):
    pass


class WaitInput(Exception):
    pass


def read_intcode(name=None) -> List[int]:
    return [int(x) for x in read_input(name, 2).split(",")]
