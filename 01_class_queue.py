class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.peek())
print(q.dequeue())
print(q.is_empty())
