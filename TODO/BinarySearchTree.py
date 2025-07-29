"""
Binary Search Tree implementation.
Description: Left < root < right.
Real-life analogy: Phone book sorted by name.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)
    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            elif val < node.val:
                return _search(node.left, val)
            else:
                return _search(node.right, val)
        return _search(self.root, val)
# Example usage:
# bst = BinarySearchTree()
# bst.insert(5)
# bst.insert(3)
# print(bst.search(3))  # True 