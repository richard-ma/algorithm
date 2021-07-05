from __future__ import annotations
from Python.src.entity import Entity


class Node:
    def __init__(self, entity: Entity):
        self.parent = self
        self.rank = 0
        self.entity = entity

    def link(self, other: Node):
        if self.rank > other.rank:
            other.parent = self
        else:
            self.parent = other
            if self.rank == other.rank:
                other.rank += 1


class DisjointSet:
    def __init__(self, keys: list):
        self.nodes = list()

        for key in keys:
            self.nodes.append(Node(Entity(key)))

    def find(self, key):
        for node in self.nodes:
            if key == node.entity.key:
                return node
        return None

    @staticmethod
    def findset(x: Node):
        if x != x.parent:
            x.parent = DisjointSet.findset(x.parent)
        return x.parent

    @staticmethod
    def union(x: Node, y: Node):
        DisjointSet.findset(x).link(DisjointSet.findset(y))


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    ds = DisjointSet(array)
    ds.find(1).parent = ds.find(2)
    ds.find(4).parent = ds.find(3)
    ds.find(5).parent = ds.find(3)

    print(DisjointSet.findset(ds.find(1)).entity.key)
    DisjointSet.union(ds.find(3), ds.find(1))
    print(ds.find(4).parent.entity.key)
    print(ds.findset(ds.find(4)).parent.entity.key)
    print(ds.find(4).parent.entity.key)
