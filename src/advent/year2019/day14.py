import re
from collections import defaultdict
from collections import deque

from advent.load import read_input


def parse_input(lines):
    out = {}

    for line in lines:
        *reqs, res = ((k, int(v)) for v, k in re.findall(r"(\d+) (\w+)", line))
        out[res[0]] = reqs, res

    return out


def ore_for_fuel(rules, fuel=1):
    q = deque(["FUEL"])
    need = defaultdict(int, {"FUEL": fuel})
    have = defaultdict(int)
    used = defaultdict(int)

    while q:
        res = q.popleft()

        if need[res] <= have[res]:
            have[res] -= need[res]
            used[res] += need[res]
            need[res] = 0
        else:
            reqs, (_, res_get) = rules[res]
            scale, carry = divmod(need[res] - have[res], res_get)
            scale += bool(carry)
            q.append(res)
            have[res] += res_get * scale

            for req, req_need in reqs:
                need[req] += req_need * scale
                q.append(req)

                if req == "ORE":
                    have["ORE"] += req_need * scale

    return used["ORE"]


def fuel_from_ore(rules, ore=1000000000000):
    guess_min = 1
    guess = ore // 2
    guess_max = ore

    while guess != guess_min:
        out = ore_for_fuel(rules, guess)

        if out == ore:
            return guess
        elif out > ore:
            guess_max = guess - 1
        elif out < ore:
            guess_min = guess + 1

        guess = (guess_min + guess_max) // 2

    return guess


data = parse_input(read_input())
print(ore_for_fuel(data))
print(fuel_from_ore(data))
