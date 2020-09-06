# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

# Example 1:
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Example 2:
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Example 3:
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


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