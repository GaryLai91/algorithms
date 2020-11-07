from algorithms.karatsuba import karat
from unittest import TestCase


def get_data():
    data = []
    with open("./data.txt", 'r') as f:
        for line in f.readlines():
            data.append(int(line))
    return data

class Test(TestCase):
    def test_count_inv_1(self):
        a = 99_999
        b = 99_999
        assert karat(a,b) == a * b

    def test_count_inv_2(self):
        a = 3141592653589793238462643383279502884197169399375105820974944592 
        b = 2718281828459045235360287471352662497757247093699959574966967627
        assert karat(a,b) == a * b


#pytest -v test.py