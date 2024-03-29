import inspect
from itertools import chain
from itertools import groupby
from itertools import islice
from pathlib import Path
from typing import Iterable
from typing import Literal
from typing import overload


def read_line(source: Iterable[str]) -> str:
    if isinstance(source, str):
        return source.strip("\n")

    return next(iter(source)).strip("\n")


@overload
def read_lines(source: Iterable[str], group: Literal[False] = ...) -> list[str]:
    ...


@overload
def read_lines(source: Iterable[str], group: Literal[True] = ...) -> list[list[str]]:
    ...


def read_lines(
    source: Iterable[str], group: bool = False
) -> list[str] | list[list[str]]:
    if isinstance(source, str):
        source = source.splitlines()

    source = (line.strip("\n") for line in source)

    if group:
        return [list(g) for k, g in groupby(source, key=bool) if k]

    return [line for line in source if line]


@overload
def read_input(
    name: str = None, back: int = 1, group: Literal[False] = ...
) -> str | list[str]:
    ...


@overload
def read_input(
    name: str = None, back: int = 1, group: Literal[True] = ...
) -> list[list[str]]:
    ...


def read_input(
    name: str = None, back: int = 1, group: bool = False
) -> str | list[str] | list[list[str]]:
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

        if not group and len(head) == 1 or len(head) == 2 and not head[1].strip():
            return read_line(head[0])

        return read_lines(chain(head, f), group=group)
