import random


def partition(A: list, p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    return i + 1


def random_partition(A: list, p: int, r: int) -> int:
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def random_select(A: list, p: int, r: int, i: int) -> int:
    if p == r:
        return A[p]

    q = random_partition(A, p, r)
    k = q - p + 1

    if k == i:
        return A[q]
    elif i < k:
        return random_select(A, p, q-1, i)
    else:
        return random_select(A, q+1, r, i - k)


if __name__ == "__main__":
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(array)

    print(random_select(array, 0, len(array)-1, 1))
    print(random_select(array, 0, len(array)-1, 3))
    print(random_select(array, 0, len(array)-1, 4))
    print(random_select(array, 0, len(array)-1, 8))
