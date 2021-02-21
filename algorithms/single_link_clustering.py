from collections import defaultdict
from union_find import UF
from scipy.spatial.distance import hamming
import heapq


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


def get_bin_input(filename):
    graph = {}
    with open(filename, 'r') as f:
        n = [int(i) for i in f.readline().strip().split(" ")]
        for i in range(1, n[0] + 1):
            line = f.readline()
            arr = [int(j) for j in line.strip().split(" ")]
            graph[i] = arr
    return graph


def create_hamming_graph(bin_input):
    graph = defaultdict(dict)
    for u in bin_input.keys():
        for v in bin_input.keys():
            try:
                graph[u][v]
            except KeyError:
                if u != v:
                    w = hamming(bin_input[u], bin_input[v]) * len(bin_input[u])
                    graph[u][v] = int(w)
                    graph[v][u] = int(w)
    return graph


def create_normal_graph(hamming_graph):
    graph = defaultdict(list)
    for u in hamming_graph.keys():
        for v in hamming_graph[u].keys():
            graph[u].append((v, hamming_graph[u][v]))
    return graph


def hamming_clustering(data):
    hamming_graph = create_hamming_graph(data)
    print("Finish creating hamming graph")
    graph = create_normal_graph(hamming_graph)
    print("Finish creating normal graph")
    print("Start computing clusters...")
    n_clusters = heap_clustering(graph)
    return n_clusters


def heap_clustering(graph):
    """
    args: graph
        graph = {
            u: [(v_1, w_1), (v_2, w_2), ...]
        }
    """
    uf = UF(len(graph))
    edges = []
    for u in graph.keys():
        for v, w in graph[u]:
            heapq.heappush(edges, (w, u, v))
    edges_union = []
    while len(edges) > 0:
        w, u, v = heapq.heappop(edges)
        if uf.find(u - 1) != uf.find(v - 1) and w <= 2:
            uf.union(u - 1, v - 1)
            edges_union.append((u, v))

    return len(set(uf.parent))
