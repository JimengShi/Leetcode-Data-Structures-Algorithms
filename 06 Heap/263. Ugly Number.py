class Solution:
    def isUgly(self, num: int) -> bool:
        # (0) edge case
        if num == 0:
            return False
        
        # (1) traverse given_prime
        given_prime = [2, 3, 5]
        for p in given_prime:
            while num % p == 0:
                num //= p
        
        # (2) return result
        if num == 1:
            return True
        else:
            return False
        
# Time: O(3*logn), n is the given number
# Space: O(1)