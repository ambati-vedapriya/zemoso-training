'''
Similar to a stack, you can implement a queue in Python using a list.
A queue follows the First In, First Out (FIFO) principle,
where the first element added is the first one to be removed.

'''


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)

print("Front:", queue.front())

dequeued_item = queue.dequeue()
print("Dequeued:", dequeued_item)

print("Queue after dequeue:", queue.items)
