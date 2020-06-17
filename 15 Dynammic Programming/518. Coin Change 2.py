# Method 1: Dynammic programming, similar with Problem 322
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
    
# Time: O(N×amount), where N is a length of coins array.
# Space: O(amount) to keep dp array.



# Method 2: dfs, similar with Problem 39
class Solution(object):
    def change(self, amount, coins):
        if len(coins) == 0 and amount == 0:
            return 1
        if len(coins) == 0:
            return 0

        coins.sort()
        path = []                                    # 在遍历的过程中记录路径，一般而言它是一个栈
        res = []
        
        self.dfs(coins, 0, path, res, amount)        # 注意要传入 size ，在 range 中， size 取不到
        return len(res)

    def dfs(self, coins, begin, path, res, amount):
        if amount == 0:
            res.append(path[:])                      # Python 中可变对象是引用传递，因此拷贝出 path 里的值

        for index in range(begin, len(coins)):
            residue = amount - coins[index]
            
            if residue < 0:                          # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
                break
            
            path.append(coins[index])
            self.dfs(coins, index, path, res, residue)   # 因为下一层不能比上一层还小，起始索引还从 index 开始
            path.pop()