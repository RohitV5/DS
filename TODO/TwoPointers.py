"""
Example: Check if array has pair with sum target (Two Pointers Technique).
"""
class TwoPointers:
    @staticmethod
    def has_pair_with_sum(arr, target):
        arr.sort()
        left, right = 0, len(arr)-1
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                return True
            elif s < target:
                left += 1
            else:
                right -= 1
        return False
# Example usage:
# arr = [1,2,4,4]
# print(TwoPointers.has_pair_with_sum(arr, 8)) 