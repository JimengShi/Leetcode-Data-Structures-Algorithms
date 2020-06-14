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