from algorithms.knapsack import get_input, recursion, branch

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
    items, capacity = get_input(filename)
    output = get_output(filename.replace("input", "output"))
    value, taken = branch(items, capacity)
    assert value == output


if __name__ == "__main__":
    items, capacity = get_input("big_challenge.txt")
    value, taken = branch(items, capacity)
    print(value)
