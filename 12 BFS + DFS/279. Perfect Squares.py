# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


# Method 1: BFS
class Solution:
    def numSquares(self, n: int) -> int:
        # (0) edge case
        if n < 2: 
            return n
        
        # (1) intialize square numbers
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        
        # (2) BFS
        level = 0
        queue = [n]
        while queue:
            level += 1
            
            next_queue = set()
            for curr_sum in queue:
                for square in squares:
                    if curr_sum == square:
                        return level
                    if curr_sum < square:
                        break
                    else:
                        next_queue.add(curr_sum - square)
            queue = next_queue            # eliminate duplicate to prevent exponential calls
        
        # (3) return result
        return level

# Time: O(N^h))
# Space: O(N) 
    

# Method 2: DP
class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if square > i:               # try squre who < i
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]
    
# Time: O(N*sqrt(N))
# Space: O(N)