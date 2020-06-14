class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result, count = 0, 0
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result
    
# Time: O(N), where N is the length of nums. We perform one loop through nums.
# Space: O(1), the space used by result and count.