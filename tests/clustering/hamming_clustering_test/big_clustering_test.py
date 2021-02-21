from algorithms.big_clustering import get_bin_input
from algorithms.big_clustering import clustering
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
    n, data = get_bin_input(filename)
    output = get_output(filename.replace("input", "output"))
    shortest = clustering(n, data)
    assert shortest == output


if __name__ == "__main__":
    n, data = get_bin_input("challenge.txt")
    shortest = clustering(n, data)
    print(shortest)
