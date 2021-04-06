import unittest
from Python.src.sort_heap import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    def test_heapsort(self):
        sorted_by_sorted = list(sorted(self.data))
        heap_sort(self.data)
        self.assertEqual(
            sorted_by_sorted,
            self.data
        )


if __name__ == '__main__':
    unittest.main()
