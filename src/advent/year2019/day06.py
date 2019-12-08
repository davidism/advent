import networkx as nx

from advent.load import read_input

dg = nx.Graph(x.split(")") for x in read_input())
print(sum(dict(nx.all_pairs_shortest_path_length(dg))["COM"].values()))
g = dg.to_undirected()
print(nx.shortest_path_length(g, next(g.neighbors("YOU")), next(g.neighbors("SAN"))))
