# Given an integer array nums, find the contiguous subarray within an array 
# (containing at least one number) which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# Method 1: brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result

# Time: O(N^2)
# Space: O(1)


# Method 2: DP
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        res = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            candidates = [curr, max_so_far * curr, min_so_far * curr]
            
            min_so_far = min(candidates)
            max_so_far = max(candidates)

            res = max(max_so_far, res)

        return res
    
# Time: O(N)
# Space: O(1)


# Follow up: return the start and end index of max subarray and the max subarray
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            candidate = [curr, max_so_far * curr, min_so_far * curr]
            max_so_far = max(candidate)
            min_so_far = min(candidate)

            if max_so_far > result:
                result = max_so_far
                end_index = i
                
        j = end_index
        temp = 1
        while temp != result and j >= 0:
            temp *= nums[j]
            j -= 1
            
        print(nums[j+1 : end_index+1]) 
        return result

# Time: O(N)
# Space: O(1)


# if __name__ == "__main__":
#     nums = [2, -5, 3, 1, -4, 0, -10, 2, 8]
#     print(Solution().maxProduct(nums))

# [2, -5, 3, 1, -4]
# 120