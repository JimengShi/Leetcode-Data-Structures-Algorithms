# Method 1: DFS with recursion  
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])    
        result = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    result = max(result, self.dfs(x, y, grid))
        return result
    
    def dfs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.dfs(i-1, j, grid) + self.dfs(i, j+1, grid) + self.dfs(i+1, j, grid) + self.dfs(i, j-1, grid)
        return 0
    
# Time: O(R∗C), where R is # of rows in the given grid, and C is # of columns.
# Space: O(R∗C).    

    
# Method 2: DFS with stack  
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    temp_count = 0
                    stack = [(r, c)]
                    seen.add((r, c))
                    while stack:
                        r, c = stack.pop()
                        temp_count += 1
                        
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] and (nr, nc) not in seen:
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, temp_count)
        return ans
    
# Time: O(R∗C), where R is # of rows in the given grid, and C is # of columns.
# Space: O(R∗C).   