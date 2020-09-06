# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
# find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10

# Method 1: brute force
class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_area = 0
        for i in range(len(height)):
            min_height = float('inf')
            for j in range(i, len(height)):
                min_height = min(min_height, height[j])         # height: height[j]
                max_area = max(max_area, min_height*(j-i+1))    # width: j-i+1
        return max_area
    
# Time: O(N^2)
# Space: O(1)


# Method 2: stack to record position
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights = [0] + heights + [0]
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:     # i: R index with smaller height
                curr = stack.pop()
                ans = max(ans, (i-stack[-1]-1)*heights[curr])
            stack.append(i)                    # append it into stack if heights[i] > heights[stack[-1]]
        return ans

# Time: O(n). n numbers are pushed and popped.
# Space: O(n). Stack is used.