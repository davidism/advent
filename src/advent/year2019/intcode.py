from advent.load import read_input


def op(code: int, size: int, write: bool = False):
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
    _op_to_name = {}

    def __init__(self, data, input=()):
        self.data = data.copy()
        self.pos = 0
        self.ops = {k: getattr(self, v) for k, v in self._op_to_name.items()}
        self.input = iter(input)
        self.output = []

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, item, value):
        self.data[item] = value

    def run(self):
        while True:
            modes, op = divmod(self.data[self.pos], 100)
            self.pos += 1
            op = self.ops[op]
            args = self.data[self.pos : self.pos + op.size]
            self.pos += op.size

            for i, arg in enumerate(args):
                modes, mode = divmod(modes, 10)

                if not mode and i != op.write:
                    args[i] = self.data[arg]

            try:
                op(*args)
            except HaltExecution:
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
        value = next(self.input)
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


class HaltExecution(Exception):
    pass


def read_intcode(name=None):
    return [int(x) for x in read_input(name, 2).split(",")]
