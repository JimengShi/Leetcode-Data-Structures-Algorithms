class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # (0) edge case
        if len(nums) == 0:
            return False

        # (1) two pointers and while loop
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[l] == nums[r]:   # remove the duplicate
                l += 1
                r -= 1
                
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
    
# Time: O(n)
# Space: O(1)