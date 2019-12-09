from advent.load import read_input


def decoded_length(value):
    cs = iter(value)
    total = 0

    for c in cs:
        total += 1

        if c == "\\":
            c = next(cs)

            if c == "x":
                next(cs)
                next(cs)
            elif c not in {"\\", '"'}:
                total += 1

    return total - 2


def encoded_length(value):
    return sum(2 if c in {"\\", '"'} else 1 for c in value) + 2


data = read_input()
print(sum(len(x) - decoded_length(x) for x in data))
print(sum(encoded_length(x) - len(x) for x in data))
