# Input: A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K = 2
# Output: 6, [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
    
# 这道题和通用套路不同的是，我们只需要记录下加入窗口的是0还是1：
# 如果是1，我们什么都不用做
# 如果是0，我们将K减1

# 相应地，我们需要记录移除窗口的是0还是1:
# 如果是1，我们什么都不做
# 如果是0，说明加进来的时候就是1，加进来的时候我们K减去了1，这个时候我们再加1。

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # (1) initialze left and right pointers and result = 0
        l = res = 0
        
        # (2) traverse the list
        for r in range(len(A)):
            K -= 1 - A[r]                   # (2.1) K = K-1 if A[r] == 0; K will change nothing if A[r] == 1
            if K < 0:                       # (2.2) enter K < 0 --> we will more left pointer ahead and update K
                while l < r and A[l] == 1:
                    l += 1
                l += 1
                K += 1
            res = max(res, r - l + 1)       # (2.3) update res (window size)
        
        # (3) return result
        return res 
    
# Time: O(N), we might end up visiting every element of array twice, once by left pointer and once by right pointer.
# Space: O(1), We do not use any extra space.