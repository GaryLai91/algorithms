import heapq
from collections import namedtuple

Vertex = namedtuple("Vertex", ['dist'])
NEXT_TO_VERTICES = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]


def dist_graph(filename):
    """
    Build graph
    graph = {vertex: namedtuple(Vertex)}
    Example output:
    graph['155'] = Vertex(dist={'191': 36, '151': 33})
    vertex 155 connects to vertex 191, its edge has length 36.
    """
    graph = {}
    with open(filename, 'r') as f:
        row = f.readlines()
        for s in row:
            data = s.strip().split('\t')
            v = int(data[0])
            dist = {}
            for edge in data[1:]:
                w, l = edge.split(',')
                w = int(w)
                l = int(l)
                try:
                    if l < dist[w]:
                        dist[w] = l
                except KeyError:
                    dist[w] = l
            graph[v] = Vertex(dist=dist)
    return graph


def search_vertex(ls, vertex):
    """
    Search for a vertex in the 2nd position of List(int, str)
    and return index.
    """
    for idx in range(len(ls)):
        if ls[idx][1] == vertex:
            return idx


def dijkstra_heap(graph, source_vertex):
    """
    Implementation of Dijkstra's single source shortest path
    using the Heap data structure.
    Reduced time complexity from O(mn), where n is the number of vertices 
    and m is the number of edges; to O((m+n) * logn)

    Inputs:
    graph: An adjacency list 
    source_vertex: A source vertex, an entrypoint of the graph
    edge_lengths: A map that stores the length of each edges. 
    """
    x = set()
    heap = []
    shortest_key = {source_vertex: 0}
    heapq.heappush(heap, (0, source_vertex))

    for v in graph.keys():
        if v != source_vertex:
            shortest_key[v] = float('inf')
            heapq.heappush(heap, (float('inf'), v))

    while heap:
        length_w, w = heapq.heappop(heap)
        x.add(w)
        for y in graph[w].dist.keys():
            idx_to_remove = search_vertex(heap, y)

            #################################################################################
            ### Since the graph given it not strictly directive                     ###
            ### idx_to_remove is None only if it comes from the opposite direction        ###
            ### e.g. 1 -> 8 (already processed), but in future, we have to process 8 -> 1 ###
            #################################################################################
            if idx_to_remove is None:
                continue
            #################################################################################
            # Swap the index to be remove to the last and remove it
            heap[idx_to_remove], heap[-1] = heap[-1], heap[idx_to_remove]
            length_y, y = heap.pop()

            # Calculate the new length (dijkstra score)
            new_length_y = min(length_y, length_w + graph[w].dist[y])
            heapq.heappush(heap, (new_length_y, y))

            # Maintaining the heap invariant
            heapq.heapify(heap)

            # Update shortest_key
            shortest_key[y] = new_length_y

    return [shortest_key[i] for i in NEXT_TO_VERTICES]