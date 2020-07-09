# Method 1:
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        return self.longestOnes(nums, 1)

    def longestOnes(self, A, K):
        # (0) edge case
        if not A:
            return 0
        
        # (1) initialize two points and count
        l = 0
        res = 0
        count = 0
        
        # (2) traverse
        for r in range(len(A)):
            if A[r] == 0:          # (2.1) count number of 0
                count += 1
                
            while count > K:       # (2.2) shrink window when count > K
                if A[l] == 0:
                    count -= 1
                l += 1
                
            res = max(res, r-l+1)  # (2.3) update result
        
        # (3) return result
        return res
    
# Time: O(N), visit every element of array twice, once by left pointer and once by right pointer.
# Space: O(1), We do not use any extra space.


# Method 2:
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        # (1) initialize the pre (count consecutive 1's before 0)
        # (1) initialize the curr (count consecutive 1's after 0)
        pre, curr = -1, 0
        max_len = 0
        
        # (2) traverse the nums
        for num in nums:
            if num == 0:
                pre = curr
                curr = 0
            else:
                curr += 1
                
            max_len = max(max_len, pre + 1 + curr )
        
        # (3) return the result
        return max_len
    
# Time: O(n)
# Space: O(1)