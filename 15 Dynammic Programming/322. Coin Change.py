# Method 1: BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # (0) edge case
        if amount < 0: 
            return -1
        elif amount == 0: 
            return 0
		
        # (1) BFS with a queue
        queue = collections.deque([(0, 0)])
        seen = set()
        while queue:
            curr_ele, num = queue.popleft()
            for c in coins:
                if curr_ele + c == amount: 
                    return num + 1
                elif curr_ele + c < amount and (curr_ele + c) not in seen:
                    seen.add(curr_ele + c)
                    queue.append((curr_ele + c, num + 1))
        return -1

# Time: O(M^(amount/max(coins))), M is the length of coins, N is amount
# Space: O(N)
    
    
    
# Method 2: Dynammic Programming    
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
    
# Time: O(M*N), M is the length of coins, N is amount
# Space: O(N)