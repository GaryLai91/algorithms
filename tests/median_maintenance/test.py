from order_statistic_tree import OSNode, OSTree
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


def sum_medians(data):
    sum_of_medians = 0
    tree = OSTree()
    for i in data:
        tree.insert(i)

        # If tree size is even
        if tree.root.size % 2 == 0:
            median = tree.root.size // 2
        else:
            median = (tree.root.size + 1) // 2

        median_node = tree.select(tree.root, median)
        sum_of_medians += median_node.key
    return sum_of_medians % 10000


@pytest.mark.parametrize("filename", all_files)
def test_case(filename):
    data = get_input(filename)
    output = get_input(filename.replace("input", "output"))[0]
    shortest = sum_medians(data)
    assert shortest == output