# Given an array nums of n integers and an integer target, are there elements a, b, c, 
# and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# Example: Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]



class Solution:
    def fourSum(self, nums, target):
        # (0) edge case
        n = len(nums)
        if n < 4: 
            return []
        
        # (1) sort and initialize
        nums.sort()
        res = []
        
        # (2) traverse array, trying two pointers
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:                        # avoid duplicate
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:  # min sum of nums.sort array > 0
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:  # max sum of nums.sort array < 0
                continue
                
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res
    
# Time: O(N^3)
# Space: O(N)


class Solution(object):
    def fourSum(self, nums, target):
        
        nums.sort()
        li = []
        
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if  s == target and [nums[i], nums[j], nums[l], nums[r]] not in li:
                        li.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while (l < r) and (nums[l] == nums[l-1]):
                            l += 1
                        while (l < r) and (nums[r] == nums[r+1]):
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                            r -= 1

        return li

# Time: O(N^3)
# Space: O(N)
