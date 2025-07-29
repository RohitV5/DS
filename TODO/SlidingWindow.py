"""
Example: Find max sum subarray of size k (Sliding Window Technique).
"""
class SlidingWindow:
    @staticmethod
    def max_sum_subarray(arr, k):
        max_sum = curr_sum = sum(arr[:k])
        for i in range(k, len(arr)):
            curr_sum += arr[i] - arr[i-k]
            max_sum = max(max_sum, curr_sum)
        return max_sum
# Example usage:
# arr = [1,2,3,4,5]
# print(SlidingWindow.max_sum_subarray(arr, 3)) 