from collections import defaultdict

from advent.load import read_input

lines = [x.split(" = ", 1) for x in read_input()]
mem = defaultdict(int)
v2_mem = defaultdict(int)
mask = ""


def apply_mask(mask, value):
    value = bin(value)[2:].zfill(36)
    out = []

    for mc, vc in zip(mask, value):
        if mc == "X":
            out.append(vc)
        else:
            out.append(mc)

    return int("".join(out), 2)


def v2_mask(mask, addr):
    value = bin(addr)[2:].zfill(36)
    builds = [[]]

    for mc, vc in zip(mask, value):
        if mc == "0":
            for b in builds:
                b.append(vc)
        elif mc == "1":
            for b in builds:
                b.append("1")
        else:
            new_builds = []

            for b in builds:
                new_b = b.copy()
                new_b.append("1")
                new_builds.append(new_b)
                b.append("0")

            builds.extend(new_builds)

    for b in builds:
        yield int("".join(b), 2)


for op, value in lines:
    if op == "mask":
        mask = value
    else:
        addr = int(op[4:-1])
        value = int(value)
        mem[addr] = apply_mask(mask, value)

        for addr in v2_mask(mask, addr):
            v2_mem[addr] = value

print(sum(mem.values()))
print(sum(v2_mem.values()))
