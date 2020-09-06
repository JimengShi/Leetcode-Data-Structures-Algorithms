# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image.

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
# and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally 
# to the starting pixel of the same color as the starting pixel, 
# plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. 
# Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example 1:

# Input: sr = 1, sc = 1, newColor = 2
# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]

# Output: [[2,2,2],
#          [2,2,0],
#          [2,0,1]]

# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.


# Method 1: DFS without visited set
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # (0) edge case
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        # (1) initialize data structure
        R, C = len(image), len(image[0])
        
        # (2) dfs function
        def dfs(x, y):
            image[x][y] = newColor

            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            for dx, dy in directions:
                new_r = x + dx
                new_c = y + dy
                if 0 <= new_r < R and 0 <= new_c < C and image[new_r][new_c] == base_color:
                    dfs(new_r, new_c)
        
        # (3) call dfs function and return result
        dfs(sr, sc)
        return image
    
# Time: O(N), where N is the number of pixels in the image. We might process every pixel.
# Space: O(N), the size of the implicit call stack when calling dfs.


# Method 2: DFS with only stack
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        # (0) edge case
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        # (1) initialize data structure
        R, C = len(image), len(image[0])
        stack = [(sr, sc)]
        
        # (2) dfs
        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= r+dr < R and 0 <= c+dc < C and image[r+dr][c+dc] == base_color:
                    stack.append((new_r, new_c))
                    
        # (3) return result            
        return image
    
# Time: O(N), where N is the number of pixels in the image. We might process every pixel.
# Space: O(N), the size of the implicit call stack when calling dfs.