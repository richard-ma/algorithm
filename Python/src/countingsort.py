def counting_sort(A: list, B: list, k: int) -> None:
    A.insert(0, 0)
    B.insert(0, 0)

    C = list()
    for i in range(0, k+1):
        C.append(0)

    for j in range(1, len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k+1):
        C[i] = C[i-1] + C[i]

    for j in range(len(A)-1, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

    A.pop(0)
    B.pop(0)


if __name__ == "__main__":
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(array)

    result = [0] * len(array)
    print(result)

    k = max(array)
    print(k)

    counting_sort(array, result, k)
    print(result)
