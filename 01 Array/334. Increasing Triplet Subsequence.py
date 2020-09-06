# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Example 1:
# Input: [1,2,3,4,5]
# Output: true

# Example 2:
# Input: [5,4,3,2,1]
# Output: false


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')
        
        for num in nums:
            if num <= first:      # Find first smallest number
                first = num

            elif num <= second:   # Find second one greater than first element, reset first one if it's smaller
                second = num
            
            else:
                return True
            
        return False
    
# Time: O(n)
# Space: O(1)


# nums = [1, 10, 3, 5, 2, 9]
# num: 1
# first: 1
# ---------
# num: 10
# second: 10
# ---------
# num: 3
# second: 3
# ---------
# num: 5
# True