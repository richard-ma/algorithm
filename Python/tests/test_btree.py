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
        bt = BTree(size=3)
        for item in self.array:
            bt.add(item)
        return bt


if __name__ == '__main__':
    unittest.main()
