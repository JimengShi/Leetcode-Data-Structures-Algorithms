class Solution:
    def mySqrt(self, x):
        # (0) edge case
        if x == 0 or x == 1:
            return x
        
        # (1) two pointers and while loop
        l, r = 1, x
        while l+1 < r:
            mid = (l+r) // 2
            v = mid * mid
            if v == x:
                return mid
            if v < x:
                l = mid
            else:
                r = mid
                
        # (2) return result
        return int(l)

# Time: O(logn)
# Space: O(1)