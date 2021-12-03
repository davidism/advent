from advent.load import read_input


def count_ones(lines: list[str], i: int) -> int:
    return sum(v[i] == "1" for v in lines)


def power_consumption(lines: list[str]) -> int:
    width = len(lines[0])
    midpoint = len(lines) / 2
    gamma = 0
    epsilon = 0

    for i in range(width):
        if count_ones(lines, i) >= midpoint:
            gamma |= 1 << (width - 1 - i)
        else:
            epsilon |= 1 << (width - 1 - i)

    return gamma * epsilon


def gas_rating(lines: list[str], keep_high: bool) -> int:
    width = len(lines[0])

    for i in range(width):
        if len(lines) == 1:
            break

        c = "1" if (count_ones(lines, i) >= len(lines) / 2) is keep_high else "0"
        lines = [v for v in lines if v[i] == c]

    assert len(lines) == 1
    return int(lines[0], 2)


def life_support_rating(lines: list[str]) -> int:
    oxygen_rating = gas_rating(lines.copy(), True)
    co2_rating = gas_rating(lines.copy(), False)
    return oxygen_rating * co2_rating


def diagnostics(lines):
    print(power_consumption(lines))
    print(life_support_rating(lines))


diagnostics(read_input())
