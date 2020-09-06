# Given an integer matrix, find the length of the longest increasing path.

# From each cell, you can either move to four directions: left, right, up or down. 
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1: Input: nums = 
#                         [
#                           [9,9,4],
#                           [6,6,8],
#                           [2,1,1]
#                         ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2: Input: nums = 
#                         [
#                           [3,4,5],
#                           [3,2,6],
#                           [2,2,1]
#                         ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


# Method 1: Naive DFS Solution [Time Limit Exceed]
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(i, j, matrix, m, n))
        return res
    
    # dfs is used to return the max path length starting at (x,y)
    def dfs(self, i, j, matrix, m, n):
        length = 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                length = max(length, 1 + self.dfs(x, y, matrix, m, n))     # get the max length among dfs(neighbors of (i, j))
        return length                   
    
# Time: O(mn*4^(m+n)). 
# Totally mn node, each node has 4 directions and (m+n) length at most, which recursive depth is m+n at most
# Space: O(mn*4^(m+n)).


# Method 2: DFS + Memoization
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # (0) edge case
        if not matrix:
            return 0
        
        # (1) initialize a cache(=-1) to record we have not compute the length of this node
        m, n = len(matrix), len(matrix[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0
        
        # (2) dfs to traverse each node
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(i, j, matrix, cache))
        return res

    def dfs(self, i, j, matrix, cache):
        m, n = len(matrix), len(matrix[0])
        # (2.1) != -1 means we has computed the length of this node
        if cache[i][j] != -1:
            return cache[i][j]
        
        # (2.2) set the length of this node == 1 and search its four neighbors
        length = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                length = max(length, 1 + self.dfs(x, y, matrix, cache))
                
        # (2.3) update cache
        cache[i][j] = length
        
        return length               # return the max path length starting at (x,y)

    
# Time: O(mn). Each vertex will be calculated only once, and each edge will be visited only once.
# The total time complexity is then O(V+E). In our problem, O(V)=O(mn), O(E)=O(4V)=O(mn).
# Space: O(mn). The cache dominates the space complexity.