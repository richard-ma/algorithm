from __future__ import annotations


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

    def reverse(self, method="iterate"):
        if method == "iterate":
            return self._reverse_iterate()

    def _reverse_iterate(self):
        if self.is_empty() or self.nil_ptr.next.next == self.nil_ptr:
            return

        x_prev = self.nil_ptr
        x = self.nil_ptr.next
        x_next = self.nil_ptr.next.next

        while x != self.nil_ptr:
            x.next = x_prev
            x_prev.prev = x

            x_prev = x
            x = x_next
            x_next = x_next.next

        self.nil_ptr.next = x_prev
        x_prev.prev = self.nil_ptr

    def merge(self, ll: LinkList):
        if ll.is_empty():
            return

        if self.is_empty():
            self.nil_ptr.next = ll.nil_ptr.next
            return

        self_ptr = self.nil_ptr.next
        ll_ptr = ll.nil_ptr.next

        while self_ptr != self.nil_ptr and ll_ptr != ll.nil_ptr:
            if ll_ptr.value < self_ptr.value:  # insert ll_ptr in front of self_ptr
                ll_ptr.next.prev = ll_ptr.prev
                ll_ptr.prev.next = ll_ptr.next

                ll_ptr.prev = self_ptr.prev
                self_ptr.prev.next = ll_ptr
                self_ptr.prev = ll_ptr

                ll_ptr = ll_ptr.next  # update ll_ptr

                self_ptr.prev.next = self_ptr
            else:
                self_ptr = self_ptr.next  # update self_ptr

        if ll_ptr != ll.nil_ptr:
            self_ptr = self_ptr.prev  # last item of self
            self_ptr.next = ll_ptr
            ll_ptr.prev = self_ptr
            while ll_ptr.next != ll.nil_ptr:
                ll_ptr = ll_ptr.next
            # ll_ptr is the last item of ll
            ll_ptr.next = self.nil_ptr
            self.nil_ptr.prev = ll_ptr


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

    print("Reverse List")
    l.reverse()
    l.print()

    print("Delete List")
    for item in array:
        l.delete(item)
        l.print(end='')
        print(" -> ", item)

    array = [1, 27, 29]
    array.reverse()
    l1 = LinkList()
    for item in array:
        l1.insert(item)
    l1.print()

    array = [5, 9, 18, 40]
    array.reverse()
    l2 = LinkList()
    for item in array:
        l2.insert(item)
    l2.print()

    l1.merge(l2)
    l1.print()

