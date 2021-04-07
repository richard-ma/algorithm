import unittest
import random
from Python.src.helper import *
from Python.tests.helper import *
from Python.src.minmax import *


class MinMaxTestCase(MyTestCase):
    def setUp(self):
        self.mySetUp()

    def test_min_max_even_elements(self):
        self.min_array_length, self.max_array_length = 100, 100
        random_array = self.create_random_array()

        min_by_min = min(random_array)
        max_by_max = max(random_array)
        min_by_min_max, max_by_min_max = min_max(random_array)

        self.assertEqual(min_by_min, min_by_min_max)
        self.assertEqual(max_by_max, max_by_min_max)

    def test_min_max_odd_elements(self):
        self.min_array_length, self.max_array_length = 101, 101
        random_array = self.create_random_array()

        min_by_min = min(random_array)
        max_by_max = max(random_array)
        min_by_min_max, max_by_min_max = min_max(random_array)

        self.assertEqual(min_by_min, min_by_min_max)
        self.assertEqual(max_by_max, max_by_min_max)


if __name__ == '__main__':
    unittest.main()
