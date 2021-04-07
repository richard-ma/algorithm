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

    def test_min_max_with_empty_array(self):
        empty_array = list()
        min_by_min_max, max_by_min_max = min_max(empty_array)

        self.assertIsNone(min_by_min_max)
        self.assertIsNone(max_by_min_max)

    def test_min_max_with_one_item_array(self):
        one_item_array = [random.randint(self.l_bound, self.u_bound)]
        min_by_min_max, max_by_min_max = min_max(one_item_array)

        self.assertEqual(one_item_array[0], min_by_min_max)
        self.assertEqual(one_item_array[0], max_by_min_max)


if __name__ == '__main__':
    unittest.main()
