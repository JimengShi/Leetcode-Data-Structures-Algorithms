# Given an array of n integers nums and a target, 
# find the number of index triplets i, j, k with 0 <= i < j < k < n 
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example:

# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 
# Explanation: Because there are two triplets which sums are less than 2:
#              [-2,0,1]
#              [-2,0,3]


class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res = 0
        if len(nums) < 3:
            return res
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums < target:                    
                    res += k - j 
                    j += 1 
                elif sums >= target:
                    k -= 1
        return res
    
    
# Time: O(N^2)
# Space: O(N)