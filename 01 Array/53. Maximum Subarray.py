# Given an integer array nums, find the contiguous subarray (containing at least one number)
#  which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# (1)If you have figured out the O(n) solution, try coding another solution using the divide and conquer 
# approach, which is more subtle.
# (2) return the start and end index of max subarray and the max subarray


# Method 1: brute force
import sys
class Solution(object):
    def maxSubArray(self, nums):
        res = -sys.maxsize
        for i in range(0, len(nums)):
            s = 0
            for j in range (i, len(nums)):
                s += nums[j]
                res = max(res, s)

        return res

# Time: O(n^2)
# Space: O(n^2)


# Method 2: Divide and Conquer
class Solution(object):
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
            
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid+1, right)
        cross_sum = self.cross_sum(nums, left, right, mid)
        
        return max(left_sum, right_sum, cross_sum)
    
    
    def cross_sum(self, nums, left, right, mid):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(mid, left-1, -1):  # from mid to left-1
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for j in range(mid+1, right+1):
            curr_sum += nums[j]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum
    
# Time: O(NlogN)
# Space: O(logN) to keep the recursion stack



# Method 3: Greedy algorithm
class Solution(object):
    def maxSubArray(self, nums):
        res = nums[0]
        curr_sum = 0
        for item in nums:
            curr_sum = max(curr_sum + item, item)  # curr_sum = curr_sum + item only if curr_sum > 0
            res = max(res, curr_sum)
        return res
    
#     nums =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# curr_sum = -2, 1, -2, 4,  3, 5, 6,  1, 5  --> to see 'accumulate add' or 'restart from curr item' 
#   result = -2, 1,  1, 4,  4, 5, 6,  6, 6

# Time: O(N)
# Space: O(1)


# Method 4: Dynamic Programming
class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:                   # nums[i]: record the curr_sum by now
                nums[i] += nums[i-1]
            res = max(res, nums[i])

        return res
    
# Time: O(N)
# Space: O(1)


# nums    = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums[i] =  -2, 1, -3, 4,  3, 5, 6,  1, 5
#   res   =  -2, 1,  1, 4,  4, 5, 6,  6, 6



# [TRANSFORMATION]
# Find the start and end index of the maximum subarray
class Solution:
    def maxSubArray(self, nums):
        dp = nums.copy()
        
        res = dp[0]
        
        for i in range(1, len(dp)):
            if dp[i-1] > 0:                   # nums[i]: record the curr_sum by now
                dp[i] += dp[i-1]
                if dp[i] > res:
                    res = dp[i]
                    end_index = i
        
        j = end_index
        temp = 0
        while temp != res and j >= 0:
            temp += nums[j]
            j -= 1
            
        print(nums[j+1 : end_index+1]) 
        return res

# Time: O(N)
# Space: O(1)

# if __name__ == "__main__":
#     nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     print(Solution().maxSubArray(nums))

# [4, -1, 2, 1]
# 6