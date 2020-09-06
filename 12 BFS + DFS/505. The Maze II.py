import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # (0) edge case
        if not maze or len(maze[0]) == 0:
            return -1
        
        # (1) initialize data structure
        m, n = len(maze), len(maze[0])
        min_heap = [(0, start[0], start[1])]
        visited = set()
        
        # (2) pop and append heap
        while min_heap:
            cur_dist, x, y = heapq.heappop(min_heap)
            if [x, y] == destination:
                return cur_dist
            visited.add((x, y))
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x = x
                next_y = y
                
                temp = 0
                while 0 <= next_x + dx < m and 0 <= next_y + dy < n and maze[next_x + dx][next_y + dy] == 0:
                    next_x += dx
                    next_y += dy
                    temp += 1
                    
                if (next_x, next_y) not in visited:
                    heapq.heappush(min_heap, (cur_dist + temp, next_x, next_y))
        
        return -1
    
# Time: O(m∗n∗max(m,n)). m and n refers to the number of rows and columns of the maze, for every current node chosen, we can travel upto a maximum depth of max(m,n) in any direction.
# Space: O(mn). distance array of size m*n is used.