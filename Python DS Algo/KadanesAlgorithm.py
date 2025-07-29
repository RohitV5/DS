"""
Find maximum subarray sum (Kadane's Algorithm).
"""
class KadanesAlgorithm:
    @staticmethod
    def max_subarray_sum(arr):
        max_sum = curr_sum = arr[0]
        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
# Example usage:
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(KadanesAlgorithm.max_subarray_sum(arr)) 