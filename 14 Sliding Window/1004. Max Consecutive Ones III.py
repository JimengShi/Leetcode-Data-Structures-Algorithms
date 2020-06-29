# Method 1:
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
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
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # (1) initialze left and right pointers and result = 0
        l = res = 0
        
        # (2) traverse the list
        for r in range(len(A)):
            K -= 1 - A[r]                   # (2.1) K = K-1 if A[r] == 0; K will change nothing if A[r] == 1
            if K < 0:                       # (2.2) enter K < 0 --> move left pointer ahead and update K
                while l < r and A[l] == 1:
                    l += 1
                l += 1
                K += 1
            res = max(res, r - l + 1)       # (2.3) update res (window size)
        
        # (3) return result
        return res 
    
    
# Time: O(N), visit every element of array twice, once by left pointer and once by right pointer.
# Space: O(1), We do not use any extra space.