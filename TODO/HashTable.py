"""
Hash table using Python dict.
Description: Key-value store with fast lookup.
Real-life analogy: Dictionary for word lookup.
"""
class HashTable:
    def __init__(self):
        self.table = dict()
    def put(self, key, value):
        self.table[key] = value
    def get(self, key):
        return self.table.get(key, None)
# Example usage:
# ht = HashTable()
# ht.put('a', 1)
# print(ht.get('a'))  # 1 