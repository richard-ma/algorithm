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

    def link(self, z: Node):
        self.parent = z
        self.sibling = z.child
        z.child = self
        z.degree += 1


class BinomialHeap:
    def __init__(self):
        self.head = None

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

    def union(self, h2: BinomialHeap):
        pass


if __name__ == "__main__":
    bh = BinomialHeap()
