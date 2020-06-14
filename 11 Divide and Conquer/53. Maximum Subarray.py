# Method 1: brute force
import sys
class Solution(object):
def maxSubArray(self, nums):
    res = -sys.maxsize
    for i in range(0, len(alist)):
        s = 0
        for j in range (i, len(alist)):
            s += alist[j]
            if s > res:
                res = s
    return res

# Time: O(n^2)
# Space: O(n^2)


# Method 2: Divide and Conquer
class Solution(object):
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
    
    
    def cross_sum(self, nums, left, right, p):
        
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):  # from p to left - 1
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum
    
# Time: O(NlogN)
# Space: O(logN) to keep the recursion stack



# Method 3: Greedy algorithm
class Solution(object):
    def maxSubArray(self, nums):
        result = nums[0]
        local = 0
        for item in nums:
            local = max(local + item, item)
            result = max(result, local)
        return result
    
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# local = -2, 1, -2, 4,  3, 5, 6,  1, 5
#   res = -2, 1,  1, 4,  4, 5, 6,  6, 6

# Time: O(N)
# Space: O(1)


# Method 4: Dynamic Programming
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1] 
            max_sum = max(nums[i], max_sum)

        return max_sum
    
# Time: O(N)
# Space: O(1)