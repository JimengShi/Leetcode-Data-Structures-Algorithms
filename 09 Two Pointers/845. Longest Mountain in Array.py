# Method 1: two pointers + greedy algorithm
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # (0) edge case
        if len(A) == 0:
            return 0

        # (1) initialize maxlen = 0
        maxlen = 0
        
        # (2) traverse the input list from 1 to len(input)-2
        for i in range(1, len(A)-1):
            if A[i] > A[i+1] and A[i] > A[i-1]:                    # (2.1) A[i] is a peak
                left = i - 1
                right = i + 1
                
                while left > 0 and A[left-1] < A[left]:            # (2.2) greedy to left
                    left -= 1
                    
                while right < len(A)-1 and A[right+1] < A[right]:  # (2.3) greedy to right
                    right += 1
                    
                maxlen = max(maxlen, right-left+1)                 # (2.4) update maxlen

        # (3) return maxlen
        return maxlen

    
# Time: O(N), where N is the length of A.
# Space: O(1).