class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = 0
        m = {}
        for a in A:
            for b in B:
                m[a + b] = m.get(a + b, 0) + 1
        for c in C:
            for d in D:
                cnt += m.get(-(c + d), 0)
        return cnt
    
# Time: O(N^2). 2 nested loops to count sums, and another 2 nested loops to find complements.
# Space: O(N^2) for the hashmap. There could be up to O(n^2) distinct a + b keys.