# Method 1: hashtable
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # d = collections.Counter(words)
        # s = sorted(list(d.items()), key=lambda x: (-x[1], x[0]))
        # return [c for c, n in s][:k]
        d = {}                                     # {'leetcode': 1, 'i': 2, 'love': 2, 'coding': 1}
        for word in words:
            # d[word] = d.get(word, 0) + 1
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        freq = list(d.keys())                      # ['leetcode', 'i', 'love', 'coding']
        freq.sort(key = lambda x : (-d[x], x))     # ['i', 'love', 'coding', 'leetcode']
        return freq[:k]
    
# Time: O(NlogN)
# Space: O(N)


# Method 2: heap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)        # {'leetcode': 1, 'i': 2, 'love': 2, 'coding': 1}
        heap = [(-freq, word) for word, freq in counts.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
# Time: O(N+klogN)
# Space: O(N)