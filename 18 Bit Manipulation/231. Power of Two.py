class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        while n % 2 == 0:
            n /= 2
            
        return n == 1

# Time: O(logn)
# Space: O(1)



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return ( n & ( n-1 ) ) == 0
    
        # note:
        # power of 2 in binary         = b' 1000 ... 0, e.g.: (1000)2 --> 1*2^3 = 8
        # power of 2 minus 1 in binary = b' 0111 ... 1, e.g.: (0111)2 --> 1*2^2 + 1*2^1 + 1*2^0 = 7
        # bitwise AND of n and (n-1) must be 0 if n is power of 2
    
# Time: O(1)
# Space: O(1)