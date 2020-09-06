# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


# Method 1: hashtable
class Solution(object):
    def topKFrequent(self, nums, k):
        # Counter: {1: 3, 2: 2, 3: 1}
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        # Sorting based on frequency
        freq = list(d.keys())
        res = sorted(freq, key = lambda x : d[x], reverse = True)

        # return result
        return res[:k]
    
# Time: O(NlogN)
# Space: O(N)


# Method 2: min-heap   
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        # Counter: {1: 3, 2: 2, 3: 1}
        counts = collections.Counter(nums)

        # Sorting based on frequency using heap
        heap = [(-freq, num) for num, freq in counts.items()]
        heapq.heapify(heap)

        # return result
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
# Time: O(N+klogN)
# Space: O(N)