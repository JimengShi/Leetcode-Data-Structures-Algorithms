# Method 1: Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
    
# Time: O(N^2), loop will run n(n−1)/2 times.
# Space: O(1)    



# Method 2: maxprofit = price - minprice
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # (0) edge case
        if not prices:
            return 0
        
        # (1) minprice and maxprofit
        minprice = float('inf')                     # you also can initialize minprice = prices[0]
        maxprofit = 0
        
        # (2) traverse the prices list
        for i in range(len(prices)):
            if prices[i] < minprice:                # (2.1) find minprice
                minprice = prices[i]
                
            elif prices[i] - minprice > maxprofit:  # (2.2) find maxprofit
                maxprofit = prices[i] - minprice
        
        # (3) return result
        return maxprofit

    
# Time: O(N)
# Space: O(1)