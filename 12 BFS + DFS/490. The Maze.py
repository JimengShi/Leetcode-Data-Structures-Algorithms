# Method 1: recursively
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # (1) initialize a visited set and maze (rows x columns)
        m, n = len(maze), len(maze[0])
        seen = set()
        
        # (2) define a dfs helper function to traverse path
        def dfs(i, j):
            # (2.1) edge case: start coordinate = destination coordinate
            if [i, j] == destination: 
                return True
            seen.add((i, j))

            # (2.2) move the ball left, right, down, up
            directions = [(0,-1), (0,1), (-1,0), (1,0)]
            for dx, dy in directions:
                x, y = i, j
                while 0 <= x+dx < m and 0 <= y+dy < n and maze[x+dx][y+dy] == 0:  # move condition
                    x, y = x+dx, y+dy
                    
                if (x, y) not in seen: 
                    if dfs(x, y):
                        return True
            return False
        
        # (3) return dfs(start coordinate)
        return dfs(start[0], start[1])
    
# Time: O(|V|+|E|). In our maze, O(|V|) = O(|E|) = m * n, so time complexity is O(mn).
# Space: O(|V| + |E|) for seen list.


    
# Method 2: queue    
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # (0) edge case
        if not maze or not start or not destination:
            return False

        # (1) initialize a set and queue
        visited = set()
        queue = deque([(start[0], start[1])])    # queue = deque() + queue.append(start)
        
        # (2) traverse the queue when it's not empty
        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            visited.add((curr[0], curr[1]))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                x, y = curr[0], curr[1]
                while 0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[0]) and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
    
                if (x, y) not in visited:
                    queue.append((x, y))  # add this position to be searched from as well

        return False