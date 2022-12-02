from math import sqrt


def divisors(number: int) -> list[int]:
    divisors = {1, number}

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)

    return sorted(divisors)


def part1(target: int) -> int:
    target //= 10

    for house in range(1, target):
        if sum(divisors(house)) >= target:
            return house


def part2(target: int) -> int:
    target //= 11

    for house in range(1, target):
        if sum(i for i in divisors(house) if house // i <= 50) >= target:
            return house


target = 33100000
print(part1(target))
print(part2(target))
