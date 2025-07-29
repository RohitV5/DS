"""
Floyd's Tortoise and Hare algorithm for cycle detection in linked list.
"""
class CycleDetection:
    @staticmethod
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 