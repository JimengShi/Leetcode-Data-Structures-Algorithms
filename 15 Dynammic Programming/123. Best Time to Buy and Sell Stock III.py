class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_profits = [0] * n
        
        total_max_profit = 0
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price, prices[i])
            total_max_profit = max(total_max_profit, prices[i] - min_price)
            left_profits[i] = total_max_profit

        max_profit = 0
        max_price = float('-inf')
        for i in range(n - 1, 0, -1):
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, max_price - prices[i])

            total_max_profit = max(total_max_profit, max_profit + left_profits[i - 1])

        return total_max_profit

# Time: O(n)
# Space: O(n)    
   
    
class Solution(object):
    def maxProfit(self, prices):

        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit
    
    
# Time: O(n)
# Space: O(1)