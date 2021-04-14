from Python.src.tree_helper import *


class RedBlackTree:
    # 0 represents black, 1 represents red
    BLACK = 0
    RED = 1

    class Node:
        def __init__(self, value=None, default_ptr=None):
            self.parent = default_ptr
            self.value = value
            self.left = default_ptr
            self.right = default_ptr
            self.color = RedBlackTree.BLACK

        def print(self, end=''):
            print(self.value, ':', RedBlackTree._color_str(self.color), ':', self.left.value, ':', self.right.value, end=end, sep='')

    @staticmethod
    def _color_str(color_code):
        return 'R' if color_code == RedBlackTree.RED else 'B'

    def __init__(self):
        self.nil = RedBlackTree.Node()
        self.nil.parent = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.color = RedBlackTree.BLACK  # nil node color is Black

        self.root = self.nil

    def inorder_walk(self, root):
        if root != self.nil:
            self.inorder_walk(root.left)
            root.print(end=' ')
            self.inorder_walk(root.right)

    def print(self, end='\n'):
        self.inorder_walk(self.root)
        print(end=end)

    def search(self, k, search_func: callable = tree_search_iterative):
        return search_func(self.root, k, none=self.nil)

    def left_rotate(self, x):
        y = x.right

        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left

        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def _insert_fixup(self, z):
        while z.parent.color == RedBlackTree.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RedBlackTree.RED:
                    z.parent.color = RedBlackTree.BLACK
                    y.color = RedBlackTree.BLACK
                    z.parent.parent.color = RedBlackTree.RED
                    z = z.parent.parent
                elif z == z.parent.right: # y.color == RedBlackTree.BLACK
                    z = z.parent
                    self.left_rotate(z)
                else:
                    z.parent.color = RedBlackTree.BLACK
                    z.parent.parent.color = RedBlackTree.RED
                    self.right_rotate(z.parent.parent)
            else: # z.parent == z.parent.parent.right
                y = z.parent.parent.left
                if y.color == RedBlackTree.RED:
                    z.parent.color = RedBlackTree.BLACK
                    y.color = RedBlackTree.BLACK
                    z.parent.parent.color = RedBlackTree.RED
                    z = z.parent.parent
                elif z == z.parent.left: # y.color == RedBlackTree.BLACK
                    z = z.parent
                    self.right_rotate(z)
                else:
                    z.parent.color = RedBlackTree.BLACK
                    z.parent.parent.color = RedBlackTree.RED
                    self.left_rotate(z.parent.parent)

        self.root.color = RedBlackTree.BLACK

    def insert(self, z):
        node = RedBlackTree.Node(z, default_ptr=self.nil)
        self._insert(node)

    def _insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.color = RedBlackTree.RED

        self._insert_fixup(z)

    def _delete_fixup(self, x):
        while x != self.root and x.color == RedBlackTree.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RedBlackTree.RED:
                    w.color = RedBlackTree.BLACK
                    x.parent.color = RedBlackTree.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == RedBlackTree.BLACK and w.right.color == RedBlackTree.BLACK:
                    w.color = RedBlackTree.RED
                    x = x.parent
                elif w.right.color == RedBlackTree.BLACK:
                    w.left.color = RedBlackTree.BLACK
                    w.color = RedBlackTree.RED
                    self.right_rotate(w)
                    w = x.parent.right
                else:
                    w.color = x.parent.color
                    x.parent.color = RedBlackTree.BLACK
                    w.right.color = RedBlackTree.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                print(w.value)
                if w.color == RedBlackTree.RED:
                    w.color = RedBlackTree.BLACK
                    x.parent.color = RedBlackTree.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == RedBlackTree.BLACK and w.left.color == RedBlackTree.BLACK:
                    w.color = RedBlackTree.RED
                    x = x.parent
                elif w.left.color == RedBlackTree.BLACK:
                    w.right.color = RedBlackTree.BLACK
                    w.color = RedBlackTree.RED
                    self.right_rotate(w)
                    w = x.parent.left
                else:
                    w.color = x.parent.color
                    x.parent.color = RedBlackTree.BLACK
                    w.left.color = RedBlackTree.BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = RedBlackTree.BLACK

    def delete(self, z):
        if z.left == self.nil or z.right == self.nil:
            y = z
        else:
            y = tree_successor(z, none=self.nil)

        if y.left != self.nil:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.value, y.value = y.value, z.value
            z.color, y.color = y.color, z.color

        if y.color == RedBlackTree.BLACK:
            self._delete_fixup(x)

        return y


if __name__ == "__main__":
    array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    # start insert
    print("** Start Insert **")
    rbt = RedBlackTree()
    for item in array:
        print("** Insert %d... **" % item)
        rbt.insert(item)
        rbt.print()

    print("** Start Delete **")
    for item in array:
        print("** Delete %d... **" % item)
        node = rbt.search(item)
        if node != rbt.nil:
            delnode = rbt.delete(node)
            rbt.print(end='')
            print(' -> ', end='')
            delnode.print()
            print()
