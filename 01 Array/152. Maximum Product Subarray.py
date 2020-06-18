class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        imax = nums[0]
        imin = nums[0]
        
        for i in range(1, len(nums)):
            candidates = [nums[i], imax * nums[i], imin * nums[i]]
            imax = max(candidates)
            imin = min(candidates)
            res = max(res, imax)
        
        return res
    
# Time: O(N)
# Space: O(1)