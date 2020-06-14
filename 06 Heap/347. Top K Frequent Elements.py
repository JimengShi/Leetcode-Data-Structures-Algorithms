# Method 1: hashtable
class Solution(object):
    def topKFrequent(self, nums, k):
        # d = collections.Counter(nums)
        # s = sorted(list(d.items()), key=lambda x: -x[1])
        # return [num for num, freq in s][:k]
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        freq = list(d.keys())
        res = sorted(freq, key = lambda x : d[x], reverse = True) 
        return res[:k]
    
# Time: O(NlogN)
# Space: O(N)


# Method 2: min-heap   
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        counts = collections.Counter(nums)
        heap = [(-freq, num) for num, freq in counts.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
# Time: O(N+klogN)
# Space: O(N)