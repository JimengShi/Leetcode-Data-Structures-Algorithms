# Method 1: bruteforce
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product >= k: 
                    break
                count += 1
        return count

# Time: O(n^2)
# Space: O(1)
   
    
    
# Method 2: Sliding Window 
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # (0) edge case
        if k <= 1:
            return 0
        
        # (1) initialize product and points
        prod = 1
        ans = left = 0
        
        # (2) traverse the array to find window and greedy minimize the window size
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1

        # (3) return result
        return ans

# Time: O(N), where N is the length of nums. left can only be incremented at most N times.
# Space: O(1), the space used by prod, left, and ans.