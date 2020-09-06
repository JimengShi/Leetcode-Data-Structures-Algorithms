# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].


# Method 1: Brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

# Time: O(N^2)
# Space: O(1)


# Method 2: Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 not in d:
                d[num1] = i
            else:
                return d[num2], i

# Time: O(N)
# Space: O(1)