"""
Binary tree traversals: inorder, preorder, postorder, level-order.
"""
class TreeTraversals:
    @staticmethod
    def inorder(root):
        return TreeTraversals._inorder(root, [])
    @staticmethod
    def _inorder(node, res):
        if node:
            TreeTraversals._inorder(node.left, res)
            res.append(node.val)
            TreeTraversals._inorder(node.right, res)
        return res
    @staticmethod
    def preorder(root):
        return TreeTraversals._preorder(root, [])
    @staticmethod
    def _preorder(node, res):
        if node:
            res.append(node.val)
            TreeTraversals._preorder(node.left, res)
            TreeTraversals._preorder(node.right, res)
        return res
    @staticmethod
    def postorder(root):
        return TreeTraversals._postorder(root, [])
    @staticmethod
    def _postorder(node, res):
        if node:
            TreeTraversals._postorder(node.left, res)
            TreeTraversals._postorder(node.right, res)
            res.append(node.val)
        return res
    @staticmethod
    def level_order(root):
        from collections import deque
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res 