from algorithms.min_cut import simulate_mincut
from unittest import TestCase
import pytest, glob
from collections import defaultdict

all_files = glob.glob("input_*.txt")


def get_data(filename):
    with open(filename, "r") as f:
        graph = defaultdict(list)
        for line in f.read().splitlines():
            # can change delimiter to "\t" for challenge.txt
            arr = [int(i) for i in line.split(" ") if i != ""]
            graph[arr[0]] = arr[1:]
    return graph


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    print(filename)
    output_file = filename.replace("input", "output")
    with open(output_file, "r") as f:
        output = [int(i) for i in f.readlines()][0]
    mincut = simulate_mincut(get_data(filename))
    assert mincut == output


# pypy3 -m pytest -v test.py
