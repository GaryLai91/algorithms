from random import choice, seed
from collections import defaultdict

#seed(42)


def get_data(filename):
    with open(filename, 'r') as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            # can change delimiter to "\t" for challenge.txt
            arr = [int(i) for i in line.split(" ") if i != ""]
            for i in arr:
                for j in arr:
                    if i != j:
                        graph[i].append(j)
    return graph

def pick_edge(graph):
    """
    Given an adjacent list, randomly pick an edge
    and return its vertices
    """
    head = choice(list(graph.keys()))
    tail = choice([i for i in graph[head] if i != head])
    return head, tail

def merge(g, u, v):
    """
    Merge the 2 vertices u and v into 1 super node.
    v gets eaten by u, so we transfer all vertices connected to v to u. 
    """
    for i in g[v]:
        if i != u and i != v:
            g[u].append(i)
        for j in range(len(g[i])):
            if g[i][j] == v:
                g[i][j] = u
    del g[v]


def remove_self_loop(g, u):
    g[u] = [i for i in g[u] if i != u]
    


def random_contraction(graph):
    g = graph
    while len(g.keys()) > 2:
        # print(g)
        u,v = pick_edge(g)
        # print(f"u: {u}, v: {v}")
        merge(g, u, v)
        remove_self_loop(g, u)
    return len(g)


if __name__ == "__main__":
    graph = get_data("data.txt")
    num = 1000
    total = 0
    
    random_contraction(graph)
    for k in graph:
        print(f"Key: {k}, length: {len(graph[k])}")