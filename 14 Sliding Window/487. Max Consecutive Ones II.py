class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        return self.longestOnes(nums, 1)

    def longestOnes(self, A, K):
        # (1) initialze left and right pointers and result = 0
        l = res = 0
        
        # (2) traverse the list
        for r in range(len(A)):
            K -= 1 - A[r]                   # (2.1) K = K-1 if A[r] == 0; K will change nothing if A[r] != 0
            if K < 0:                       # (2.2) enter K < 0 --> we will more left pointer ahead and update K
                while l < r and A[l] == 1:
                    l += 1
                l += 1
                K += 1
            res = max(res, r - l + 1)       # (2.3) update res
        
        # (3) return result
        return res 

# Time: O(n)
# Space: O(1)


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