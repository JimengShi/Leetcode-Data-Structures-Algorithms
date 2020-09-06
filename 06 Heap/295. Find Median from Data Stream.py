# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
# For example,
# [2,3,4], the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.

# Example:
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
 

# Follow up:
# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


class MedianFinder(object):
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):   
        # add numbers to two heaps and guarantee len(large) = len(small) or len(large) = len(small) + 1
        small, large = self.heaps
        heapq.heappush(large, num)
        heapq.heappush(small, -heapq.heappop(large))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))


    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

    

"""
addNum
Runtime: O(log n)
Spacetime: O(n)

findMedian
Runtime: O(1)
Spacetime: O(1)
"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# -we maintain HashMap<number,frequency>
# -we also maintain total number of elements, so that median is just total-nums/2 th element from sorted array.
# -then we go over Map from 1-100 and count element, when we hit total-nums/2 th element , that is our median

"""
addNum
Runtime: O(log n)
Spacetime: O(n)

findMedian
Runtime: O(1)
Spacetime: O(1)
"""

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# -we maintain HashMap<number,frequency>
# -we also maintain total number of elements, so that median is just total-nums/2 th element from sorted array.
# -then we go over Map from 1-100 and count element, when we hit total-nums/2 th element , that is our median