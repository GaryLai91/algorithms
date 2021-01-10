from algorithms.huffman_codes import huffman, bfs_label
import pytest
import glob

all_files = glob.glob("input_random_*.txt")


def get_input(filename):
    output = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
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


if __name__ == "__main__":
    data = get_input("input_random_9_40.txt")
    output_min, output_max = get_output("input_random_9_40.txt".replace(
        "input", "output"))
    root = huffman(data)
    output, _min, _max = bfs_label(root)
    print(f"Output: {output}\nMin: {min(output)}\nMax: {max(output)}")
    print(_min, _max)