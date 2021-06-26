from Python.src.helper import *
from Python.src.entity import Entity


class Node:
    def __init__(self):
        self.parent = None
        self.entitys = list()
        self.childs = list()

    def find(self, key):
        for e in self.entitys:
            if e.key == key:
                return e

    def delete(self, key):
        for pos, e in enumerate(self.entitys):
            if e.key == key:
                del self.entitys[pos]
                return pos, e

    def isLeaf(self):
        return len(self.childs) == 0

    def addEntity(self, entity):
        self.entitys.append(entity)
        self.entitys.sort(key=lambda x: x.key)

    def addChild(self, n):
        self.childs.append(n)
        n.parent = self
        self.childs.sort(key=lambda x: x.entitys[0].key)


class BTree:
    def __init__(self, size=6):
        self.size = size
        self.root = None
        self.length = 0

    def add(self, key, value=None):
        self.length += 1

        if self.root:
            current = self.root
            while not current.isLeaf():
                for pos, e in enumerate(current.entitys):
                    if e.key > key:
                        current = current.childs[pos]
                        break
                    elif e.key == key:
                        e.value = value
                        self.length -= 1
                        return
                else:
                    current = current.childs[-1]

            current.addEntity(Entity(key, value))

            if len(current.entitys) > self.size:
                self.__split(current)
        else:
            self.root = Node()
            self.root.addEntity(Entity(key, value))

    def get(self, key):
        n = self.__findNode(key)
        if n:
            return n.find(key).value

    def delete(self, key):
        node = self.__findNode(key)

        if node:
            pos_i, e = node.delete(key)

            if not node.isLeaf():
                child = node.childs[pos_i]
                pos_j, entity = child.delete(child.entitys[-1].key)
                node.addEntity(entity)

                while not child.isLeaf():
                    node = child
                    child = child.childs[pos_j]
                    pos_j, entity = child.delete(child.entitys[-1].key)
                    node.addEntity(entity)

            self.length -= 1
            return e.value

    def isEmpty(self):
        return self.length == 0

    def __findNode(self, key):
        if self.root:
            current = self.root

            while not current.isLeaf():
                for i, e in enumerate(current.entitys):
                    if e.key > key:
                        current = current.childs[i]
                        break
                    elif e.key == key:
                        return current
                else:
                    current = current.childs[-1]

            if current.find(key):
                return current

    def __split(self, node):
        middle = len(node.entitys) // 2
        top = node.entitys[middle]
        right = Node()

        for e in node.entitys[middle+1:]:
            right.addEntity(e)
        for n in node.childs[middle+1:]:
            right.addChild(n)

        node.entitys = node.entitys[:middle]
        node.childs = node.childs[:middle+1]

        parent = node.parent

        if parent:
            parent.addEntity(top)
            parent.addChild(right)

            if len(parent.entitys) > self.size:
                self.__split(parent)
        else:
            self.root = Node()
            self.root.addEntity(top)
            self.root.addChild(node)
            self.root.addChild(right)


if __name__ == "__main__":
    t = BTree(4)
    t.add(20)
    t.add(40)
    t.add(60)
    t.add(70, 'c')
    t.add(80)
    t.add(10)
    t.add(30)
    t.add(15, 'python')
    t.add(75, 'java')
    t.add(85)
    t.add(90)
    t.add(25)
    t.add(35, 'c#')
    t.add(50)
    t.add(22, 'c++')
    t.add(27)
    t.add(32)

    print(t.get(15))
    print(t.get(75))
    print(t.delete(35))
    print(t.delete(22))
    t.add(22, 'lua')
    print(t.get(22))
    print(t.length)

    array = [2, 3, 5, 7, 11, 13, 15, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    bt = BTree(size=3)

    print('*' * 80)
    for item in array:
        bt.add(item)
        print('**', item, '**')
    print('*' * 80)
