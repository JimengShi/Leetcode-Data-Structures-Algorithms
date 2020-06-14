# Method 1: DFS with recursion and visited set (do not change input)            
class Solution(object):
    def numIslands(self, grid):
        ans = 0
        visited = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if self.dfs(grid, i, j, visited):
                    ans += 1
        return ans
            
    def dfs(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or (i, j) in visited:
            return False
        visited.add((i, j))
        for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
            newi, newj = i + di, j + dj
            self.dfs(grid, newi, newj, visited)
        return True
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


# Method 2: DFS with only recursion (change input) 
class Solution(object):
    def numIslands(self, grid):
        ans = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if self.dfs(grid, i, j):
                    ans += 1
        return ans
            
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return False
        grid[i][j] = "0"
        for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
            newi, newj = i + di, j + dj
            self.dfs(grid, newi, newj)
        return True
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


# Method 3: DFS with stack and visited set (do not change input)  
class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0;
        
        islands = 0
        stack = []
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    stack.append((i, j))
                    
                    while stack:
                        row, col = stack.pop()
                        visited.add((i, j))
                        for dr, dc in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                            new_R = row + dr
                            new_C = col + dc
                            if 0 <= new_R < len(grid) and 0 <= new_C < len(grid[0]) and grid[new_R][new_C] == '1' and (new_R, new_C) not in visited:
                                stack.append((new_R, new_C)) 
        return islands
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.


# Method 4: DFS with only stack (change input) 
class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        stack = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    stack.append((i, j))
                    while stack:
                        row, col = stack.pop()      
                        if grid[row][col] == '1':
                            grid[row][col] = '0'
                            
                        for dr, dc in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                            new_R = row + dr
                            new_C = col + dc
                            if 0 <= new_R < len(grid) and 0 <= new_C < len(grid[0]) and grid[new_R][new_C] == '1':
                                stack.append((new_R, new_C)) 
        return islands
    
# Time: O(M×N) where M is the number of rows and N is the number of columns.
# Space: O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.