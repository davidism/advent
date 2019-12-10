import json

from advent.load import read_input


def traverse(data, no_red=False):
    if isinstance(data, dict):
        if no_red and "red" in data.values():
            return 0

        return traverse(list(data.values()), no_red)

    if isinstance(data, list):
        return sum(traverse(x, no_red) for x in data)

    return data if isinstance(data, int) else 0


data = json.loads(read_input())
print(traverse(data))
print(traverse(data, True))
