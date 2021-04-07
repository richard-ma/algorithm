from Python.src.helper import *


def min_max(A: list) -> tuple:
    if len(A) == 0:
        return None, None
    if len(A) == 1:
        return A[0], A[0]

    max_ret = INT_MIN
    min_ret = INT_MAX

    i = 0
    while i + 1 < len(A):
        if A[i] < A[i+1]:
            less, larger = A[i], A[i+1]
        else:
            less, larger = A[i+1], A[i]

        if less < min_ret:
            min_ret = less

        if larger > max_ret:
            max_ret = larger

        i += 2

    if i < len(A):
        if A[i] < min_ret:
            min_ret = A[i]
        if A[i] > max_ret:
            max_ret = A[i]

    return min_ret, max_ret


if __name__ == "__main__":
    array = [2, 8, 7, 1, 3, 5, 6, 4, 9]
    print(array)

    min_ret, max_ret = min_max(array)
    print(min_ret, max_ret)
