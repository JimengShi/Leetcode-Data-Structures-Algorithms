# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


# Method 1: Brute Force
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        min_len = n + 1

        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                if cur_sum >= s:
                    min_len = min(min_len, j-i+1)
                    break
        
        return 0 if min_len == n + 1 else min_len

# Time: O(N^2)
# Space: O(1)


# Method 2: Binary Search
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0]                                    # sums[i]: nums[0] 到 nums[i−1] 的元素和, 共 i 个元素
        for i in range(n):                            # nums = [2, 3, 1, 2, 4, 3]
            sums.append(sums[-1] + nums[i])           # sums = [0, 2, 5, 6, 8, 12, 15]
        
        for i in range(1, n+1):
            target = s + sums[i-1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - i + 1)
        
        return 0 if ans == n + 1 else ans

# Time: O(NlogN)
# Space: O(N)
    
    
# Method 3: Sliding window
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