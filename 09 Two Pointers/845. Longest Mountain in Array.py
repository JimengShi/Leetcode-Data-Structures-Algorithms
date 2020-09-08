# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 
# Return 0 if there is no mountain.

# Example 1:
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

# Example 2:
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.

# Note:
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# Follow up:

# Can you solve it using only one pass?
# Can you solve it in O(1) space?

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