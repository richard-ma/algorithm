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

    def test_heapqueue(self):
        max_item_by_max = max(self.data)
        build_max_heap(self.data, len(self.data)-1)
        max_item_by_heap_extract_max = heap_extract_max(self.data)
        self.assertEqual(
            max_item_by_max,
            max_item_by_heap_extract_max
        )

    def test_heapqueue_with_random_data(self):
        for i in range(0, self.random_test_times):
            # create random data
            random_data = deepcopy(self.random_data)
            for time in range(1, self.random_data_length + 1):
                random_data.append(randint(self.min, self.max))

            max_item_by_max = max(random_data)
            build_max_heap(random_data, len(random_data)-1)
            max_item_by_heap_extract_max = heap_extract_max(random_data)
            self.assertEqual(
                max_item_by_max,
                max_item_by_heap_extract_max
            )


if __name__ == '__main__':
    unittest.main()
