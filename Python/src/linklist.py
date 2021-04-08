class LinkList:
    class Node:
        def __init__(self, value=None):
            self.prev = None
            self.value = value
            self.next = None

    def __init__(self):
        self.nil_ptr = LinkList.Node()
        self.nil_ptr.next = self.nil_ptr
        self.nil_ptr.prev = self.nil_ptr

    def is_empty(self):
        return self.nil_ptr.next == self.nil_ptr

    def print(self, end='\n'):
        ptr = self.nil_ptr.next
        while ptr != self.nil_ptr:
            print(ptr.value, ' ', end='')
            ptr = ptr.next
        print(end=end)

    def _insert(self, x):
        x.next = self.nil_ptr.next
        self.nil_ptr.next.prev = x
        self.nil_ptr.next = x
        x.prev = self.nil_ptr

    def insert(self, x):
        node = LinkList.Node(x)
        self._insert(node)

    def _delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def delete(self, x):
        node = self.search(x)
        self._delete(node)

    def search(self, k):
        ptr = self.nil_ptr.next
        while ptr != self.nil_ptr and ptr.value != k:
            ptr = ptr.next

        if ptr == self.nil_ptr:
            ptr = None
        return ptr


if __name__ == "__main__":
    array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

    l = LinkList()
    for item in array:
        l.insert(item)
    l.print()

    result = l.search(9)
    if result is not None:
        print(result.value)
    result = l.search(33)
    if result is None:
        print("Result is None.")

    for item in array:
        l.delete(item)
        l.print(end='')
        print(" -> ", item)
