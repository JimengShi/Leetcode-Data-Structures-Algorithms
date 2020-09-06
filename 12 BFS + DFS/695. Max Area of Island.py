# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:
# [[0,0,1,0,1,0],
#  [0,0,1,1,1,0],
#  [0,0,0,0,1,0],
#  [0,1,1,1,0,0],
#  [0,1,1,0,0,0]]

# Given the above grid, return 6. because the island must be connected 4-directionally. 


# Method 1: DFS with recursion  
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])    
        res = 0
        visited = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in visited:
                    res = max(res, self.dfs(x, y, grid, visited))
        return res
        
    def dfs(self, i, j, grid, visited):
        m, n = len(grid), len(grid[0])
        count = 1
        visited.add((i, j))
        for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
            new_r = i + dr
            new_c = j + dc
            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                count += self.dfs(new_r, new_c, grid, visited)
        return count
    
# Time: O(R∗C), where R is # of rows in the given grid, and C is # of columns.
# Space: O(R∗C).    

    
# Method 2: DFS with stack  
class Solution(object):
    def maxAreaOfIsland(self, grid):
        # (1) initialize
        seen = set()
        ans = 0
        
        # (2) dfs for each point
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    # dfs to get temp count
                    temp_count = 0
                    stack = [(r, c)]
                    while stack:
                        r, c = stack.pop()
                        temp_count += 1
                        seen.add((r, c))
                        for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                            new_r, new_c = r+dr, c+dc
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] and (new_r, new_c) not in seen:
                                stack.append((new_r, new_c))
                                seen.add((new_r, new_c))
                    # update ans            
                    ans = max(ans, temp_count)
        
        # (3) return final result            
        return ans
    
# Time: O(R∗C), where R is # of rows in the given grid, and C is # of columns.
# Space: O(R∗C).   