class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i+1) for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in range(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush(heap, (nums[nei+1]-nums[root], root, nei+1))
        return d

# Time: O((N+klogN+NlogN), where N is the length of nums. O(klogN) + O(N) + O(klogN)
# Space: O(N), the space used to store our heap of at most N-1 elements.