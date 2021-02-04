from algorithms.mst_prim import get_input
from algorithms.kruskal import kruskal_mst, kruskal_uf
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
    data = get_input(filename)
    output = get_output(filename.replace("input", "output"))
    shortest = kruskal_uf(data)
    assert shortest == output


if __name__ == "__main__":
    data = get_input("challenge.txt")
    shortest = kruskal_mst(data)
    print(shortest)
