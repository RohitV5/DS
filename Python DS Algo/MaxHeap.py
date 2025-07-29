"""
Max-Heap using heapq (invert values).
Description: Largest element at root.
Real-life analogy: Leaderboard for top scores.
"""
import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self, val):
        heapq.heappush(self.heap, -val)
    def pop(self):
        return -heapq.heappop(self.heap) if self.heap else None
# Example usage:
# mxh = MaxHeap()
# mxh.push(3)
# mxh.push(1)
# print(mxh.pop())  # 3 