# The key idea is to take down all daily returns and sum up all positive returns. 
# This works because we can break every trade down to several overnight trades.
# For example, considering [1, 2, 3], buy 1 sell 3 is equivalent to buy 1 sell 2 + buy 2 sell 3.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # (0) edge case
        if len(prices) == 1: 
            return 0
        
        # (1) only return positive daily profit
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1]))
        
        # (2) return result
        return sum(profit)
    
# Time: O(n)
# Space: O(1)
    
    
class Solution(object):
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)-1):
            if 0 < prices[i+1]- prices[i]:
                res += prices[i+1]- prices[i]
        return res
    
# Time: O(n)
# Space: O(1)