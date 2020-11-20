from algorithms.quicksort import Quicksort
from unittest import TestCase


def get_data(fname):
    data = []
    with open(fname, "r") as f:
        for line in f.readlines():
            data.append(int(line))
    return data


class Test(TestCase):
    def test_1_first(self):
        data = get_data("test1.txt")
        count = Quicksort(data, 0, len(data) - 1, "first")
        assert count == 25

    def test_1_last(self):
        data = get_data("test1.txt")
        count = Quicksort(data, 0, len(data) - 1, "last")
        assert count == 31

    def test_1_median(self):
        data = get_data("test1.txt")
        count = Quicksort(data, 0, len(data) - 1, "median")
        assert count == 21

    def test_2_first(self):
        data = get_data("test2.txt")
        count = Quicksort(data, 0, len(data) - 1, "first")
        assert count == 620

    def test_2_last(self):
        data = get_data("test2.txt")
        count = Quicksort(data, 0, len(data) - 1, "last")
        assert count == 573

    def test_2_median(self):
        data = get_data("test2.txt")
        count = Quicksort(data, 0, len(data) - 1, "median")
        assert count == 502

    def test_challenge_first(self):
        data = get_data("challenge.txt")
        count = Quicksort(data, 0, len(data) - 1, "first")
        assert count == 162085

    def test_challenge_last(self):
        data = get_data("challenge.txt")
        count = Quicksort(data, 0, len(data) - 1, "last")
        assert count == 164123

    def test_challenge_median(self):
        data = get_data("challenge.txt")
        count = Quicksort(data, 0, len(data) - 1, "median")
        assert count == 138382
