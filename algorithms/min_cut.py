from random import choice, seed, sample
from collections import defaultdict
from copy import deepcopy


def get_data(filename):
    with open(filename, "r") as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            # can change delimiter to "\t" for challenge.txt
            arr = [int(i) for i in line.split("\t") if i != ""]
            graph[arr[0]] = arr[1:]
    return graph


def pick_edge(g):
    """
    Given an adjacent list, randomly pick an edge
    and return its vertices
    """
    u = choice(list(g.keys()))
    v = choice(list(set(g[u])))
    return u, v


def merge(g, u, v):
    """
    Merge the 2 vertices u and v into 1 super node.
    v gets eaten by u, so we transfer all vertices connected to v to u. 
    """
    g[u] = [i for i in g[u] if i != v]
    for i in g[v]:
        if i != u:
            g[u].append(i)
            for j in range(len(g[i])):
                if g[i][j] == v:
                    g[i][j] = u
    del g[v]
    return g


def MinCut(graph):
    g = deepcopy(graph)
    while len(g.keys()) > 2:
        u, v = pick_edge(g)
        g = merge(g, u, v)
    cut = len(g[list(g.keys())[0]])
    return cut


def simulate_mincut(graph):
    min_ = 99999999999999999
    for i in range(1, 5001):
        min_cut = MinCut(graph)
        print(f"{i+1}th iteration: {min_cut}")
        if min_cut < min_:
            min_ = min_cut
    return min_


if __name__ == "__main__":
    graph = get_data(input_dir)
    with open(output_dir, "r") as f:
        output = [int(i) for i in f.readlines()][0]
    min_ = 99999999999999999
    for i in range(1, 5001):
        min_cut = MinCut(graph)
        print(f"{i+1}th iteration: {min_cut}")
        if min_cut < min_:
            min_ = min_cut
    print(f"MinCut: {min_}")
    print(f"Answer: {output}")
