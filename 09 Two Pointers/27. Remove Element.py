class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # (0) edge case
        if len(nums) == 0: 
            return 0
        
        # (1) initialize two pointers
        prev, curr = -1, 0
        
        # (2) traverse the array to compare nums[curr] with the last element
        while curr < len(nums):
            if nums[curr] == val:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        
        # (3) return the length
        return prev + 1
    
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pre = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                pre += 1
                nums[pre] = nums[i]
        return pre+1
    
    
# Time: O(n)
# Space: O(1)