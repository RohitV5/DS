"""
Doubly linked list implementation.
Description: Nodes have prev and next pointers.
Real-life analogy: Train cars linked in both directions.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Insert after a given node value
    def insert_after(self, target_data, data):
        curr = self.head
        while curr and curr.data != target_data:
            curr = curr.next
        if not curr:
            print("Target not found")
            return
        new_node = Node(data)
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    # Delete by value
    def delete(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if not curr:
            print("Key not found")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next  # Deleting head
        if curr.next:
            curr.next.prev = curr.prev

    # Delete at beginning
    def delete_at_beginning(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        curr = self.head
        if not curr.next:  # Only one node
            self.head = None
            return
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    # Traverse forward
    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    # Traverse backward
    def traverse_backward(self):
        curr = self.head
        if not curr:
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")

    # Search for a value
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    # Length of the list
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

# Example usage:
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.insert_after(10, 15)

dll.traverse_forward()     # Output: 5 <-> 10 <-> 15 <-> 20 <-> None
dll.traverse_backward()    # Output: 20 <-> 15 <-> 10 <-> 5 <-> None

# print(dll.search(15))      # True
# print(dll.length())        # 4

# dll.delete(10)
# dll.traverse_forward()     # Output: 5 <-> 15 <-> 20 <-> None

# dll.delete_at_beginning()
# dll.traverse_forward()     # Output: 15 <-> 20 <-> None

# dll.delete_at_end()
# dll.traverse_forward()     # Output: 15 <-> None
