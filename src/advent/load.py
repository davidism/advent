import inspect
from itertools import chain
from itertools import islice
from pathlib import Path
from typing import Iterable
from typing import List
from typing import Union


def read_line(source: Iterable[str]) -> str:
    if isinstance(source, str):
        return source.strip("\n")

    return next(iter(source)).strip("\n")


def read_lines(source: Iterable[str]) -> List[str]:
    if isinstance(source, str):
        source = source.splitlines()

    return [l for l in (l.strip("\n") for l in source) if l]


def read_input(name: str = None, back: int = 1) -> Union[str, List[str]]:
    frame = inspect.currentframe()

    while frame and back:
        frame = frame.f_back
        back -= 1

    py_path = Path(frame.f_globals["__file__"])

    if name is None:
        name = py_path.stem + ".txt"

    name_path = Path(name)

    if name_path.exists():
        path = name_path
    else:
        path = py_path.with_name(name)

    with path.open(encoding="utf8") as f:
        head = list(islice(f, 3))

        if len(head) == 1 or len(head) == 2 and not head[1].strip():
            return read_line(head[0])

        return read_lines(chain(head, f))
