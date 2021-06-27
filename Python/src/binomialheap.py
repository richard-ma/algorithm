from __future__ import annotations  # 必须放在第一行，为了让Node类的link方法调用Node类型的参数
from Python.src.entity import Entity


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


if __name__ == "__main__":
    bh = BinomialHeap()
