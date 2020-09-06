# Problem: Return if there is a path from A to B.

# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right,
# but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
# You may assume that the borders of the maze are all walls. 
# The start and destination coordinates are represented by row and column indexes.


# Example 1:
# Input 1: a maze represented by a 2D array
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0

# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)

# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.


# Example 2:
# Input 1: a maze represented by a 2D array
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0

# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)

# Output: false

# Explanation: There is no way for the ball to stop at the destination.


# Method 1: recursively dfs
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # (0) edge case
        if not maze or not start or not destination:
            return False
        
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
                    seen.add((x, y))
                    if dfs(x, y):
                        return True
            return False
        
        # (3) return dfs(start coordinate)
        return dfs(start[0], start[1])
    
# Time: O(|V|+|E|). In our maze, O(|V|) = O(|E|) = m * n, so time complexity is O(mn).
# Space: O(|V| + |E|) for seen set.


# Method 1: iteratively dfs with stack
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # (0) edge case
        if not maze or not start or not destination:
            return False

        # (1) initialize a set and queue
        visited = set()
        stack = [(start[0], start[1])]        # queue = deque() + queue.append(start)
        
        # (2) BFS
        while stack:
            curr = stack.pop()
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
                    visited.add((x, y))
                    stack.append((x, y))  # add this position to be searched from as well
        
        # (3) return False otherwise
        return False
    
# Time: O(|V|+|E|). In our maze, O(|V|) = O(|E|) = m * n, so time complexity is O(mn).
# Space: O(|V| + |E|) for visited set.


# Method 2: iteratively dfs with queue  
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # (0) edge case
        if not maze or not start or not destination:
            return False

        # (1) initialize a set and queue
        visited = set()
        queue = deque([(start[0], start[1])])    # queue = deque() + queue.append(start)
        
        # (2) BFS
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
                    visited.add((x, y))
                    queue.append((x, y))  # add this position to be searched from as well
        
        # (3) return False otherwise
        return False
    
# Time: O(|V|+|E|). In our maze, O(|V|) = O(|E|) = m * n, so time complexity is O(mn).
# Space: O(|V| + |E|) for visited set.


# matrix = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0],     ---> False
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0]
# ]
# start = (0, 0)
# dest  = (4, 4)

# matrix = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0],     ---> True
#     [1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0]
# ]
# start = (0, 0)
# dest  = (3, 2)
