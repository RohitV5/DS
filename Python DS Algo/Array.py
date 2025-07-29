"""
Dynamic array (Python list) implementation.
Description: Stores elements in contiguous memory, supports random access.
Real-life analogy: Like a row of lockers, each with a number (index).
"""
class Array:
    def __init__(self, elements=None):
        self.data = elements if elements else []
    def append(self, value):
        self.data.append(value)
    def get(self, index):
        return self.data[index]
    def __repr__(self):
        return str(self.data)
# Example usage:
# arr = Array([1,2,3])
# arr.append(4)
# print(arr.get(2))  # 3 