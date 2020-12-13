from collections import Counter


class Kosaraju():
    def __init__(self, graph):
        self.graph = graph
        self.num_scc = 0
        self.scc = {}
        self.explored = []
        self.current_label = len(self.graph)
        self.topo_explored = []
        self.topo_order = {}

    def _reverse_graph(self, G):
        """
        Reverse a directed graph represented as an adjacency list
        """
        g_rev = {k: [] for k in G.keys()}
        for k in G.keys():
            for v in G[k]:
                g_rev[v].append(k)
        return g_rev

    def _format_scc(self, scc):
        """
        Helper function to get top 5 scc sizes for 
        homework solutions and test case purposes
        """
        count = Counter(scc.values())
        values = sorted(list(count.values()), reverse=True)
        while len(values) < 5:
            values.append(0)
        return values[:5]

    def TopoSort(self, G):
        """
        Topological Sort of a DAG
        G: a graph represented as an adjacency list
        """
        vertices = list(G.keys())
        for v in vertices:
            if v not in self.topo_explored:
                self.DFS_Topo_Iterator(G, v)
        order_ascending = {
            k: v
            for k, v in sorted(self.topo_order.items(),
                               key=lambda item: item[1])
        }
        return order_ascending

    def DFS_Topo(self, G, s):
        """
        Explore the graph using DFS and mark nodes as explored
        and assign a topological ordering value
        """
        self.topo_explored.append(s)
        for v in G[s]:
            if v not in self.topo_explored:
                self.DFS_Topo(G, v)

        self.topo_order[s] = self.current_label
        self.current_label -= 1

    def DFS_Topo_Iterator(self, G, s):
        """
        Implementation of DFS to explore a graph iteratively
        instead of recursively
        """
        stack = [s]
        while len(stack) > 0:
            v = stack.pop()
            if v not in self.topo_explored:
                self.topo_explored.append(v)
                for w in G[v]:
                    stack.append(w)
        self.topo_order[s] = self.current_label
        self.current_label -= 1

    def DFS_SCC_Iterator(self, G, s):
        stack = [s]
        while len(stack) > 0:
            v = stack.pop()
            if v not in self.explored:
                self.explored.append(v)
                self.scc[v] = self.num_scc
                for w in G[v]:
                    stack.append(w)

    def DFS_SCC(self, G, s):
        """
        Evert vertex reachable from s is marked as explored 
        and has an assigned scc-value
        """
        self.explored.append(s)
        self.scc[s] = self.num_scc
        for v in self.graph[s]:
            if v not in self.explored:
                self.DFS_SCC(G, v)

    def get_scc(self):
        """
        Find strongly connected components.
        """
        g_rev = self._reverse_graph(self.graph)
        g_rev_order = self.TopoSort(g_rev)
        for v in g_rev_order.keys():
            if v not in self.explored:
                self.num_scc += 1
                self.DFS_SCC_Iterator(self.graph, v)
        return self._format_scc(self.scc)


if __name__ == "__main__":
    G = {
        1: [2],
        2: [3, 4, 5],
        3: [6],
        4: [5, 7],
        5: [2, 6, 7],
        6: [3, 8],
        7: [8, 10],
        8: [7],
        9: [7],
        10: [9, 11],
        11: [12],
        12: [10]
    }
    kosaraju = Kosaraju(G)
    print(kosaraju.get_scc())
