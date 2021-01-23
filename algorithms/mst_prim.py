import heapq
from collections import defaultdict
import random


def get_input(filename):
    output = defaultdict(list)
    with open(filename, "r") as f:
        _ = f.readline()
        lines = f.readlines()
        for line in lines:
            data = [int(i) for i in line.strip().split(" ")]
            u, v, w = data
            output[u].append((v, w))
            output[v].append((u, w))
    return output


def calc_cost(nodes_map):
    cost = 0
    for i in nodes_map:
        cost += i[2]
    return cost


def simple_mst_prim(graph):
    vertices = list(graph.keys())
    s = random.choice(vertices)
    x = {s}
    t = []
    while True:
        edges = []
        for u in x:
            for v, w in graph[u]:
                if v not in x:
                    edges.append((v, w))
        if len(edges) == 0:
            break
        min_edge = min(edges, key=lambda z: z[1])
        x.add(min_edge[1])
        t.append(min_edge)
    return calc_cost(t)


def min_cost(graph) -> int:
    visited, cost = set(), 0
    minHeap = [(0, 1)]
    while minHeap:
        minCost, city = heapq.heappop(minHeap)
        if city not in visited:
            cost += minCost
            visited.add(city)
            for nxt, c in graph[city]:
                if nxt not in visited:
                    heapq.heappush(minHeap, (c, nxt))
    return cost
