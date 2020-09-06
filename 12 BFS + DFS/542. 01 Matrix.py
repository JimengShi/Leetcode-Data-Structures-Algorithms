# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example 1:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Example 2:
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]


# Method 1: BFS from 0 to 1
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # (0) edge case
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            return []
        
        # (1) initialize the distance for each cell = positive infinity and a queue to bfs neighbors
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dis[i][j] = 0
                    queue.append((i, j))
                    
        # (2) bfs with a queue consisted of 0's
        while queue:
            x, y = queue.pop(0)
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dx, dy in directions:
                a = x + dx
                b = y + dy
                if 0 <= a < rows and 0 <= b < cols and dist[a][b] > dist[x][y] + 1:
                    dist[a][b] = dist[x][y] + 1
                    queue.append((a, b))
                    
        # (3) return result
        return dist
    
# Time: O(|V|+|E|) = O(r⋅c). O(|V|) = O(|E|) = m * n, so time complexity is O(mn).
# Space: O(|V|+|E|) = O(r⋅c) for queue.


# Method 2: DP
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        
        # Calculate the TOP/LEFT adjacents
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 0:
                    top  = matrix[row - 1][col] if row > 0 else float('inf')
                    left = matrix[row][col - 1] if col > 0 else float('inf')
                    
                    matrix[row][col] = min(top, left) + 1
        
        # Calcualte the BOTTOM/RIGHT adjacents
        for row in range(rows)[::-1]:
            for col in range(cols)[::-1]:
                if matrix[row][col] != 0:
                    bottom = matrix[row + 1][col] if row < rows - 1 else float('inf')
                    right  = matrix[row][col + 1] if col < cols - 1 else float('inf')
                    
                    matrix[row][col] = min(matrix[row][col], min(bottom, right) + 1)

        return matrix

# Time: O(mn).
# Space: O(1).