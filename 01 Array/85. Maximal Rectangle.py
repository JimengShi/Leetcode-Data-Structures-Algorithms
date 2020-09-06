# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        heights = [0] * len(matrix[0])
        res = 0
        for row in matrix:
            for i, val in enumerate(row):
                heights[i] = heights[i] + 1 if val == '1' else 0
            maxA = self.calArea(heights)
            res = max(res, maxA)
        return res

    def calArea(self, heights):
        heights = [0] + heights + [0]
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                maxArea = max(maxArea, (i-stack[-1]-1)*heights[j])
            stack.append(i)
        return maxArea

# Time: O(m*n)
# Space: O(m*n)