from algorithms.mst_prim import get_input
from algorithms.single_link_clustering import clustering
import pytest
import glob

filename = "input_completeRandom_*.txt"
all_files = glob.glob(filename)


def get_output(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        return int(line)


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    data = get_input(filename)
    output = get_output(filename.replace("input", "output"))
    shortest = clustering(data)
    assert shortest == output


if __name__ == "__main__":
    data = get_input("challenge.txt")
    shortest = clustering(data)
    print(shortest)
