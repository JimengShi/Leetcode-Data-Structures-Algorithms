# Given a collection of intervals, merge all overlapping intervals.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # (1) sort the whole input based on the first element of each interval
        intervals.sort(key = lambda x: x[0])
        
        # (2) maintain a list to save the output
        merged = []
        for interval in intervals:
            # merged list is empty or current interval does not overlap with the previous --> append
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        # (3) return the whole mergerd list
        return merged
    
# Time: O(nlogn)
# Space: O(n)