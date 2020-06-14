# Method 1: binary search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # (1) x is on the left of arr[0]
        if x <= arr[0]: 
            return arr[:k]
        
        # (2) x is on the right of arr[-1]
        if x >= arr[-1]: 
            return arr[-k:]
        
        # (3) x is in the middle of array, binary search to find the closest element to x
        l, r = 0, len(arr)-k
        while l < r:
            m = (l+r) >> 1        # m = (l+r) // 2
            if x-arr[m] > arr[m+k]-x:
                l = m + 1
            else:
                r = m
                
        return arr[l:l+k]
    
# Time: O(logn+k). O(logn) is for binary search to find the closest element to x, while O(k) is for shrinking the index range to k elements.
# Space: O(k). It is to generate the required sublist.

# x << y: multiplying x by 2**y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).

# x >> y: dividing x by 2**y
# Returns x with the bits shifted to the right by y places.

# e.g.: 2 << 5 to get 64 = 2*2^5, 1000 >> 2 to get 250 = 1000 / 2^2.



# Method 2:
class Solution(object):
    def findClosestElements(self, arr, k, x):
        i, j = 0, len(arr)-1
        while j-i+1 != k:
            # will stop once we have k elements
            # else keep shifting pointers towards minimum difference
            left_diff = abs(arr[i] - x)
            right_diff = abs(arr[j] - x)
            if left_diff > right_diff:
                i += 1
            else:
                j -= 1
        return arr[i:j+1]

# Time: O(n)
# Space: O(k)
    
    
    
# Method 3: heap
import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []
        for num in arr[:k]:                                     # klogk
            heapq.heappush(heap, [-(abs(num - x)), -num])
        # heapq.heapify(heap)
        
        for num in arr[k:]:                                     # (n-k)logk
            if -(abs(num - x)) >= heap[0][0]:
                heapq.heappush(heap, [-(abs(num - x)), -num])
                heapq.heappop(heap)
                
        return sorted([-pair[1] for pair in heap])              # klogk
    
# Time: O(nlogk)
# Space: O(k)
