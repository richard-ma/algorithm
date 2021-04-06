import unittest
from Python.src.heap import *
from random import randint
from sys import maxsize
from copy import deepcopy


class MyTestCase(unittest.TestCase):
    INT_MAX = maxsize
    INT_MIN = -maxsize - 1

    def setUp(self) -> None:
        self.data = [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

        self.random_test_times = 100
        self.max = 10000
        self.min = -10000
        self.random_data_length = randint(100, 10000)
        self.random_data = [MyTestCase.INT_MIN]

    def test_heapsort(self):
        sorted_by_sorted = list(sorted(self.data))
        heap_sort(self.data)
        self.assertEqual(
            sorted_by_sorted,
            self.data
        )

    def test_heapsort_with_random_data(self):
        for i in range(0, self.random_test_times):
            # create random data
            random_data = deepcopy(self.random_data)
            for time in range(1, self.random_data_length + 1):
                random_data.append(randint(self.min, self.max))

            sorted_by_sorted = list(sorted(random_data))
            sorted_by_heapsort = deepcopy(random_data)
            heap_sort(sorted_by_heapsort)
            self.assertEqual(
                sorted_by_sorted,
                sorted_by_heapsort
            )


if __name__ == '__main__':
    unittest.main()
