# Method 1: Naive DFS Solution [Time Limit Exceed]
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if len(matrix) == 0:
#             return 0
#         m, n = len(matrix), len(matrix[0])
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 cur_len = self.dfs(i, j, matrix, m, n)
#                 res = max(res, cur_len)
#         return res
    
#     def dfs(self, i, j, matrix, m, n):
#         res = 0
#         directions = [(1,0),(-1,0),(0,1),(0,-1)]
#         for direction in directions:
#             x, y = i + direction[0], j + direction[1]
#             if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
#                 continue
#             res = max(self.dfs(x, y, matrix, m, n), res)
#         return res               # return the max path length starting at (x,y)
    


# Method 2: DFS + Memoization
# Time: O(mn). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once. The total time complexity is then O(V+E). V is the total number of vertices and E is the total number of edges. In our problem, O(V)=O(mn), O(E)=O(4V)=O(mn).
# Space: O(mn). The cache dominates the space complexity.

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
                cur_len = self.dfs(i, j, matrix, cache, m, n)
                res = max(res, cur_len)
        return res

    def dfs(self, i, j, matrix, cache, m, n):
        # (2.1) != -1 means we has computed the length of this node
        if cache[i][j] != -1:
            return cache[i][j]
        
        # (2.2) set the length of this node == 1 and search its four neighbors
        res = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                length = 1 + self.dfs(x, y, matrix, cache, m, n)
                res = max(length, res)
                
        # (2.3) update cache
        cache[i][j] = res
        
        return res               # return the max path length starting at (x,y)