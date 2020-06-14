class Solution:
    def minSubArrayLen(self, s, nums):
        # (1) initialze l pointer, cur_sum, and ans: minimal length, assume it = len(nums)+1
        l = 0
        cur_sum = 0
        ans = len(nums) + 1               
        
        # (2) traverse the nums and update the cur_num
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= s:
                ans = min(ans, r - l + 1) # (2.1) update ans when cur_sum >= s, window is good
                cur_sum -= nums[l]        # (2.2) remove the leftmost element, greedy minimize
                l += 1                    # (2.3) update l = l + 1, greedy minimize
        
        # (3) return 0 or the minimal length
        return 0 if ans == len(nums) + 1 else ans
    
# Time: O(N)
# Space: O(1)


class Solution:
    def minSubArrayLen(self, s, nums):
        # (1) initialze l pointer, cur_sum, and ans: minimal length, assume it = len(nums)+1
        l = 0
        cur_sum = 0
        ans = float("inf")              
        
        # (2) traverse the nums and update the cur_num
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= s:
                ans = min(ans, r - l + 1) # (2.1) update ans when cur_sum >= s
                cur_sum -= nums[l]        # (2.2) remove the leftmost element
                l += 1                    # (2.3) update l = l + 1
        
        # (3) return 0 or the minimal length
        if ans > len(nums):
            return 0
        return res
    
# Time: O(N)
# Space: O(1)