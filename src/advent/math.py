from functools import reduce
from math import gcd


def lcm(*args):
    return reduce(lambda a, b: a * b // gcd(a, b), args)
