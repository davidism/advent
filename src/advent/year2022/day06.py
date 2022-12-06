from more_itertools import windowed

from advent.load import read_input


def find_marker(data: str, size: int) -> int:
    for i, chars in enumerate(windowed(data, size), start=size):
        if len(set(chars)) == size:
            return i


data = read_input()
print(find_marker(data, 4))
print(find_marker(data, 14))
