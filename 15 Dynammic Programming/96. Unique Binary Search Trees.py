# Method 1: DP
class Solution:
    def numTrees(self, n: int) -> int:
        # (0) edge case
        if n <= 2:
            return n
        
        # (1) initialize dp array with base cases
        sol = [0] * (n + 1)
        sol[0] = sol[1] = 1
        
        # (2) iterative compute dp value with a general formula
        for i in range(2, n + 1):
            for left in range (0, i):
                sol[i] += sol[left] * sol[i - 1 - left]

        # (3) return result
        return sol[n]   

# Time: O(n^2)
# Space: O(n)
    
    
# Method 2: Mathematical Deduction
class Solution(object):
    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
    
# Time: O(n)
# Space: O(1)