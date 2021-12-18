from functools import cache
from functools import reduce
from math import gcd


def lcm(*args):
    return reduce(lambda a, b: a * b // gcd(a, b), args)


@cache
def triangular(x: int) -> int:
    return x * (x + 1) // 2
