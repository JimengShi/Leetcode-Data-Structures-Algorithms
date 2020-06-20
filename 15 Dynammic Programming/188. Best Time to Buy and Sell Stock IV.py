class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        if k >= len(prices) // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        
        profits = [0]*len(prices)
        for j in range(k):
            preprofit = 0
            for i in range(1,len(prices)):
            
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit+profit, profits[i])
                profits[i] = max(profits[i-1], preprofit)
    
        return profits[-1]