# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0

# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.


class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1) for i in range(len(nums)-1)]
        heapq.heapify(heap)

        for _ in range(k):
            diff, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush(heap, (nums[nei+1]-nums[root], root, nei+1))
                
        return diff

# Time: O((N+klogN+NlogN), where N is the length of nums. O(klogN) + O(N) + O(klogN)
# Space: O(N), the space used to store our heap of at most N-1 elements.

# index:                 i = 0,1,2,3,4
# example: [3,1,4,5,1] ---> [1,1,3,4,5]
# diff:                    = 0,2,1,1