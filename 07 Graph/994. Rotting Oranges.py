# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queuefrom collections import deque

import collections
class Solution: 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # (0) edge case
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return -1
        
        # (1) initialize the a queue to save index of rotten oranges and minute == 0
        queue = collections.deque()
        minute = 0
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        
        # (2) count up the number of fresh oranges
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        if not fresh:
            return 0
        
        # (3) BFS with a queue to search next fresh oranges
        while queue:
            minute += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:                    
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
                        fresh -= 1
                        if fresh == 0:
                            return minute
                        
        # (4) return results after we jump out of the 'while' loop
        return -1
    
