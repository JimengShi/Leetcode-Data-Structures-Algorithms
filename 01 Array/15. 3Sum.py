# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# Example: Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        # (0) pre-preparation: sort
        nums.sort()
        
        # (1) initialize
        res = []
        length = len(nums)
        
        # (2) traverse array to fix one number
        for i in range(length):
            # (2.1) check in advance
            if nums[i] > 0:                     # fixed value > 0, don't have to compute later numbers who must > 0
                break
            if i > 0 and nums[i] == nums[i-1]:  # avoid duplicate, eg: [-4,-1,-1,0,1,2], compute 1st -1, neglect 2nd
                continue
            
            # (2.2) find the left two numbers from the right of fixed number
            l = i + 1
            r = length - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if  s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        
        # (3) return result
        return res
    
# Time: O(N^2)
# Space: O(N)