# Method 1: DP with bigger space  
class Solution:
    def rob(self, nums: List[int]) -> int:
        # (0) edge case
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # (1) maintain array
        dp = [ [0] * 2 for _ in range(n + 1)]
        print(dp)
        
        # (2) recursion formula
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])  # forget it
            dp[i][1] = nums[i - 1] + dp[i - 1][0]       # let's do it
            
        # (3) return result
        return max(dp[n][0], dp[n][1]) 

# Time: O(n)
# Space: O(n)


# Method 2: DP with smaller space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        yes, no = 0, 0
        for i in nums: 
            no, yes = max(no, yes), i + no
        return max(no, yes)
    
# Time: O(n)
# Space: O(1)