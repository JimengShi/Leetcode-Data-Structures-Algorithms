class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) == 0: 
            return 0
        
        # (1) initialize two pointers
        prev, curr = 0, 1
        
        # (2) traverse the array to compare nums[curr] with the last element
        while curr < len(nums):
            if nums[curr] == nums[prev]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        
        # (3) return the length
        return prev + 1
    
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) == 0:
            return 0
        
        # (1) initialize two pointers i and j 
        # (1) i keeps length and the position, j traverses array
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        # (2) return the length i+1 since i is index
        return i + 1
    
# Time: O(n)
# Space: O(1)        