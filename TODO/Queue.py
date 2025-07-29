"""
Queue (FIFO) implementation using deque.
Description: First-In-First-Out data structure.
Real-life analogy: Line at a ticket counter.
"""
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.popleft() if self.queue else None
    def is_empty(self):
        return len(self.queue) == 0
# Example usage:
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# print(q.dequeue())  # 1 