# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        # (1) intialize data structure
        ans = [[False] * n for _ in range(n)]
        
        # (2) initialize variable: traversal order: right, down, left, up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = 0                # go the next one in the same direction
        di = 0                   # used to change direction
        
        # (3) start traversing
        for i in range(1, n*n+1):
            ans[r][c] = i

            new_r, new_c = r + dr[di], c + dc[di]
            if 0 <= new_r < n and 0 <= new_c < n and not ans[new_r][new_c]:
                r, c = new_r, new_c
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        # (4) return result        
        return ans

# Time: O(m*n)
# Space: O(m*n)