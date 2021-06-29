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

    @staticmethod
    def _create_root_list(a: list) -> Node:
        head = None
        current = head
        for n in a:
            node = Node(Entity(n))
            if current is None:
                current = node
                head = current
            else:
                current.sibling = node
                current = current.sibling
        current.sibling = None

        return head

    @staticmethod
    def print_root_list(head):
        current = head
        while current is not None:
            print(current.entity.key, end=' -> ')
            current = current.sibling
        print(current)

    def test_binomialheap_merge(self):
        a1 = [7, 27, 29]
        a2 = [5, 9, 18, 40]

        print("origin & other are None")
        origin = BinomialHeap()
        other = BinomialHeap()
        origin.merge(other)
        BinomialHeapNodeTestCase.print_root_list(origin.head)

        print("other is None")
        origin = BinomialHeap()
        other = BinomialHeap()
        origin.head = BinomialHeapNodeTestCase._create_root_list(a1)
        origin.merge(other)
        BinomialHeapNodeTestCase.print_root_list(origin.head)

        print("origin is None")
        origin = BinomialHeap()
        other = BinomialHeap()
        other.head = BinomialHeapNodeTestCase._create_root_list(a2)
        origin.merge(other)
        BinomialHeapNodeTestCase.print_root_list(origin.head)

        print("origin & other are not None")
        origin = BinomialHeap()
        other = BinomialHeap()
        origin.head = BinomialHeapNodeTestCase._create_root_list(a1)
        other.head = BinomialHeapNodeTestCase._create_root_list(a2)
        origin.merge(other)
        BinomialHeapNodeTestCase.print_root_list(origin.head)


if __name__ == '__main__':
    unittest.main()
