from copy import deepcopy
from Python.src.helper import *


class MinHeap:
    def __init__(self, array=None) -> None:
        if array is not None:
            self.build(array)
        else:
            self._data = [0]

    @property
    def length(self) -> int:
        return len(self._data) - 1

    @property
    def data(self) -> list:
        return MinHeap.remove_first(self._data)

    @property
    def minimum(self) -> int:
        return self._data[1]

    @staticmethod
    def remove_first(array: list):
        return array[1:]

    @staticmethod
    def parent(idx: int) -> int:
        return idx // 2

    @staticmethod
    def left(idx: int) -> int:
        return idx * 2

    @staticmethod
    def right(idx: int) -> int:
        return idx * 2 + 1

    @staticmethod
    def min_heapify(data: list, idx: int, length: int) -> None:
        l = MinHeap.left(idx)
        r = MinHeap.right(idx)

        least = idx
        if l <= length and data[l] < data[idx]:
            least = l

        if r <= length and data[r] < data[least]:
            least = r

        if least != idx:
            data[idx], data[least] = data[least], data[idx]
            MinHeap.min_heapify(data, least, length)

    def build(self, array: list):
        self._data = [0]
        self._data.extend(array)

        for idx in range(self.length // 2, 0, -1):
            MinHeap.min_heapify(self._data, idx, self.length)

    def sort(self) -> list:
        sorted_array = deepcopy(self._data)
        array_length = len(sorted_array) - 1
        for idx in range(array_length, 1, -1):
            sorted_array[1], sorted_array[idx] = sorted_array[idx], sorted_array[1]
            array_length -= 1
            MinHeap.min_heapify(sorted_array, 1, array_length)

        return MinHeap.remove_first(sorted_array)

    def extract_minimum(self) -> int:
        if self.length <= 0:
            raise OverflowError()

        min_item = self._data[1]
        self._data[1] = self._data.pop()
        MinHeap.min_heapify(self._data, 1, self.length)

        return min_item

    def decrease_key(self, idx: int, key: int) -> None:
        if key > self._data[idx]:
            raise OverflowError()

        self._data[idx] = key
        while idx > 1 and self._data[MinHeap.parent(idx)] > self._data[idx]:
            self._data[idx], self._data[MinHeap.parent(idx)] = self._data[MinHeap.parent(idx)], self._data[idx]
            idx = MinHeap.parent(idx)

    def insert(self, key: int) -> None:
        self._data.append(INT_MAX)
        self.decrease_key(self.length, key)


if __name__ == "__main__":
    print("** Class MinHeap **")
    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    min_heap = MinHeap(A)
    print(min_heap.data)
    min_heap.build(A)
    print(min_heap.data)
    min_heap = MinHeap()
    print(min_heap.data)
    min_heap.build(A)
    print(min_heap.data)

    print(min_heap.sort())

    print(min_heap.minimum)

    print(min_heap.extract_minimum())
    print(min_heap.length)
    print(min_heap.data)

    min_heap.insert(5)
    print(min_heap.data)
    min_heap.insert(6)
    print(min_heap.data)
