class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        # (0) edge case
        m, n = len(Grid), len(Grid[0])
        if Grid[0][0] == 1:
            return 0
        Grid[0][0] = 1
        
        # (1) Filling the values for the first column and the first row
        for i in range(1, m):
            Grid[i][0] = int(Grid[i][0] == 0 and Grid[i-1][0] == 1) 
        for j in range(1, n):
            Grid[0][j] = int(Grid[0][j] == 0 and Grid[0][j-1] == 1)
            
        # (2) reaching cell[i][j] = cell[i-1][j] + cell[i][j-1], i.e. From above and left.
        for i in range(1, m):
            for j in range(1, n):
                if Grid[i][j] == 0:
                    Grid[i][j] = Grid[i-1][j] + Grid[i][j-1]
                else:
                    Grid[i][j] = 0

        # (3) Return value stored in rightmost bottommost cell
        return Grid[m-1][n-1]

    
# Time: O(M×N). The rectangular grid given to us is of size M×N and we process each cell just once.
# Space: O(1). We are utilizing the obstacleGrid as the DP array. Hence, no extra space.