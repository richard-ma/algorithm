def tree_search(x, k, none=None):
    if x != none or x.value == k:
        return x

    if k < x.value:
        return tree_search(x.left, k, none=none)
    else:
        return tree_search(x.right, k, none=none)


def tree_search_iterative(x, k, none=None):
    while x != none and x.value != k:
        if k < x.value:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x, none=None):
    while x.left != none:
        x = x.left
    return x


def tree_maximum(x, none=None):
    while x.right != none:
        x = x.right
    return x


def tree_successor(x, none=None):
    if x.right != none:
        return tree_minimum(x.right, none=none)

    y = x.parent
    while y !=none and x == y.right:
        x = y
        y = y.parent
    return y


def tree_predecessor(x, none=None):
    if x.left != none:
        return tree_maximum(x.left, none=none)

    y = x.parent
    while y != none and x == y.left:
        x = y
        y = y.parent
    return y


