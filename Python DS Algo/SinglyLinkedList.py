"""
Singly linked list implementation.
Description: Each node points to the next.
Real-life analogy: Train cars linked in one direction.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    def search(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False
# Example usage:
# ll = SinglyLinkedList()
# ll.insert(1)
# ll.insert(2)
# print(ll.search(1))  # True 