# Method 1: Greedy algorithm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # import sys
        # result = -sys.maxsize
        result = nums[0]
        local = 0
        for item in nums:
            local = max(local + item, item)
            result = max(result, local)
        return result
    
# Time: O(N)
# Space: O(1)


# Method 2: Divide and Conquer
class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)
    
# Time: O(NlogN)
# Space: O(logN)