# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1


# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Method 1: DFS with recursion and visited set (do not change input)  
# Goal of DFS: start from each point of matrix, traversing all of connected '1'
class Solution(object):
    def numIslands(self, grid):
        ans = 0
        visited = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:  # use dfs condition for m*n points in matrix
                    self.dfs(grid, i, j, visited)
                    ans += 1
        return ans
            
    def dfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])

        visited.add((i, j))
        
        for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
            newi = i + di
            newj = j + dj
            if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == '1' and (newi, newj) not in visited:
                self.dfs(grid, newi, newj, visited)
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


# Method 2: DFS with only recursion (change input) 
class Solution(object):
    def numIslands(self, grid):
        ans = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    ans += 1
        return ans
            
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        
        grid[i][j] = "0"
        
        for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
            newi, newj = i + di, j + dj
            if 0 <= newi < m and 0 <= newj < n and grid[newi][newj] == '1':
                self.dfs(grid, newi, newj)
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


# Method 3: DFS with stack and visited set (do not change input)  
class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:     
        islands = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()
                        visited.add((i, j))
                        for dr, dc in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                            new_R = row + dr
                            new_C = col + dc
                            if 0 <= new_R < len(grid) and 0 <= new_C < len(grid[0]) and grid[new_R][new_C] == '1' and (new_R, new_C) not in visited:
                                stack.append((new_R, new_C))
                                visited.add((new_R, new_C))
        return islands
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


# Method 4: DFS with only stack (change input) 
class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    
                    stack = [(i, j)]
                    while stack:
                        row, col = stack.pop()      
                        grid[row][col] = '0'
                            
                        for dr, dc in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                            new_R = row + dr
                            new_C = col + dc
                            if 0 <= new_R < len(grid) and 0 <= new_C < len(grid[0]) and grid[new_R][new_C] == '1':
                                stack.append((new_R, new_C)) 
        return islands
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.