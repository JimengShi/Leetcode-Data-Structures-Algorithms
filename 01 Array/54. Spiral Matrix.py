# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # (0) edge case
        if not matrix: 
            return []
        
        # (1) initialize data structure
        R, C = len(matrix), len(matrix[0])
        visited = set()
        ans = []
        
        # (2) traversal order: right, down, left, up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = 0                # go the next one in the same direction
        di = 0                   # change direction
        
        # (3) start traversing
        for _ in range(R * C):
            ans.append(matrix[r][c])
            visited.add((r,c))
            new_r, new_c = r + dr[di], c + dc[di]
            if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited:
                r, c = new_r, new_c
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        # (4) return result        
        return ans

# Time: O(m*n)
# Space: O(m*n)