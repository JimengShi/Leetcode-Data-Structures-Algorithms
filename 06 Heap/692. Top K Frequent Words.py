# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.

# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


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
        counts = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counts.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
# Time: O(N+klogN)
# Space: O(N)