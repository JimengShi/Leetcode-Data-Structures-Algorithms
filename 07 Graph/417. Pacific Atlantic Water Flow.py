# 从海洋倒着往大陆流，四方向DFS，因为四个方向上的点已经确定可以流出Pacific或Atlantic，只能从低往高流，
# 看看哪些点既能被太平洋的水流到又能被大西洋的水流到
                
# Method 1: dfs with recursion
class Solution:            
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # (0) edge case
        if not matrix or not matrix[0]:
            return []
        
        # (1) initialize two sets
        m, n = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
        
        # (2) dfs function with recursion
        def dfs(visited, x, y):
            visited.add((x, y))
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x,new_y) not in visited and matrix[new_x][new_y] >= matrix[x][y]:
                    dfs(visited, new_x, new_y)
        
        # (3) iterate from left border and right border
        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n-1)

        # (3) iterate from up border and bottom border
        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m-1, j)
            
        # (4) return intersections of two sets where water can flow to both P and A
        return list(p_visited & a_visited)            # return list(p_visited.intersection(a_visited))   
    
# Time: O((m+n)*mn)
# Space: O(m+n)


# Method 2: dfs with stack
class Solution:            
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # (0) edge case
        if not matrix or not matrix[0]:
            return []
        
        # (1) initialize two sets
        m, n = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
        
        # (2) dfs function with stack                    
        def dfs(visited, x, y):
            visited.add((x, y))
            stack = [(x, y)]
            while stack:
                (i, j) = stack.pop()
                for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    new_i, new_j = di+i, dj+j
                    if 0 <=new_i< m and 0 <=new_j< n and (new_i,new_j) not in visited and matrix[new_i][new_j] >= matrix[i][j]:
                        stack.append((new_i, new_j))
                        visited.add((new_i, new_j))
        
        # (3) iterate from left border and right border
        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n-1)

        # (3) iterate from up border and bottom border
        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m-1, j)
            
        # (4) return intersections of two sets where water can flow to both P and A
        return list(p_visited & a_visited)            # return list(p_visited.intersection(a_visited)) 
    
# Time: O((m+n)*mn)
# Space: O(m+n)