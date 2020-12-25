def DFS(G, s):
    """
    A vertex is reachable from s if 
    and only if it is marked as explored
    G: a graph represented as an adjacency list
    s: source node
    """
    explored = []
    stack = [s]

    while len(stack) > 0:
        v = stack.pop()
        print(f"Exploring node {v}")
        if v not in explored:
            explored.append(v)
            for w in G[v]:
                stack.append(w)


def DFS_recursive(G, s):
    """
    A vertex is reachable from s if 
    and only if it is marked as explored in a recursive fashion
    G: a graph represented as an adjacency list
    s: source node
    """
    explored = [s]
    for v in G[s]:
        if v not in explored:
            DFS_recursive(G, v)
