# We can express the solution in terms of sub problems.
# To get to stair i, there's 2 possibilities: from stair i-1 and stair i-2. 
# The minimum cost is the minimum of those stairs plus the transition cost. 
# Continuously calculate this begining from stair 2 to the final stair. 
# Stair 0 and 1 cost 0 since we can start at either one for free.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        dp = [0] * n
        for i in range(2, n):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n - 1]

# Time: O(N) where N is the length of cost.
# Space: O(N)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        dp0, dp1, dp2 = 0, 0, 0
        for i in range(2, n):
            dp2 = min(dp0 + cost[i - 2], dp1 + cost[i - 1])
            dp0, dp1 = dp1, dp2
        return dp2
    
# Time: O(N) where N is the length of cost.
# Space: O(1)