# Method 1: BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # (0) edge case
        if amount < 0: 
            return -1
        elif amount == 0: 
            return 0
        if len(coins) == 0: 
            return -1
		
        # (1) BFS with a queue
        q = collections.deque([(0, 0)])
        seen = set()                    # record seen elements
        while q:
            curr_ele, num = q.popleft()
            for c in coins:
                if curr_ele + c == amount: 
                    return num + 1
                elif curr_ele + c < amount and (curr_ele + c) not in seen:
                    seen.add(curr_ele + c)
                    q.append((curr_ele + c, num + 1))
        return -1

# Time: O(N+E)
# Space: O(N)
    
    
    
# Method 2: Dynammic Programming    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0: return -1
        elif amount == 0: return 0
        if len(coins) == 0: return -1
		
        D = [0] + [-1] * amount
        cand = []
        for a in range(1, amount+1): # 從頭開始建構，無法用 coins 組合出就維持 -1
            cand.clear()
            for c in coins:
                if a-c >= 0 and D[a-c] >= 0:
                    cand.append(1 + D[a-c])
            if cand:
                D[a] = min(cand)
        return D[amount]