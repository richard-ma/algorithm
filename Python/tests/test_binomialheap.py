import unittest
from Python.src.binomialheap import *


class BinomialHeapNodeTestCase(unittest.TestCase):
    def test_binomialheap_node(self):
        y = Node(Entity(2, "two"))
        z = Node(Entity(3, "three"))
        z_orig_child = z.child
        y.link(z)

        self.assertEqual(y.parent, z)
        self.assertEqual(z.child, y)
        self.assertEqual(y.sibling, z_orig_child)
        self.assertEqual(z.degree, y.degree+1)


if __name__ == '__main__':
    unittest.main()
