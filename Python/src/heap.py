DEBUG = False


def parent(i: int) -> int:
    return i // 2


def left(i: int) -> int:
    return i * 2


def right(i) -> int:
    return i * 2 + 1


def max_heapify(A: list, i: int, length: int) -> None:
    l = left(i)
    r = right(i)

    largest = i
    if l <= length and A[l] > A[i]:
        largest = l

    if r <= length and A[r] > A[largest]:
        largest = r

    if largest != i:
        if DEBUG:
            print("exchange: \t", A[largest], "\t <--> \t", A[i], " - ", A)
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, length)


def build_max_heap(A: list, length: int) -> None:
    for i in range(length // 2, 0, -1):
        max_heapify(A, i, length)


def heap_sort(A: list) -> None:
    length = len(A) - 1
    if DEBUG: print("legnth: ", length)
    build_max_heap(A, length)
    if DEBUG: print("build-max-heap: ", A)
    for i in range(length, 1, -1):
        if DEBUG: print(A[1], "\t<->\t", A[i], "\t : \t\t", A)
        A[1], A[i] = A[i], A[1]
        length = length - 1
        if DEBUG:
            print(A[1], "\tmax-heapify: \t", A)
        max_heapify(A, 1, length)
        if DEBUG:
            print("\t\t\t\t\t", A)
            print("-" * 80)


def heap_maximum(A: list) -> int:
    return A[1]


def heap_extract_max(A: list) -> int:
    length = len(A) - 1
    if length < 1:
        raise OverflowError()

    max_item = A[1]
    A[1] = A[-1]
    A.pop()
    length = len(A) - 1
    max_heapify(A, 1, length)

    return max_item


if __name__ == "__main__":
    DEBUG = True

    A = [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    length = len(A) - 1

    from copy import deepcopy
    sorted_heap = deepcopy(A)
    heap_sort(sorted_heap)
    print(sorted_heap)

    print("*" * 80)

    max_queue = deepcopy(A)
    build_max_heap(max_queue, length)
    for i in range(length, 0, -1):
        print(heap_maximum(max_queue))
        max_item = heap_extract_max(max_queue)
        print(max_queue, " -> ", max_item)
        print("-" * 80)

    print("*" * 80)
