class Solution(object):
    def canJump(self, nums):
        # (1) initialize max_i: farest position
        max_i = 0
        
        # (2) tranverse array and update max_i
        for i in range(len(nums)):
            if max_i >= i and i+nums[i] > max_i:  # farest >= curr_index and curr_index + jump > farest
                max_i = i + nums[i]               # update farest position

        # (3) return result
        return max_i >= i
    
    
# Time: O(N)
# Space: O(1)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = nums[0]
        
        for i in range(1, n):          # if one could't reach this point
            if max_pos < i:
                return False
            max_pos = max(max_pos, nums[i] + i)

        return False
    
# Time: O(N)
# Space: O(1)