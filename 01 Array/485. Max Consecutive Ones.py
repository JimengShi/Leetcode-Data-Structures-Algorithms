class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # (0) initialize cur_count and max_count
        cur_count = max_count = 0
        
        # (1) traverse the nums
        for num in nums:
            if num == 1:        
                cur_count += 1                         # (1.1) Increase cur_count if num is 1
            else:                                      
                max_count = max(max_count, cur_count)  # (1.2) Find the max_count till now.
                cur_count = 0                          # (1.3) reset cur_count = 0 for num is 1
        
        # (2) return result
        return max(max_count, cur_count)
    
# Time: O(N)
# Space: O(1)