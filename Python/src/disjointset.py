from __future__ import annotations
from Python.src.entity import Entity


class Node:
    def __init__(self, entity: Entity):
        self.parent = self
        self.entity = entity
        self.next = None


class DisjointSet:
    def __init__(self):
        self.head = None

if __name__ = '__main__':
    array = []
