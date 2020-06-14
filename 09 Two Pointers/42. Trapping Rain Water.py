# Method 1: Brute force
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(1,len(height)-1): 
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            potential = min(max_left, max_right) - height[i]
            ans += max(0, potential) 
        return ans

# Time: O(n^2)
# Space: O(1)


# Method 2: Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        # (0) edge case
        if not height:
            return 0
        
        # (1) initialize the answer and two pointers
        left = 0
        right = len(height) - 1
        maxleft = height[0]
        maxright = height[len(height) - 1]
        ans = 0

        # (2) traverse the height array from left and right at the same time
        while left <= right:
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        
        # (3) return the result
        return ans
    
# Time: O(n)
# Space: O(1)