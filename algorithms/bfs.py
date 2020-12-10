from queue import Queue
from collections import defaultdict


class Node():
    def __init__(self, name, adjacent_nodes):
        self.visited = False
        self.name = name
        self.adjacent_nodes = adjacent_nodes
        self.level = 99999999
        self.visited_from = ""


def BFS(G, s):
    """
    G is the graph G = (V, E) representated
    in an adjacency-list
    s : Source vertex
    """
    g = {}
    for vertex in G:
        g[vertex] = Node(vertex, G[vertex])
    g[s].visited = True
    g[s].level = 0
    q = Queue()
    q.put(g[s])

    while not q.empty():
        v = q.get()
        for w in v.adjacent_nodes:
            if not g[w].visited:
                g[w].visited = True
                g[w].level = v.level + 1
                g[w].visited_from = v.name
                q.put(g[w])


def UCC(G):
    """
    G: graph G = (V, E) in adjacency-list representation,
    with V = {1,2,3,4,...,n}
    For every u,v in V, cc(u) = cc(v) iff u,v are
    in the same connected component
    """
    explored = {}
    connected_component = defaultdict(set)
    num_cc = 0
    for node in list(G.keys()):
        try:
            _ = explored[node]  # unexplored nodes will throw error
        except KeyError:
            num_cc += 1
            q = Queue()
            q.put(node)
            while not q.empty():
                v = q.get()
                connected_component[num_cc].update([v])
                for w in G[v]:
                    try:
                        _ = explored[w]
                    except KeyError:
                        explored[w] = 1
                        q.put(w)
    return connected_component


if __name__ == "__main__":
    # G = {
    #     "s": ["a", "b"],
    #     "a": ["s", "c"],
    #     "b": ["s", "c", "d"],
    #     "c": ["a", "b", "d", "e"],
    #     "d": ["b", "c", "e"],
    #     "e": ["c", "d"]
    # }
    # BFS(G, 's')
    G = {
        1: [3, 5],
        2: [4],
        3: [1, 5],
        4: [2],
        5: [1, 3, 7, 9],
        6: [8, 10],
        7: [5],
        8: [6],
        9: [5],
        10: [6]
    }
    cc = UCC(G)
    print(cc)