from Python.src.helper import *


class ListNode:
    def __init__(self, v):
        self.prev = None
        self.value = v
        self.next = None


def list_print(head) -> None:
    ptr = head
    while ptr is not None:
        print(ptr.value, ' ', end='')
        ptr = ptr.next
    print()


def list_insert(head, x: ListNode):
    x.next = head
    if head is not None:
        head.prev = x
    head = x
    x.prev = None

    return head


def list_delete(head, x: ListNode):
    if x.prev is not None:
        x.prev.next = x.next
    else:
        head = x.next

    if x.next is not None:
        x.next.prev = x.prev

    return head


def list_search(head, k):
    x = head
    while x is not None and x.value != k:
        x = x.next

    return x


if __name__ == "__main__":
    array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    length = len(array)

    head = None
    # insert
    for item in array:
        node = ListNode(item)
        head = list_insert(head, node)
    list_print(head)

    # search
    k = 7
    x = list_search(head, k)
    if x is not None:
        print("SEARCH: ", x.value)
    else:
        print("NOT SEARCH: ", k)
    k = 13
    x = list_search(head, k)
    if x is not None:
        print("SEARCH: ", x.value)
    else:
        print("NOT SEARCH: ", k)

    # delete
    while head is not None:
        head = list_delete(head, head)
        list_print(head)

    print("** END **")

