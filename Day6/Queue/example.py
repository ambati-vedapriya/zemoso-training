'''
For implementing a queue, you can use the queue module, specifically the Queue class.

'''

from queue import Queue

# Create a Queue
queue = Queue()

# Enqueue (put) elements into the queue
queue.put(1)
queue.put(2)
queue.put(3)

# Check if the queue is empty
print("Is the queue empty?", queue.empty())

# Get the size of the queue
print("Size of the queue:", queue.qsize())

# Peek at the front of the queue without removing an element
if not queue.empty():
    front_element = queue.queue[0]
    print("Front element of the queue:", front_element)

# Dequeue (get) elements from the queue
dequeued_item = queue.get()
print("Dequeued item:", dequeued_item)

# Check the size after dequeue
print("Size of the queue after dequeue:", queue.qsize())

# Check if the queue is empty after dequeue
print("Is the queue empty after dequeue?", queue.empty())
