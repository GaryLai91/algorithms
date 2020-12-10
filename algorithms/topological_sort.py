def TopoSort(G):
    """
    Topological Sort of a DAG
    G: a graph represented as an adjacency list
    """
    vertices = list(G.keys())
    global current_label, order, explored
    explored = []
    current_label = len(vertices)
    order = {}
    for v in vertices:
        if v not in explored:
            DFS_Topo(G, v)
    order_ascending = {
        k: v
        for k, v in sorted(order.items(), key=lambda item: item[1])
    }
    return order_ascending


def DFS_Topo(G, s):
    """
    Explore the graph using DFS and mark nodes as explored
    and assign a topological ordering value
    """
    global current_label, explored
    explored.append(s)
    for v in G[s]:
        if v not in explored:
            DFS_Topo(G, v)

    order[s] = current_label
    current_label -= 1


if __name__ == "__main__":
    G = {'A': ['B', 'C'], 'B': [], 'C': ['D'], 'D': []}
    order = TopoSort(G)
    print(order)