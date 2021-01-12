from algorithms.huffman_codes import huffman, bfs_label
import pytest
import glob

all_files = glob.glob("input_random_*.txt")


def get_input(filename):
    output = []
    with open(filename, "r") as f:
        n = int(f.readline())
        #lines = f.readlines()
        for i in range(n):
            line = f.readline()
            d = int(line)
            output.append(d)
    return output


def get_output(filename):
    output = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            d = int(line)
            output.append(d)
    return min(output), max(output)


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    data = get_input(filename)
    output_min, output_max = get_output(filename.replace("input", "output"))
    root = huffman(data)
    output, _min, _max = bfs_label(root)
    assert _min == output_min and _max == output_max