"""
Min-Heap using heapq.
Description: Smallest element at root.
Real-life analogy: Priority queue for tasks.
"""
import heapq
class MinHeap:
    def __init__(self):
        self.heap = []
    def push(self, val):
        heapq.heappush(self.heap, val)
    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None
# Example usage:
# mh = MinHeap()
# mh.push(3)
# mh.push(1)
# print(mh.pop())  # 1 