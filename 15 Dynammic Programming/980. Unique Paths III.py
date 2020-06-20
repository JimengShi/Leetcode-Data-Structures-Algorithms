class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: 
                    todo += 1
                if val == 1: 
                    sr, sc = r, c
                if val == 2: 
                    tr, tc = r, c

        self.ans = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: 
                return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans
    
# Time: O(4^R∗C), where R, CR,C are the number of rows and columns in the grid. (We can find tighter bounds, but such a bound is beyond the scope of this article.)
# Space: O(R∗C).