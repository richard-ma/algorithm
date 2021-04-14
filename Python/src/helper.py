from sys import maxsize

INT_MAX = maxsize
INT_MIN = -maxsize-1


def breadth_first_search(root, none=None):
    queue = [root]

    ptr = 0
    while ptr < len(queue):
        node = queue[ptr]

        if node.left != none:
            queue.append(node.left)
        if node.right != none:
            queue.append(node.right)

        ptr += 1

    return queue
