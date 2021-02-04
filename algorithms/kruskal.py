from collections import defaultdict
from algorithms.mst_prim import get_input
from queue import Queue
from copy import deepcopy
from union_find import UF


def detect_cycle(graph, s):
    parent = {k: -1 for k in graph.keys()}
    visited = {k: False for k in graph.keys()}
    visited[s] = True
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                parent[v] = u
            elif parent[u] != v:
                return True
    return False


def kruskal_mst(graph):
    """
    args: graph
        graph = {
            u: [(v_1, w_1), (v_2, w_2), ...]
        }
    """
    bfs_graph = defaultdict(set)
    edges = []
    t = set()
    cost = 0
    for u in graph.keys():
        for v, w in graph[u]:
            edges.append((u, v, w))
    edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in edges:
        bfs_graph_addition = deepcopy(bfs_graph)
        bfs_graph_addition[u].add(v)
        bfs_graph_addition[v].add(u)
        if not detect_cycle(bfs_graph_addition, u) and tuple(sorted(
            [u, v])) not in t:
            t = t.union([tuple(sorted([u, v]))])
            cost += w
            bfs_graph[u].add(v)
            bfs_graph[v].add(u)
    return cost


def kruskal_uf(graph):
    uf = UF(len(graph))
    t = set()
    cost = 0
    edges = []
    for u in graph.keys():
        for v, w in graph[u]:
            edges.append((u, v, w))
    edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in edges:
        if uf.find(u - 1) != uf.find(v - 1):
            t = t.union([tuple(sorted([u, v]))])
            uf.union(u - 1, v - 1)
            cost += w
    return cost


if __name__ == "__main__":
    data = get_input("test.txt")
    # print(data)
    # print(len(data))
    print(kruskal_uf(data))