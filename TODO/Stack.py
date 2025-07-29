"""
Stack (LIFO) implementation using list.
Description: Last-In-First-Out data structure.
Real-life analogy: Stack of plates; add/remove from the top.
"""
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def peek(self):
        return self.stack[-1] if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0
# Example usage:
# s = Stack()
# s.push(1)
# s.push(2)
# print(s.pop())  # 2 