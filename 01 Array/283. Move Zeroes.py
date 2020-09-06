# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

            fast += 1

# Time complexity: O(n). Our fast pointer does not visit the same spot twice.
# Space complexity: O(1). All operations are made in-place


# Algorithm:

# slow pointer: to find the next zero by slow += 1
# fast pointer: to find the next non-zero by fast += 1 and swap nums[fast] and 0 if nums[fast] != 0