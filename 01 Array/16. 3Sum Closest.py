# Given an array nums of n integers and an integer target, 
# find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.


# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2

# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = 0
        diff = float('inf')
        
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s == target:
                    return target
                elif s > target:
                    end -= 1
                else:
                    start += 1
                    
                if abs(target - s) < diff:
                    diff = abs(target - s)
                    ans = s
        return ans
    
# Time: O(N^2)
# Space: O(N)