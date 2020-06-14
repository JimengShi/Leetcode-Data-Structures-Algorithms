# Method 1: Brute force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                ans = max(ans, min(height[i], height[j]) * (j - i))
        return ans

# Time: O(N^2)
# Space: O(1)


# Method 2: two pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # (1) initialize the ans and two pointers
        ans = 0
        left = 0
        right = len(height) - 1
        
        # (2) compute the answer area as big as possible (greedy)
        while left < right:
            ans = max(ans, (right-left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        # (3) return the final answer
        return ans
    
    
# Time: O(n). Single pass.
# Space: O(1). Constant space is used.
    
# input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
# index:  0  1  2  3  4  5  6  7  8
#            l                    r