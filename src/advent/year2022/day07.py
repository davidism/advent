from collections import defaultdict
from pathlib import PurePosixPath

from advent.load import read_input

history: list[str] = list(reversed(read_input()))
history.insert(0, "$")
fs: dict[PurePosixPath, int] = defaultdict(int)
cwd = PurePosixPath("/")
state = "prompt"
output = []

while history:
    line = history.pop()

    if state == "prompt":
        if line.startswith("$ cd"):
            target = line.rpartition(" ")[2]

            if target == "..":
                cwd = cwd.parent
            else:
                cwd /= target
        elif line.startswith("$ ls"):
            state = "ls"
    else:
        if line.startswith("$"):
            total = sum(int(ol.partition(" ")[0]) for ol in output)
            fs[cwd] += total

            for p in cwd.parents:
                fs[p] += total

            output.clear()
            state = "prompt"
            history.append(line)
            continue

        if line.startswith("dir"):
            continue

        output.append(line)

print(sum(v for v in fs.values() if v < 100_000))
need = 30_000_000 - (70_000_000 - fs[PurePosixPath("/")])
print(min(v for v in fs.values() if v >= need))
