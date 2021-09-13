## Q53, 209, 560, 930

# Method 1: brute force
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        for i in range(0, len(nums)):
            temp_sum = 0
            for j in range(i, len(nums)):
                temp_sum += nums[j]
                max_sum = max(max_sum, temp_sum)

        return max_sum

# Time: O(n^2)
# Space: O(n^2)
         
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, arr, l, r):
        if l == r:
            return arr[l]
        mid = (l+r) // 2
        left_max = self.helper(arr, l, mid)
        right_max = self.helper(arr, mid+1, r)
        cross_max = self.cross(arr, l, r, mid)
        return max(left_max, right_max, cross_max)
    
    def cross(self, li, l, r, mid):
        if l == r:
            return li[l]
        left_sub = float('-inf')
        left_cur = 0
        for i in range(mid, l-1, -1):
            left_cur += li[i]
            left_sub = max(left_sub, left_cur)
            
        right_sub = float('-inf')
        right_cur = 0
        for j in range(mid+1, r+1):
            right_cur += li[j]
            right_sub = max(right_sub, right_cur)
            
        return left_sub + right_sub

    
# Method 2: Divide and Conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:      
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, left, right):
        """
        @func: It's used to compute the maximun sum of subarray
        @given: left and right boundary
        """
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
            
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid+1, right)
        cross_sum = self.cross_sum(nums, left, right, mid)
        
        return max(left_sum, right_sum, cross_sum)
    
    
    def cross_sum(self, nums, left, right, mid):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(mid, left-1, -1):  # from mid to left-1 (reverse order)
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for j in range(mid+1, right+1):
            curr_sum += nums[j]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum
    
# Time: O(NlogN)
# Space: O(logN) to keep the recursion stack



# Method 3: Greedy algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        cur_sum = max(cur_sum + num, num)    # accumulative addition is bigger or cur num is bigger
        """
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum + num, num)    # cur_sum = cur_sum + num only if cur_sum > 0
            max_sum = max(max_sum, cur_sum)
        return max_sum

    
#     nums =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
#  cur_sum = -2, 1, -2, 4,  3, 5, 6,  1, 5
#  max_sum = -2, 1,  1, 4,  4, 5, 6,  6, 6

# Time: O(N)
# Space: O(1)


# Method 4: Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] > 0:                   # nums[i]: record the curr_sum by now
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])

        return max_sum
    
# Time: O(N)
# Space: O(1)


# nums    = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums[i] =  -2, 1, -3, 4,  3, 5, 6,  1, 5
#   max_sum   =  -2, 1,  1, 4,  4, 5, 6,  6, 6



# [TRANSFORMATION]
# Find the start and end index of the maximum subarray
class Solution:
    def maxSubArray(self, nums):
        dp = nums.copy()
        res = dp[0]
        
        for i in range(1, len(dp)):
            if dp[i-1] > 0:                   # nums[i]: record the curr_sum by now
                dp[i] += dp[i-1]
                if dp[i] > res:
                    res = dp[i]
                    end_index = i
        
        j = end_index
        temp = 0
        while temp != res and j >= 0:
            temp += nums[j]
            j -= 1
            
        print(nums[j+1 : end_index+1]) 
        return res
    
# index =  0, 1,  2,[3,  4, 5, 6,] 7, 8     
# nums  = -2, 1, -3, 4, -1, 2, 1, -5, 4
#  dp   = -2, 1, -3,[4, -1, 2, 1,]-5, 4
# dp[i] = -2, 1, -3,[4,  3, 5, 6,] 1, 5
# 
#   res   =  -2, 1,  1, 4,  4, 5, 6,  6, 6
