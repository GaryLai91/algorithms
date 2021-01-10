import heapq
from queue import Queue
from string import ascii_lowercase
from typing import List


class Node:
    def __init__(self, weight, name=""):
        self.weight = weight
        self.name = name
        self.left = None
        self.right = None
        self.visited = False
        self.level = 99999999

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.name == other.name


def huffman(C: List):
    """
    Args: Dict[k=weight, v=frequency]
    Return: root of the prefix tree
    """
    index = 0
    n = len(C)
    heap = []
    for i in range(n):
        heapq.heappush(heap, Node(weight=C[i], name=index))
        index += 1
    for i in range(n - 1):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        z_weight = x.weight + y.weight
        z = Node(weight=z_weight)
        z.left = x
        z.right = y
        heapq.heappush(heap, z)
    print(len(heap))
    return heapq.heappop(heap)


def bfs_label(root):
    """
    Args:
        G: Root node of a graph built by the subroutine huffman
    Returns:
        A List of levels of the values to encode
    """
    _min = 99999999999999999
    _max = 0
    output = []
    root.level = 0
    q = Queue()
    q.put(root)
    while not q.empty():
        v = q.get()
        adjacent_nodes = [v.left, v.right]
        for w in adjacent_nodes:
            if w is not None and w.visited == False:
                w.visited = True
                w.level = v.level + 1
                q.put(w)
                if w.name:
                    output.append(w.level)
                    if w.level < _min:
                        _min = w.level
                    if w.level > _max:
                        _max = w.level
    return output, _min, _max


if __name__ == "__main__":
    ls = [37, 59, 43, 27, 30, 96, 96, 71, 8, 76]
    root = huffman(ls)
    output, _min, _max = bfs_label(root)
    print(f"Min: {_min}, Max: {_max}")
