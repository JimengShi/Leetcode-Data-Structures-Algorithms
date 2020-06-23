class Solution:
    def jump(self, nums: List[int]) -> int:
        # (0) edge case
        if len(nums) < 2:
            return 0 
        
        # (1) initialize max_position and max steps
        max_pos = nums[0]
        max_steps = nums[0]
        
        # (2) traverse the array and trying jump
        jumps = 1
        for i in range(1, len(nums)):    
            if max_steps < i:                    # to reach this point, it needs one more jump
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)
        
        # (3) return result
        return jumps
    
# Time: O(N)
# Space: O(1)