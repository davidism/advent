import dataclasses
import operator
from functools import reduce
from itertools import islice
from typing import Iterable
from typing import Optional

from advent.load import read_input


@dataclasses.dataclass
class Packet:
    version: int
    type: int

    def version_sum(self) -> int:
        return self.version

    def calculate(self):
        raise NotImplementedError


@dataclasses.dataclass
class Literal(Packet):
    value: int

    def calculate(self):
        return self.value


@dataclasses.dataclass
class Operator(Packet):
    packets: list[Packet]

    def version_sum(self) -> int:
        return sum((p.version_sum() for p in self.packets)) + self.version

    def calculate(self) -> int:
        values = [p.calculate() for p in self.packets]

        if self.type == 0:
            return sum(values)

        if self.type == 1:
            return reduce(operator.mul, values)

        if self.type == 2:
            return min(values)

        if self.type == 3:
            return max(values)

        if self.type == 5:
            return int(values[0] > values[1])

        if self.type == 6:
            return int(values[0] < values[1])

        if self.type == 7:
            return int(values[0] == values[1])

        raise ValueError


def hex_to_bits(hex_str: str) -> list[int]:
    bin_str = bin(int(hex_str, 16))[2:]
    r = len(bin_str) % 4

    if r:
        bin_str = "0" * (4 - r) + bin_str

    return list(map(int, bin_str))


def bits_to_int(bits: Iterable[int]) -> int:
    return reduce(lambda out, bit: (out << 1) | bit, bits)


def take_n(stream: Iterable[int], n: int) -> list[int]:
    out = list(islice(stream, n))

    if len(out) != n:
        raise StopIteration

    return out


def bits_to_packets(
    bits: Iterable[int], packet_count: Optional[int] = None
) -> list[Packet]:
    stream = iter(bits)
    out: list[Packet] = []

    try:
        while packet_count is None or len(out) < packet_count:
            version = bits_to_int(take_n(stream, 3))
            type = bits_to_int(take_n(stream, 3))

            if type == 4:
                value_bits = []
                stop = False

                while not stop:
                    stop = not next(stream)
                    value_bits.extend(take_n(stream, 4))

                out.append(Literal(version, type, bits_to_int(value_bits)))
            else:
                nest_stream = stream
                nest_count = None

                if next(stream) == 0:
                    nest_stream = take_n(stream, bits_to_int(take_n(stream, 15)))
                else:
                    nest_count = bits_to_int(take_n(stream, 11))

                out.append(
                    Operator(version, type, bits_to_packets(nest_stream, nest_count))
                )
    except StopIteration:
        pass

    return out


p = bits_to_packets(hex_to_bits(read_input()))[0]
print(p.version_sum())
print(p.calculate())
