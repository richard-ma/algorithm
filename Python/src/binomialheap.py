from __future__ import annotations  # 必须放在第一行，为了让Node类的link方法调用Node类型的参数
from copy import deepcopy
from Python.src.entity import Entity
from Python.src.helper import INT_MAX, INT_MIN


class Node:
    def __init__(self, entity: Entity):
        self.parent = None
        self.entity = entity
        self.degree = 0
        self.child = None
        self.sibling = None

    # 将现有节点作为z的子节点
    def link(self, z: Node):
        self.parent = z
        self.sibling = z.child
        z.child = self
        z.degree += 1

    @staticmethod
    def print_node(node: Node, level: int):
        print(" " * (level * 4), end='')
        print("[", node.degree, node.entity.key, node.entity.value, "]", sep=':')

    @staticmethod
    def print(node: Node, level: int = None):
        if node.parent is None:
            level = 0
        Node.print_node(node, level)
        if node.child is not None:
            Node.print(node.child, level+1)
        if node.sibling is not None:
            Node.print(node.sibling, level)

    @staticmethod
    def print_sibling(node: Node):
        Node.print_node(node, 0)
        if node.sibling is not None:
            Node.print_sibling(node.sibling)


class BinomialHeap:
    def __init__(self):
        self.head = None

    def print(self):
        Node.print(self.head)

    def print_root_list(self):
        print('*' * 20, 'root list start', '*' * 20)
        Node.print_sibling(self.head)
        print('*' * 20, 'root list end', '*' * 20)

    def minimum(self):
        y = None
        x = self.head
        m = INT_MAX
        while x is not None:
            if x.entity.key < m:
                m = x.entity.key
                y = x
            x = x.sibling
        return y

    def merge(self, other: BinomialHeap):
        origin = self

        if other.head is None:
            return

        if origin.head is None:
            origin.head = deepcopy(other.head)  # TODO: test delete h after merged h
            return

        origin_ptr = origin.head
        other_ptr = other.head

        current_ptr = None
        while origin_ptr is not None and other_ptr is not None:
            if origin_ptr.entity.key <= other_ptr.entity.key:
                current_node = origin_ptr
                origin_ptr = origin_ptr.sibling
            else:
                current_node = other_ptr
                other_ptr = other_ptr.sibling

            if current_ptr is None:  # add first node
                current_ptr = current_node
                origin.head = current_node
            else:
                current_ptr.sibling = current_node
                current_ptr = current_ptr.sibling

        # add the tail of origin_ptr or other_ptr
        if origin_ptr is not None:
            current_ptr.sibling = origin_ptr
        if other_ptr is not None:
            current_ptr.sibling = other_ptr

    def union(self, other: BinomialHeap):
        self.merge(other)
        self.print_root_list()

        if self.head is None:
            return

        prev_x = None
        x = self.head
        next_x = self.head.sibling

        while next_x is not None:
            if x.degree != next_x.degree or \
                    (next_x.sibling is not None and next_x.sibling.degree == x.degree):
                prev_x = x
                x = next_x
            elif x.entity.key <= next_x.entity.key:
                x.sibling = next_x.sibling
                next_x.link(x)
            else:
                if prev_x is None:
                    self.head = next_x
                else:
                    prev_x.sibling = next_x
                x.link(next_x)
                x = next_x
            next_x = next_x.sibling

    def insert(self, x: Node):
        other = BinomialHeap()
        x.parent = None
        x.child = None
        x.sibling = None
        x.degree = 0
        other.head = x
        self.union(other)


if __name__ == "__main__":
    array = [7, 27, 29, 5, 9, 18, 40]
    bh = BinomialHeap()
    for num in array:
        bh.insert(Node(Entity(num)))

    print('*' * 80)
    bh.print()
