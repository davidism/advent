from advent.load import read_input
from advent.year2020.interpreter import Program


class LoopProgram(Program):
    def __init__(self, lines):
        super().__init__(lines)
        self.seen = set()

    def run_step(self):
        if self.pos in self.seen:
            raise ValueError(f"looped to {self.pos}")

        self.seen.add(self.pos)
        return super().run_step()


p0 = LoopProgram.parse(read_input())

try:
    p0.run()
except ValueError:
    pass

print(p0.acc)

for i, (name, values) in enumerate(p0.lines):
    if name == "acc":
        continue

    name = "jmp" if name == "nop" else "nop"
    new_lines = p0.lines.copy()
    new_lines[i] = (name, values)
    p = LoopProgram(new_lines)

    try:
        p.run()
    except ValueError:
        continue

    print(i, p.acc)
    break
