from collections import defaultdict
from union_find import UF
from algorithms.mst_prim import get_input


def clustering(graph, n_clusters=4):
    """
    args: graph
        graph = {
            u: [(v_1, w_1), (v_2, w_2), ...]
        }
    """
    uf = UF(len(graph))
    t = set()
    cost = 0
    edges = []
    for u in graph.keys():
        for v, w in graph[u]:
            edges.append((u, v, w))
    edges = sorted(edges, key=lambda x: x[2])
    edges_index = 0
    #while len(set(uf.parent)) > n_clusters and edges_index < len(edges):
    while len(t) != len(graph.keys()) - n_clusters:
        # print(uf.parent)
        u, v, w = edges[edges_index]
        if uf.find(u - 1) != uf.find(v - 1):
            t = t.union([tuple(sorted([u, v]))])
            uf.union(u - 1, v - 1)
        edges_index += 1

    max_space = calculate_max_distance(edges, uf)

    return max_space


def calculate_max_distance(edges, uf):
    """
    args:
        rank = [1, 1, 1, 1, 8, 1, 1, 1]
    """
    max_space = 999999999
    for u, v, w in edges:
        if uf.find(u - 1) != uf.find(v - 1) and w < max_space:
            max_space = w
    return max_space


if __name__ == "__main__":
    data = get_input("test.txt")
    max_space = clustering(data)
    print(max_space)