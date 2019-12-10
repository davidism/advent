from itertools import groupby


def look_and_say(value, n=1):
    out = value

    for _ in range(n):
        acc = ""

        for c, group in groupby(out):
            acc += str(len(list(group))) + c

        out = acc

    return out


print(len(look_and_say("1113122113", 40)))
print(len(look_and_say("1113122113", 50)))
