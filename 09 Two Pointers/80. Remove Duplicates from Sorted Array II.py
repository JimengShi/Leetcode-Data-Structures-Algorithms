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