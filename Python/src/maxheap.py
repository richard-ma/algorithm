from copy import deepcopy
from Python.src.helper import *


class MaxHeap:
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
        return MaxHeap.remove_first(self._data)

    @property
    def maximum(self) -> int:
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
    def max_heapify(data: list, idx: int, length: int) -> None:
        l = MaxHeap.left(idx)
        r = MaxHeap.right(idx)

        largest = idx
        if l <= length and data[l] > data[idx]:
            largest = l

        if r <= length and data[r] > data[largest]:
            largest = r

        if largest != idx:
            data[idx], data[largest] = data[largest], data[idx]
            MaxHeap.max_heapify(data, largest, length)

    def build(self, array: list):
        self._data = [0]
        self._data.extend(array)

        for idx in range(self.length // 2, 0, -1):
            MaxHeap.max_heapify(self._data, idx, self.length)

    def sort(self) -> list:
        sorted_array = deepcopy(self._data)
        array_length = len(sorted_array) - 1
        for idx in range(array_length, 1, -1):
            sorted_array[1], sorted_array[idx] = sorted_array[idx], sorted_array[1]
            array_length -= 1
            MaxHeap.max_heapify(sorted_array, 1, array_length)

        return MaxHeap.remove_first(sorted_array)

    def extract_maximum(self) -> int:
        if self.length <= 0:
            raise OverflowError()

        max_item = self._data[1]
        self._data[1] = self._data.pop()
        MaxHeap.max_heapify(self._data, 1, self.length)

        return max_item

    def increase_key(self, idx: int, key: int) -> None:
        if key < self._data[idx]:
            raise OverflowError()

        self._data[idx] = key
        while idx > 1 and self._data[MaxHeap.parent(idx)] < self._data[idx]:
            self._data[idx], self._data[MaxHeap.parent(idx)] = self._data[MaxHeap.parent(idx)], self._data[idx]
            idx = MaxHeap.parent(idx)

    def insert(self, key: int) -> None:
        self._data.append(INT_MIN)
        self.increase_key(self.length, key)


if __name__ == "__main__":
    print("** Class MaxHeap **")
    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    max_heap = MaxHeap(A)
    print(max_heap.data)
    max_heap.build(A)
    print(max_heap.data)
    max_heap = MaxHeap()
    print(max_heap.data)
    max_heap.build(A)
    print(max_heap.data)

    print(max_heap.sort())

    print(max_heap.maximum)

    print(max_heap.extract_maximum())
    print(max_heap.length)
    print(max_heap.data)

    max_heap.insert(11)
    print(max_heap.data)
    max_heap.insert(6)
    print(max_heap.data)
