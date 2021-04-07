import unittest
import random
from Python.src.helper import *
from Python.tests.helper import *
from Python.src.countingsort import *


class CountingSortTestCase(MyTestCase):
    def setUp(self):
        self.mySetUp()
        self.l_bound = 0

    def test_counting_sort(self):
        random_array = self.create_random_array()
        sort_by_sorted = list(sorted(random_array))
        sort_by_counting_sort = [0] * len(random_array)
        counting_sort(random_array, sort_by_counting_sort, max(random_array))

        self.assertEqual(
            sort_by_sorted,
            sort_by_counting_sort
        )


if __name__ == '__main__':
    unittest.main()
