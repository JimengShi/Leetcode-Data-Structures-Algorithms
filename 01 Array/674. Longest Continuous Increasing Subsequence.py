class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # (0) edge case
        if not nums:
            return 0
        
        # (1) initialization
        res, count = 0, 0
        
        # (2) traverse the nums array
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:    # (2.1) increase
                count += 1
                res = max(res, count)
            else:                                # (2.2) decrease
                count = 1
                
        # (3) return result
        return res
    
# Time: O(N), where N is the length of nums. We perform one loop through nums.
# Space: O(1), the space used by res and count.


# [1,3,5,4,7]
# i: 0
# count: 1
# res: 1
# -----------
# i: 1
# count: 2
# res: 2
# -----------
# i: 2
# count: 3
# res: 3
# -----------
# i: 3
# count: 1
# -----------
# i: 4
# count: 2
# res: 3
# -----------
# 3