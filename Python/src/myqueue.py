class MyQueue:
    def __init__(self, size: int = 4) -> None:
        self.length = size
        self.buffer = [0] * (self.length + 1)
        self.tail = 0
        self.head = 0

    def enqueue(self, x) -> None:
        self.buffer[self.tail] = x
        if self.tail == self.length:
            self.tail = 1
        else:
            self.tail += 1

    def dequeue(self) -> int:
        x = self.buffer[self.head]
        if self.head == self.length:
            self.head = 1
        else:
            self.head += 1
        return x


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue())
    print(q.dequeue())
