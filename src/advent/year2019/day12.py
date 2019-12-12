import re
from itertools import permutations

import attr

from advent.load import read_input
from advent.math import lcm


@attr.dataclass(slots=True)
class Moon:
    x: int
    y: int
    z: int
    vx: int = attr.ib(init=False, default=0)
    vy: int = attr.ib(init=False, default=0)
    vz: int = attr.ib(init=False, default=0)

    @classmethod
    def from_line(cls, line):
        return cls(*map(int, re.findall(r"-?\d+", line)))

    def apply_gravity(self, other):
        self.vx += (-1 if self.x > other.x else 1) if self.x != other.x else 0
        self.vy += (-1 if self.y > other.y else 1) if self.y != other.y else 0
        self.vz += (-1 if self.z > other.z else 1) if self.z != other.z else 0

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def potential_energy(self):
        return sum(map(abs, (self.x, self.y, self.z)))

    @property
    def kinetic_energy(self):
        return sum(map(abs, (self.vx, self.vy, self.vz)))

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy


class System:
    def __init__(self, moons):
        self.moons = moons
        self.pairs = list(permutations(self.moons, 2))
        self.time = 0
        self.seen_x = set()
        self.seen_y = set()
        self.seen_z = set()
        self.rx = self.ry = self.rz = None
        self._record_state()

    @classmethod
    def from_lines(cls, lines):
        return cls([Moon.from_line(line) for line in lines])

    def step(self):
        for m1, m2 in self.pairs:
            m1.apply_gravity(m2)

        for m in self.moons:
            m.apply_velocity()

        self.time += 1
        self._record_state()

    def n_steps(self, n):
        for _ in range(n):
            self.step()

    @property
    def total_energy(self):
        return sum(m.total_energy for m in self.moons)

    def _record_state(self):
        hx = hash(tuple((m.x, m.vx) for m in self.moons))
        hy = hash(tuple((m.y, m.vy) for m in self.moons))
        hz = hash(tuple((m.z, m.vz) for m in self.moons))

        if self.rx is None and hx in self.seen_x:
            self.rx = self.time

        if self.ry is None and hy in self.seen_y:
            self.ry = self.time

        if self.rz is None and hz in self.seen_z:
            self.rz = self.time

        self.seen_x.add(hx)
        self.seen_y.add(hy)
        self.seen_z.add(hz)

    def find_repeat(self):
        while not all((self.rx, self.ry, self.rz)):
            self.step()

        return lcm(self.rx, self.ry, self.rz)


system = System.from_lines(read_input())
system.n_steps(1000)
print(system.total_energy)

system = System.from_lines(read_input())
print(system.find_repeat())
