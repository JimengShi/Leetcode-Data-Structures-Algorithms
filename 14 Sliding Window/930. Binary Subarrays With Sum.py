# Method 1: two pointers
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # (1) initialize two pointers and result and count and sum
        l = count = res = 0
        s = 0
        
        # (2) traverse the list A
        for r, item in enumerate(A):
            s += item                 # (2.1) accumulation
            if item == 1:             # (2.2) first set count is 0 when item == 1
                count = 0
            while l <= r and s >= S:  # (2.3) shrink window when s >= S
                if s == S:
                    count += 1
                s -= A[l]
                l += 1
            res += count              # (2.4) update result
        
        # (3) return result
        return res
    
# Time: O(N), where N is the length of A.
# Space: O(1).