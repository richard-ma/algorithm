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

    def __init__(self):
        self.nil = RedBlackTree.Node()
        self.nil.color = RedBlackTree.BLACK  # nil node color is Black

        self.root = self.nil

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
        pass

    def insert(self, z):
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
