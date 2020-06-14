class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # (0) edge case
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return []
        
        # (1) initialize the distance for each cell = positive infinity and a queue to bfs neighbors
        dis = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
                    queue.append((i, j))
                    
        # (2) bfs with a queue consisted of 0's
        while queue:
            x, y = queue.pop(0)
            for (a, b) in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= a < rows and 0 <= b < cols and dis[a][b] > dis[x][y] + 1:
                    dis[a][b] = dis[x][y] + 1
                    queue.append((a, b))
                    
        # (3) return result
        return dis
    
# Time: O(|V|+|E|) = O(r⋅c). O(|V|) = O(|E|) = m * n, so time complexity is O(mn).
# Space: O(|V|+|E|) = O(r⋅c) for queue.