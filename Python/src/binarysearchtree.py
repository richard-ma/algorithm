def _search(x, k):
    if x is None or x.value == k:
        return x

    if k < x.value:
        return _search(x.left, k)
    else:
        return _search(x.right, k)


def _search_iterative(x, k):
    while x is not None and x.value != k:
        if k < x.value:
            x = x.left
        else:
            x = x.right
    return x


def _minimum(x):
    while x.left is not None:
        x = x.left
    return x


def _maximum(x):
    while x.right is not None:
        x = x.right
    return x


def _successor(x):
    if x.right is not None:
        return _minimum(x.right)

    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


def _predecessor(x):
    if x.left is not None:
        return _maximum(x.left)

    y = x.parent
    while y is not None and x == y.left:
        x = y
        y = y.parent
    return y


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

    def search(self, k, search_func: callable = _search_iterative):
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
        return _minimum(self.root)

    def maximum(self):
        return _maximum(self.root)

    def _delete(self, z):
        if z.left is None or z.right is None:
            y = z
        else:
            y = _successor(z)

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
