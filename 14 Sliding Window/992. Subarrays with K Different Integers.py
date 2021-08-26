class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)
    
    def atMostK(self, A: str, K: int) -> int:  # subarray with at most K different numbers
        # (0) edge case
        if not A:
            return 0
        
        # (1) initialize
        d = {}
        l, res = 0, 0
        
        # (2) traverse array
        for r in range(len(A)):
            d[A[r]] = d.get(A[r], 0) + 1   # (2.1) add characters of s into dictionary

            while len(d) > K:              # (2.2) deal with len(d) > 2
                d[A[l]] -= 1
                if d[A[l]] == 0:
                    del d[A[l]]
                l += 1

            res += r-l+1                   # (2.3) update the maxwindow

        # (3) return result
        return res
    
# Time: O(N)
# Space: O(N)
