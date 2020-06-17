## APPROACH 1 : RECURSION ##
# 1. base condition (to exit loop) i.e i>n => return 0  or i==n return 1
# 2. recursive call : climb(i+1,n) + climb(i+2,n)   
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(0, n)
    
    def helper(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.helper(i+1, n) + self.helper(i+2, n)

# Time: O(2^n)
# Space: O(n)



## APPROACH 2 : DP ##
#   1. top can be reached from (N-1)th Step or (N-2)th Step i.e ===> dp[N-1] + dp[N-2]
#   2. base case :                                              No of ways
#   0 steps     ===>    0 step                                      0
#   1 steps     ===>    1 step                                      1   
#   2 steps     ===>    (1 + 1 steps) or (2 steps)                  2       

#   FINDING DP PATTERN
#   3 steps     ===>    (1+1+1) (1+2) (2+1) (3)                     3
#   4 steps     ===>    (1+1+1+1) (1+2+1) (2+1+1) (1+1+2) (2+2)     5   (pattern found n-1 + n-2 )    
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        
        if n < 2:
            return dp[n]
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
# Time: O(n). Single loop upto nn.
# Space: O(n). dpdp array of size nn is used.


import math
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fib = ((1+sqrt5)/2)**(n+1) - ((1-sqrt5)/2)**(n+1)
        return int(fib/sqrt5)
    
# Time: O(logn). pow method takes logn time.
# Space: O(1). Constant space is used.