# Method 1: sort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]

# Time: O(NlogN), where N is the length of points.
# Space: O(N).


# Method 2: min heap
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # (1) build a heap to save all points
        heap = list()
        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)        # distance
            heapq.heappush(heap, (d, point))
        
        # (2) heapq.heappop(heap) k times to get k closest
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
        
        # (3) return result
        return res

# Time: O(N) for building heap, O(KlogN) for extracting K times, where N is length of points.
# Space: O(N).


# Method 3: Divide and Conquer: quicksort
class Solution(object):
    def kClosest(self, points, K):
        nums = []
        for point in points:
            dist = math.sqrt(point[0]**2+point[1]**2)
            nums.append(dist)
        return self.kSmallest(nums, K)
    
    
    def kSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k == pos+1:
                return nums[pos]
            elif k < pos+1:
                return self.kSmallest(nums[:pos], k)
            else:
                return self.kSmallest(nums[pos+1:], k-pos-1)
            
    def partition(self, nums, l, r):
        # maintain two pointers l and r
        low = l
        while l < r:
            if nums[l] < nums[r]:                        # find 1st element > num[r] and move it right
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1                                       # traverse the nums with l += 1
        nums[low], nums[r] = nums[r], nums[low]          # swap
        return low
    
    
# Time: O(N) in the average case, O(N^2) in the worst case.
# Space: O(1).