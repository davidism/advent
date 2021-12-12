import networkx as nx

from advent.load import read_input


def parse_graph(lines: list[str]) -> nx.Graph:
    g = nx.Graph()

    for line in lines:
        a, _, b = line.partition("-")
        g.add_edge(a, b)

    return g


def _find_paths(
    g: nx.Graph, seen: set[str], path: list[str], has_twice: bool, allow_twice: bool
) -> list[list[str]]:
    if path[-1] == "end":
        return [path]

    out = []

    for n in g.neighbors(path[-1]):
        if n == "start":
            continue

        if n in seen and n.islower():
            if not allow_twice or has_twice:
                continue

            n_has_twice = True
        else:
            n_has_twice = has_twice

        n_seen = seen.copy()
        n_seen.add(n)
        n_path = path.copy()
        n_path.append(n)
        out.extend(_find_paths(g, n_seen, n_path, n_has_twice, allow_twice))

    return out


def find_paths(g: nx.Graph, allow_twice: bool = False) -> list[list[str]]:
    return _find_paths(g, {"start"}, ["start"], False, allow_twice)


lines = read_input()
g = parse_graph(lines)
print(len(find_paths(g)))
print(len(find_paths(g, True)))
