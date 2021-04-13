def tree_search(x, k):
    if x is None or x.value == k:
        return x

    if k < x.value:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def tree_search_iterative(x, k):
    while x is not None and x.value != k:
        if k < x.value:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)

    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)

    y = x.parent
    while y is not None and x == y.left:
        x = y
        y = y.parent
    return y


