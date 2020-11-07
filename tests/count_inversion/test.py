from algorithms.count_inversion import count_inv
from unittest import TestCase


def get_data():
    data = []
    with open("./data.txt", 'r') as f:
        for line in f.readlines():
            data.append(int(line))
    return data

class Test(TestCase):
    def test_count_inv_1(self):
        data = get_data()
        ls, count = count_inv(data)
        assert count == 2407905288

    def test_count_inv_2(self):
        data = [8, 7, 6, 5, 4, 3, 2, 1]
        ls, count = count_inv(data)
        assert count == 28


#pytest -v test.py