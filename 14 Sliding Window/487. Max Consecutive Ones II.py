# Method 1: brute force
# Check every possible consecutive sequence
# Count how many 0's are in each sequence
# If sequence has one or fewer 0's, check if that's the longest consecutive sequence of 1's.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        len_longest_sequence = 0
        for l in range(len(nums)):
            num_zeroes = 0
            for r in range(l, len(nums)):      # check every consecutive sequence
                if num_zeroes == 2:
                    break
                if nums[r] == 0:               # count how many 0's
                    num_zeroes += 1
                if num_zeroes <= 1:            # update answer if it's valid
                    len_longest_sequence = max(len_longest_sequence, r-l+1)
        return len_longest_sequence
    
    
    
# Method 2: sliding window
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.findMaxConsecutiveOnesWithKTimes(nums, 1)
    
    def findMaxConsecutiveOnesWithKTimes(self, A, k):
        max_num = 0
        l = 0
        count = 0
        
        for r in range(len(A)):
            if A[r] == 0:
                count += 1
                
            while count > k:
                if A[l] == 0:
                    count -= 1
                l += 1
            max_num = max(max_num, r-l+1)
            
        return max_num
    
# Time: O(N), visit every element of array twice, once by left pointer and once by right pointer.
# Space: O(1), We do not use any extra space.
