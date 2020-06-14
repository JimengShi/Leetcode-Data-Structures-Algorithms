class MedianFinder(object):
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):   
        # add numbers to two heaps and guarantee len(large) = len(small) or len(large) = len(small) + 1
        small, large = self.heaps
        heapq.heappush(large, num)
        heapq.heappush(small, -large[0])
        heapq.heappop(large)
        
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