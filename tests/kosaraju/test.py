from algorithms.kosaraju import Kosaraju
from unittest import TestCase
import pytest, glob
from collections import defaultdict
from itertools import chain

import sys
sys.setrecursionlimit(10**6)
all_files = glob.glob("input_mostlyCycles_*.txt")


def clear_global_var():
    for name in dir():
        if not name.startswith('_'):
            print(globals()[name])


def get_data(filename):
    with open(filename, "r") as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            arr = [int(i) for i in line.split(" ") if i != ""]
            graph[arr[0]].append(arr[1])
    vertices = list(set(chain.from_iterable(graph.values())))
    max_node = max(vertices)
    for v in range(1, max_node + 1):
        if v not in graph.keys():
            graph[v] = []
    return graph


def get_output(filename):
    with open(filename, "r") as f:
        output = [int(i) for i in f.readlines()[0].split(",")]
    return output


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    g = get_data(filename)
    kosaraju = Kosaraju(g)
    scc = kosaraju.get_scc()
    output = get_output(filename.replace("input", "output"))
    assert scc == output


if __name__ == "__main__":
    filename = "challenge.txt"
    g = get_data(filename)
    kosaraju = Kosaraju(g)
    scc = kosaraju.get_scc()
    print(scc)