# Method 1: brute force
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        # (1) initialize
        res = []
        for i in nums1[k]:
            for j in nums2[k]:
                res.append([i,j])
                
        return res.sort(key = lambda x: x[0] + x[1])[:k]
    
    
# Method 2: heap
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        # (0) edge case
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        # (1) build a heap with k pairs consisted of (nums1[i], nums2[0])
        heap = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, [nums1[i] + nums2[j], i, j])

        for x in range(0, k):
            push(x, 0)
        
        # (2) maintain a list to save the result
        pairs = []
        while heap and len(pairs) < k:
            _, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)

        # (3) return result
        return pairs
    
# Time: O(klogk)
# Space: O(k)