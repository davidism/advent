from advent.load import read_input


def module_fuel(v):
    total = v // 3 - 2
    fuel = total

    while fuel > 8:
        fuel = fuel // 3 - 2

        if fuel > 0:
            total += fuel

    return total


data = [int(x) for x in read_input()]
print(sum(v // 3 - 2 for v in data))
print(sum(module_fuel(v) for v in data))
