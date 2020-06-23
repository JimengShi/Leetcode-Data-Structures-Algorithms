# Find Minimum Number of Coins
# Given a value amount, if we want to make change for it, and we have infinite supply of each of the denominations, i.e., we have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change?\
# Similar with Leetcode 322, 518

def minCoins(coins, amount):
    result = []
    for i in coins[::-1]:
        while amount >= i:      # greedy: always want to big value first
            amount -= i
            result.append(i)

    return result

# Time: O(N)
# Space: O(N)

# coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
# amount = 93
# minCoins(coins, amount)