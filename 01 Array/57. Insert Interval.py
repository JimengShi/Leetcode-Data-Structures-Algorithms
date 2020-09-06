# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # (1) maintain a merged list to save output
        merged = []
        
        # (2) traverse input and compare each of them with newInterval
        for interval in intervals:
            # case 1: interval: [1,2], newInterval: [4,8]  ---> append(interval)
            if newInterval is None or interval[1] < newInterval[0]:  
                merged.append(interval)
            
            # case 2: interval: [6,7], newInterval: [4,5] ----> append(newInterval) first, then interval
            elif interval[0] > newInterval[1]:                       
                merged.append(newInterval)
                merged.append(interval)
                newInterval = None
                
            # case 3: there is overlap: interval: [4,7], newInterval: [5,8] ---> get minleft and maxright
            else:                                                    
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # (3) solve case 3 after newInterval is updated [[1,2],[3,5]], [4,8] --> update [4,8] as [3,8]
        if newInterval is not None:
            merged.append(newInterval)
        
        # (4) return the result merged list
        return merged
    
# Time: O(n)
# Space: O(n)