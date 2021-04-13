from Python.src.tree_helper import *


class BinarySearchTree:
    class Node:
        def __init__(self, value=None):
            self.parent = None
            self.value = value
            self.left = None
            self.right = None

        def print(self, end=''):
            print(self.value, end=end)

    def __init__(self):
        self.root = None

    def inorder_walk(self, root):
        if root is not None:
            self.inorder_walk(root.left)
            root.print(end=' ')
            self.inorder_walk(root.right)

    def print(self, end='\n'):
        self.inorder_walk(self.root)
        print(end=end)

    def search(self, k, search_func: callable = tree_search_iterative):
        return search_func(self.root, k)

    def _insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

    def insert(self, z):
        node = BinarySearchTree.Node(z)
        self._insert(node)

    def minimum(self):
        return tree_minimum(self.root)

    def maximum(self):
        return tree_maximum(self.root)

    def _delete(self, z):
        if z.left is None or z.right is None:
            y = z
        else:
            y = tree_successor(z)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.value = y.value

        return y

    def delete(self, z):
        node = self.search(z)
        if node is not None:
            self._delete(node)


if __name__ == "__main__":
    array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    bst = BinarySearchTree()
    for item in array:
        bst.insert(item)

    bst.print()

    result = bst.search(8)
    if result is not None:
        result.print

    result = bst.search(33)
    if result is None:
        print("Result is None.")

    print("minimum: ", bst.minimum().value)
    print("maximum: ", bst.maximum().value)

    for item in array:
        bst.delete(item)
        bst.print(end='')
        print(' -> ', item)
