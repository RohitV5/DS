"""
Example: Activity selection (max non-overlapping intervals).
"""
class Greedy:
    @staticmethod
    def activity_selection(intervals):
        intervals.sort(key=lambda x: x[1])
        res, last_end = [], float('-inf')
        for start, end in intervals:
            if start >= last_end:
                res.append((start, end))
                last_end = end
        return res
# Example usage:
# intervals = [(1,3),(2,4),(3,5)]
# print(Greedy.activity_selection(intervals)) 