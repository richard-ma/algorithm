import unittest
import random
from Python.src.minheap import *
from Python.src.helper import *
from Python.tests.helper import *


class MinHeapTestCase(MyTestCase):
    @staticmethod
    def check_min_heap(array: list):
        test_array = [0]
        test_array.extend(array)
        for i in range(len(test_array)-1, 1, -1):
            if test_array[i] < test_array[MinHeap.parent(i)]:
                return False

        return True

    def setUp(self):
        self.mySetUp()

    def test_length(self):
        random_array = self.create_random_array()

        mh = MinHeap()
        self.assertEqual(mh.length, 0)
        mh.build(random_array)
        self.assertEqual(mh.length, len(random_array))

        mh = MinHeap(random_array)
        self.assertEqual(mh.length, len(random_array))

    def test_data(self):
        random_array = self.create_random_array()

        mh = MinHeap()
        self.assertEqual(mh.data, list())
        mh.build(random_array)
        self.assertTrue(MinHeapTestCase.check_min_heap(mh.data))

        mh = MinHeap(random_array)
        self.assertTrue(MinHeapTestCase.check_min_heap(mh.data))

    def test_minimum(self):
        random_array = self.create_random_array()

        mh = MinHeap(random_array)
        self.assertEqual(
            mh.minimum,
            min(random_array)
        )

    def test_build(self):
        random_array = self.create_random_array()

        mh = MinHeap()
        mh.build(random_array)
        self.assertEqual(mh.length, len(random_array))
        self.assertTrue(MinHeapTestCase.check_min_heap(mh.data))

    def test_sort(self):
        random_array = self.create_random_array()

        mh = MinHeap(random_array)
        sorted_array = mh.sort()
        self.assertEqual(
            sorted_array,
            list(sorted(random_array, reverse=True))
        )

    def test_extract_minimum(self):
        random_array = self.create_random_array()

        mh = MinHeap(random_array)
        length = mh.length
        min_item = mh.extract_minimum()

        self.assertEqual(min_item, min(random_array))
        self.assertEqual(length-1, mh.length)
        self.assertTrue(MinHeapTestCase.check_min_heap(mh.data))

        mh = MinHeap()
        with self.assertRaises(OverflowError):
            mh.extract_minimum()

    def test_decrease_key(self):
        random_array = self.create_random_array()

        mh = MinHeap(random_array)
        mh.decrease_key(mh.length, self.l_bound)

        self.assertTrue(MinHeapTestCase.check_min_heap(mh.data))

    def test_insert(self):
        random_array = self.create_random_array()

        mh = MinHeap(random_array)
        length = mh.length
        mh.insert(random.randint(self.l_bound, self.u_bound))

        self.assertEqual(length+1, mh.length)
        self.assertTrue(MinHeapTestCase.check_min_heap(mh.data))


if __name__ == '__main__':
    unittest.main()
