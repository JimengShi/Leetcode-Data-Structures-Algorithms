class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # (1) edge case
        size = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            return False

        # (2) traverse given array
        for i, cur_val in enumerate(nums):
            for j in range(i+1, i+k+1):
                if j >= size:                  # avoid index out of boundary
                    break
                if abs(cur_val-nums[j]) <= t   # i != j, |i-j| <= k, |nums[i]-nums[j]| <= t
                    return True
        
        # (3) otherwise return False
        return False
    
# Time: O(N*k), N is the length of array, k is the length of sliding window
# Space: O(1)


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: 
            return False
        
        d = {}
        for i in range(len(nums)):
            m = nums[i] // (t + 1)
            
            if m in d or (m - 1 in d and nums[i] - d[m - 1] <= t) or (m + 1 in d and d[m + 1] - nums[i] <= t):
                return True
            
            d[m] = nums[i]
            if i >= k: 
                del d[nums[i - k] // (t + 1)]
                
        return False
    
# Time: O(N)
# Space: O(N)