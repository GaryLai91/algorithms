from topological_sort import TopoSort
from collections import Counter

num_scc = 0
scc = {}
explored = []


def reverse_graph(G):
    """
    Reverse a directed graph represented as an adjacency list
    """
    g_rev = {k: [] for k in G.keys()}
    for k in G.keys():
        for v in G[k]:
            g_rev[v].append(k)
    return g_rev


def format_scc(scc):
    """
    Helper function to get top 5 scc sizes for 
    homework solutions and test case purposes
    """
    count = Counter(scc.values())
    values = sorted(list(count.values()), reverse=True)
    while len(values) < 5:
        values.append(0)
    return values


def DFS_SCC(G, s):
    """
    Evert vertex reachable from s is marked as explored 
    and has an assigned scc-value
    """
    global num_scc, scc, explored
    explored.append(s)
    scc[s] = num_scc
    for v in G[s]:
        if v not in explored:
            DFS_SCC(G, v)


def Kosaraju(G):
    """
    Find strongly connected components.
    """
    global num_scc, scc, explored
    g_rev = reverse_graph(G)
    g_rev_order = TopoSort(g_rev)
    for v in g_rev_order.keys():
        if v not in explored:
            num_scc += 1
            DFS_SCC(G, v)
    return format_scc(scc)


# if __name__ == "__main__":
#     G = {
#         1: [2],
#         2: [3, 4, 5],
#         3: [6],
#         4: [5, 7],
#         5: [2, 6, 7],
#         6: [3, 8],
#         7: [8, 10],
#         8: [7],
#         9: [7],
#         10: [9, 11],
#         11: [12],
#         12: [10]
#     }
#     scc = Kosaraju(G)
#     print(scc)
