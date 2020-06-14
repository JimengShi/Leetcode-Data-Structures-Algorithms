# Method 1: Sort and return  --> O(NlogN)

    
# Method 2: min-heap
# Time: O(Nlogk) insert one element takes logk, and need to insert n elements
# Space: O(k) to store the heap elements.
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k-1]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
    
# Quickselect
# Time: O(N) in the average case, O(N^2) in the worst case.
# Space: O(1).
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quicksort is ascending order, so kth largest needs to change to solve len(nums)-k+1 Smallest
        res = self.findKthSmallest(nums, len(nums)+1-k)
        return res

    # find kth Smallest using quicksort
    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k == pos+1:
                return nums[pos]
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)

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