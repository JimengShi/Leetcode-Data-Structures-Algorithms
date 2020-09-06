# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution:
    def jump(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) < 2:
            return 0
        
        # (1) initialize max_position and max steps
        max_pos = nums[0]
        max_steps = nums[0]                      # max number of steps inside this jump
        jumps = 1
        
        # (2) traverse the array and trying jump
        for i in range(1, len(nums)):    
            if max_steps < i:                    # to reach this point, it needs one more jump
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)
        
        # (3) return result
        return jumps

# Time: O(N)
# Space: O(1)

# Initiate max position that one could reach starting from curr index i or before: max_pos = nums[0].

# Initiate max position reachable during the current jump: max_steps = nums[0].

# Initiate number of steps: at least one, if array has more than 1 cell.

# Iterate over number of elements in the input array:

#       If max_step < i, one needs one more jump: jumps += 1. 
#       To minimize the number of jumps, choose the longest possible one: max_steps = max_pos.
#       Update max_pos = max(max_pos, i + nums[i]).

# Return the number of jumps.