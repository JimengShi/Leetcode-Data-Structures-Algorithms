# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. 
# Its maximum jump length is 0, which makes it impossible to reach the last index.


class Solution(object):
    def canJump(self, nums):
        # (1) initialize max_i: farest position
        max_i = 0
        
        # (2) tranverse array and update max_i each step (greedy)
        for i in range(0, len(nums)):
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


# nums = [2, 3, 1, 1, 4]
# pos   = 0, 1, 2, 3, 4
#            p
# M     =        M
