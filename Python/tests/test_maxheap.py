import unittest
import random
from Python.src.maxheap import *
from Python.src.helper import *
from Python.tests.helper import *


class MaxHeapTestCase(MyTestCase):
    @staticmethod
    def check_max_heap(array: list):
        test_array = [0]
        test_array.extend(array)
        for i in range(len(test_array)-1, 1, -1):
            if test_array[i] > test_array[MaxHeap.parent(i)]:
                return False

        return True

    def setUp(self):
        self.mySetUp()

    def test_length(self):
        random_array = self.create_random_array()

        mh = MaxHeap()
        self.assertEqual(mh.length, 0)
        mh.build(random_array)
        self.assertEqual(mh.length, len(random_array))

        mh = MaxHeap(random_array)
        self.assertEqual(mh.length, len(random_array))

    def test_data(self):
        random_array = self.create_random_array()

        mh = MaxHeap()
        self.assertEqual(mh.data, list())
        mh.build(random_array)
        self.assertTrue(MaxHeapTestCase.check_max_heap(mh.data))

        mh = MaxHeap(random_array)
        self.assertTrue(MaxHeapTestCase.check_max_heap(mh.data))

    def test_maximum(self):
        random_array = self.create_random_array()

        mh = MaxHeap(random_array)
        self.assertEqual(
            mh.maximum,
            max(random_array)
        )

    def test_build(self):
        random_array = self.create_random_array()

        mh = MaxHeap()
        mh.build(random_array)
        self.assertEqual(mh.length, len(random_array))
        self.assertTrue(MaxHeapTestCase.check_max_heap(mh.data))

    def test_sort(self):
        random_array = self.create_random_array()

        mh = MaxHeap(random_array)
        sorted_array = mh.sort()
        self.assertEqual(
            sorted_array,
            list(sorted(random_array))
        )

    def test_extract_maximum(self):
        random_array = self.create_random_array()

        mh = MaxHeap(random_array)
        length = mh.length
        max_item = mh.extract_maximum()

        self.assertEqual(max_item, max(random_array))
        self.assertEqual(length-1, mh.length)
        self.assertTrue(MaxHeapTestCase.check_max_heap(mh.data))

        mh = MaxHeap()
        with self.assertRaises(OverflowError):
            mh.extract_maximum()

    def test_increase_key(self):
        random_array = self.create_random_array()

        mh = MaxHeap(random_array)
        mh.increase_key(mh.length, self.u_bound)

        self.assertTrue(MaxHeapTestCase.check_max_heap(mh.data))

    def test_insert(self):
        random_array = self.create_random_array()

        mh = MaxHeap(random_array)
        length = mh.length
        mh.insert(random.randint(self.l_bound, self.u_bound))

        self.assertEqual(length+1, mh.length)
        self.assertTrue(MaxHeapTestCase.check_max_heap(mh.data))


if __name__ == '__main__':
    unittest.main()
