from algorithms.single_link_clustering import get_bin_input
from algorithms.single_link_clustering import hamming_clustering2
from algorithms.single_link_clustering import create_hamming_graph2
import pytest
import glob

filename = "input_random_*.txt"
all_files = glob.glob(filename)


def get_output(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        return int(line)


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    data = get_bin_input(filename)
    output = get_output(filename.replace("input", "output"))
    shortest = hamming_clustering2(data)
    assert shortest == output


if __name__ == "__main__":
    data = get_bin_input("challenge.txt")
    shortest = hamming_clustering2(data)
    print(shortest)
