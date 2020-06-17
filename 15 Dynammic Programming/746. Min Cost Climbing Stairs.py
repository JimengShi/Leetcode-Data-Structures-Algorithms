# We can express the solution in terms of sub problems.
# To get to stair i, there's 2 possibilities: from stair i-1 and stair i-2. 
# The minimum cost is the minimum of those stairs plus the transition cost. 
# Continuously calculate this begining from stair 2 to the final stair. 
# Stair 0 and 1 cost 0 since we can start at either one for free.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2, curr = 0, 0, 0

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev1, prev2 = curr, prev1
        
        return curr
    
# Time: O(N) where N is the length of cost.
# Space: O(1)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
            
        return min(cost[n-1], cost[n-2])
    
# Time: O(N) where N is the length of cost.
# Space: O(1)