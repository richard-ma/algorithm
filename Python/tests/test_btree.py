import unittest
import random
from Python.src.helper import *
from Python.tests.helper import *
from Python.src.btree import *
from copy import deepcopy


class BTreeTestCase(MyTestCase):
    def setUp(self):
        self.array = [2, 3, 5, 7, 11, 13, 15, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def tearDown(self):
        pass

    def _build_tree(self):
        bt = BTree(t=3)
        for item in self.array:
            bt.insert(item)

        return bt

    def test_minimum(self):
        bt = self._build_tree()
        node, idx = bt.minimum()
        self.assertEqual(node.keys[idx], self.array[0])

    def test_maximum(self):
        bt = self._build_tree()
        node, idx = bt.maximum()
        self.assertEqual(node.keys[idx], self.array[-1])

    def test_predecessor(self):
        bt = self._build_tree()
        self.assertEqual(bt.predecessor(*bt.search(2)), (None, None))

        for i in range(1, len(self.array)):
            node, idx = bt.predecessor(*bt.search(self.array[i]))
            self.assertEqual(self.array[i-1], node.keys[idx])

    def test_successor(self):
        bt = self._build_tree()
        self.assertIsNone(bt.successor(*bt.search(97)))

    def test_search(self):
        bt = self._build_tree()
        last_item = self.array[-1]
        node, idx = bt.search(last_item)
        self.assertIsNotNone(node)
        self.assertIsNotNone(idx)
        self.assertEqual(node.keys[idx], last_item)

        not_in_array_item = 100
        node, idx = bt.search(not_in_array_item)
        self.assertIsNone(node)
        self.assertIsNone(idx)

    def test_insert(self):
        array = deepcopy(self.array)
        test_times = 10000
        for i in range(0, test_times):
            # random shuffle array
            random.shuffle(array)

            bt = BTree(t=3)
            for item in array:
                bt.insert(item)

            last_item = array[-1]
            node, idx = bt.search(last_item)
            self.assertIsNotNone(node)
            self.assertIsNotNone(idx)
            self.assertEqual(node.keys[idx], last_item)


if __name__ == '__main__':
    unittest.main()
