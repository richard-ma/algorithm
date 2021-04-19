class HuffmanEncodeTree:
    LEFT_CODE = '0'
    RIGHT_CODE = '1'

    class Node:
        def __init__(self, none=None):
            self.none = none
            self.key = ' '
            self.value = 0
            self.left = self.none
            self.right = self.none

        def print(self):
            print(
                self.key,
                self.value,
                self.left.key if self.left != self.none else 'None',
                self.right.key if self.right != self.none else 'None',
                end='')

    def __init__(self, none=None):
        self.none = none
        self.root = self.none
        self.encode_dict = dict()

    def _gen_encode_dict(self, root, code):
        print(code)
        if root.left == self.none and root.right == self.none:
            self.encode_dict[root.key] = code
            print(root.key)

        if root.left != self.none:
            self._gen_encode_dict(root.left, code+HuffmanEncodeTree.LEFT_CODE)

        if root.right != self.none:
            self._gen_encode_dict(root.right, code+HuffmanEncodeTree.RIGHT_CODE)

    def gen_encode_dict(self):
        self.encode_dict = dict()

        self._gen_encode_dict(self.root, '')

        return self.encode_dict

    def walk_print(self, root):
        if root != self.none:
            root.print()
            print()

        if root.left != self.none:
            self.walk_print(root.left)

        if root.right != self.none:
            self.walk_print(root.right)

    def print(self):
        self.walk_print(self.root)

    def insert(self, q, node):
        i = 0
        while i < len(q):
            if len(q) == 0 or node.value < q[i].value:
                break
            i += 1
        q.insert(i, node)

    def _build_queue(self, d):
        q = list()
        for key, value in d.items():
            node = HuffmanEncodeTree.Node()
            node.key = key
            node.value = value

            self.insert(q, node)

        return q

    def build(self, d):
        q = self._build_queue(d)

        while len(q) > 1:
            l = q.pop(0)
            r = q.pop(0)

            node = HuffmanEncodeTree.Node()
            node.value = l.value + r.value
            node.left = l
            node.right = r

            self.insert(q, node)
            self.root = node


if __name__ == "__main__":
    dictionary = {
        'a': 8167,
        'b': 1492,
        'c': 2782,
        'd': 4253,
        'e': 12702,
        'f': 2228,
        'g': 2015,
        'h': 6094,
        'i': 6966,
        'j': 153,
        'k': 772,
        'l': 4025,
        'm': 2406,
        'n': 6749,
        'o': 7507,
        'p': 1929,
        'q': 95,
        'r': 5987,
        's': 6327,
        't': 9056,
        'u': 2758,
        'v': 978,
        'w': 2360,
        'x': 150,
        'y': 1974,
        'z': 74,
    }

    het = HuffmanEncodeTree()
    het.build(dictionary)
    het.print()

    encode_dict = het.gen_encode_dict()
    print(encode_dict)
