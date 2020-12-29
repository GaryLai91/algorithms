from two_sum import solve
import pytest
import glob

all_files = glob.glob("input_random_*.txt")


def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
    return data


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    data = get_input(filename)
    output = get_input(filename.replace("input", "output"))[0]
    shortest = solve(data)
    assert shortest == output
