from advent.load import read_input


def op(code: int, size: int):
    def wrapper(f):
        f.op = code
        f.size = size
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

    def __init__(self, data):
        self.data = data.copy()
        self.pos = 0
        self.ops = {k: getattr(self, v) for k, v in self._op_to_name.items()}

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, item, value):
        self.data[item] = value

    def run(self):
        while True:
            op = self.ops[self.data[self.pos]]
            self.pos += 1
            args = self.data[self.pos : self.pos + op.size]
            self.pos += op.size

            try:
                op(*args)
            except HaltExecution:
                break

        return True

    def deref(self, addr, value=None):
        if value is not None:
            self.data[addr] = value

        return self.data[addr]

    @op(99, 0)
    def op_halt(self):
        raise HaltExecution

    @op(1, 3)
    def op_add(self, a, b, dest):
        self.deref(dest, self.deref(a) + self.deref(b))

    @op(2, 3)
    def op_mul(self, a, b, dest):
        self.deref(dest, self.deref(a) * self.deref(b))


class HaltExecution(Exception):
    pass


def read_intcode(name=None):
    return [int(x) for x in read_input(name, 2).split(",")]
