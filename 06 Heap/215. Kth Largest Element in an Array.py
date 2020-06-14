# Method 1: Sort and return  --> O(NlogN)



# Method 2: min-heap
import heapq   
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)  # always be a min-heap with size of k, k largest candidates from now on
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

# Time: O(k+(N-k)*logk), O(k) for building a heap, insert one element takes logk, and insert n-k elements
# Space: O(k) to store the heap elements.


# Method 2: min-heap
import heapq   
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)  # always be a min-heap with size of k, k largest candidates from now f
            else:
                if num > heap[0]:
                    heapq.heappushpop(heap, num)
        return heap[0]
        
# Time: O(N*logk)
# Space: O(k) to store the heap elements.


# Method 2: min-heap
import heapq   
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [num for num in nums]
        heapq.heapify(heap)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
    
# Time: O(N+(N-k)*logN), O(k) for building a heap, insert one element takes logk, and insert n-k elements
# Space: O(N) to store the heap elements.


# Method 2: min-heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for _ in range(k-1):
            heapq.heappop(heap)
        return -1*heapq.heappop(heap)
    
# Time: O(N+k*logN), O(k) for building a heap, insert one element takes logk, and insert n-k elements
# Space: O(N) to store the heap elements.
    

# Method 4: Quick selection
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
        pivot = nums[l]
        while l < r:
            # (<--) find the elment which < pivot and move them forward, now nums[right] is empty
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]        
            
            # (-->) find the elment which > pivot and move them backward, now nums[left] is empty
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
            
        nums[l] = pivot              # correct position of pivot, we can also write nums[right] = pivot
        return l                     # return index of pivot, we can also write return right
    
# Time: O(N) in the average case, O(N^2) in the worst case. T(N)=T(N/2)+O(N) --> O(N)
# Space: O(1).