from Python.src.helper import *


class BTree:
    class Node:
        def __init__(self, t):
            self.leaf = True
            self.n = 0
            self.parent = None
            self.keys = [INT_MIN] * (2 * t - 1)
            self.childs = [None] * (2 * t)

    def __init__(self, t=2, none=None):
        self.t = t
        self.none = none
        self.root = self.none

        self._create()

    def _print(self, root):
        print('[', root.n, ']', sep='', end=' ')
        for i in range(0, root.n):
            print(root.keys[i], end=' ')
        print()
        for item in root.childs:
            if item is not None:
                self._print(item)

    def print(self):
        self._print(self.root)

    def _create(self):
        x = BTree.Node(self.t)
        x.leaf = True
        x.n = 0
        self.root = x

    def _split_child(self, x, i, y):
        z = BTree.Node(self.t)
        z.leaf = y.leaf
        z.parent = y.parent
        z.n = self.t - 1
        for j in range(0, self.t-1):
            z.keys[j] = y.keys[j+self.t]

        if not y.leaf:
            for j in range(0, self.t):
                z.childs[j] = y.childs[j+self.t]
        y.n = self.t - 1

        for j in range(x.n, i, -1):
            x.childs[j+1] = x.childs[j]
        x.childs[i+1] = z

        for j in range(x.n-1, i-1, -1):
            x.keys[j+1] = x.keys[j]
        x.keys[i] = y.keys[self.t-1]
        x.n += 1

    def _insert_nonfull(self, x, k):
        i = x.n
        if x.leaf:
            while i > 0 and k < x.keys[i-1]:
                x.keys[i] = x.keys[i-1]
                i -= 1
            x.keys[i] = k
            x.n += 1
        else:
            while i > 0 and k < x.keys[i-1]:
                i -= 1
            if x.childs[i].n == self.t * 2 - 1:
                self._split_child(x, i, x.childs[i])

                if k > x.keys[i]:
                    i += 1

            self._insert_nonfull(x.childs[i], k)

    def insert(self, k):
        r = self.root
        if r.n == self.t * 2 - 1:
            s = BTree.Node(self.t)
            self.root = s
            s.leaf = False
            s.n = 0
            s.childs[0] = r
            r.parent = s
            self._split_child(s, 0, r)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _search(self, x, k):
        i = 0
        while i < x.n and k > x.keys[i]:
            i += 1
        if i < x.n and k == x.keys[i]:
            return x, i
        if x.leaf:
            return None, None
        else:
            return self._search(x.childs[i], k)

    def search(self, k):
        return self._search(self.root, k)

    def _minimum(self, x):
        while x.n > 0 and x.childs[0] is not None:
            x = x.childs[0]
        return x, 0

    def minimum(self):
        return self._minimum(self.root)

    def _maximum(self, x):
        while x.n > 0 and x.childs[x.n] is not None:
            x = x.childs[x.n]
        return x, x.n-1

    def maximum(self):
        return self._maximum(self.root)

    def predecessor(self, x, i):
        if x.leaf:
            if i == 0:
                k = x.keys[i]
                if k < x.parent.keys[i]:
                    return None
                j = 1
                while j < x.parent.n and k > x.parent.keys[j]:
                    j += 1
                return x.parent, j
            else:
                return x, i-1
        else:
            return x.childs[i], x.childs[i].n-1

    def successor(self, x, i):
        if x.leaf:
            if i == x.n-1:
                k = x.keys[i]
                if k > x.parent.keys[x.parent.n-1]:
                    return None
                j = 0
                while j < x.parent.n and k > x.parent.keys[j]:
                    j += 1
                return x.parent, j+1
            else:
                return x, i+1
        else:
            return x.childs[i+1], 0

    def _delete(self, x, k):
        i = 0
        while i < x.n and k > x.keys[i]:
            i += 1

        if k == x.keys[i]:
            if x.leaf:
                for j in range(i, x.n-1):
                    x.keys[j] = x.keys[j+1]
                x.n -= 1
            else:
                if x.childs[i].n >= self.t:
                    pass


if __name__ == "__main__":
    DEBUG = False

    array = [2, 3, 5, 7, 11, 13, 15, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    bt = BTree(t=3)
    for item in array:
        print('*' * 80)
        bt.insert(item)
        print('**', item, '**')
        bt.print()
    print('*' * 80)

    for i in range(1, len(array)):
        node, idx = bt.predecessor(*bt.search(array[i]))
        print(array[i - 1], node.keys[idx])
