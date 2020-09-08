# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,1,2,3,3],
# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
# It doesn't matter what values are set beyond the returned length.

# Similar with [Problem 26 / 27]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) <= 2: 
            return len(nums)
        
        # (1) initialize two pointers
        prev, curr = 1, 2
        
        # (2) traverse the array to compare nums[curr] with two elements before it
        while curr < len(nums):
            if nums[curr] == nums[prev] and nums[curr] == nums[prev - 1]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        
        # (3) return the length
        return prev + 1
    
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if count < 2 or nums[count - 2] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count
    
    
# Time: O(n)
# Space: O(1)