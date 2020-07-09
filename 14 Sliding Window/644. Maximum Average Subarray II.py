class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float('-inf')
        for j in range(k, len(nums)):
            ans = max(self.helper(nums, j) / j, ans)
        return ans
        
    def helper(self, nums, k): 
        # (1) initialize moving_sum and calculate the sum of first k elements
        moving_sum = 0.0
        for i in range(k):
            moving_sum += nums[i]
        
        # (2) calculate the moving_sum by sliding window
        res = moving_sum
        for i in range(k, len(nums)):
            moving_sum += nums[i] - nums[i - k]
            res = max(res, moving_sum)
            
        # (3) return result
        return res
    
# Time: O(N^2)
# Space: O(1)