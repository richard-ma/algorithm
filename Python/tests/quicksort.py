import unittest
import random
from Python.src.helper import *
from Python.tests.helper import *
from Python.src.quicksort import *


class QuickSortTestCase(MyTestCase):
    def setUp(self):
        self.mySetUp()

    def test_quick_sort(self):
        random_array = self.create_random_array()
        sort_by_sorted = list(sorted(random_array))
        quick_sort(random_array, 0, len(random_array)-1)

        self.assertEqual(
            sort_by_sorted,
            random_array
        )

    def test_quick_sort_with_random_partition(self):
        random_array = self.create_random_array()
        sort_by_sorted = list(sorted(random_array))
        quick_sort(random_array, 0, len(random_array)-1, partition_func=random_partition)

        self.assertEqual(
            sort_by_sorted,
            random_array
        )

    def test_quick_sort_2(self):
        random_array = self.create_random_array()
        sort_by_sorted = list(sorted(random_array))
        quick_sort_2(random_array, 0, len(random_array)-1)

        self.assertEqual(
            sort_by_sorted,
            random_array
        )

    def test_quick_sort_2_with_random_partition(self):
        random_array = self.create_random_array()
        sort_by_sorted = list(sorted(random_array))
        quick_sort_2(random_array, 0, len(random_array)-1, partition_func=random_partition)

        self.assertEqual(
            sort_by_sorted,
            random_array
        )


if __name__ == '__main__':
    unittest.main()
