from algorithms.dijkstra import dijkstra_heap, dist_graph
import pytest
import glob

all_files = glob.glob("input_random_*.txt")


def get_output(filename):
    with open(filename, "r") as f:
        data = f.readline().strip().split(',')
        output = [int(i) for i in data]
    return output


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    graph = dist_graph(filename)
    output = get_output(filename.replace("input", "output"))
    shortest = dijkstra_heap(graph, 1)
    assert shortest == output