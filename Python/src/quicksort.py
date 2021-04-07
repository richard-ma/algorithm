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


def quick_sort(A: list, p: int, r: int, partition_func: callable = partition) -> None:
    if p < r:
        q = partition_func(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def quick_sort_2(A: list, p: int, r: int, partition_func: callable = partition) -> None:
    while p < r:
        q = partition_func(A, p, r)
        quick_sort_2(A, p, q - 1)
        p = q + 1


if __name__ == "__main__":
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)

    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(array)
    quick_sort(array, 0, len(array)-1, partition_func=random_partition)
    print(array)

    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(array)
    quick_sort_2(array, 0, len(array)-1)
    print(array)

    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(array)
    quick_sort_2(array, 0, len(array)-1, partition_func=random_partition)
    print(array)
