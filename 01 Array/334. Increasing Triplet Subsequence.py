class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = float('inf')
        
        for n in nums:
            if n <= first:      # Find first smallest number
                first = n
            elif n <= second:   # Find second one greater than first element, reset first one if it's smaller
                second = n
            else:
                return True
            
        return False
    
# Time: O(n)
# Space: O(1)


# nums = [1, 10, 3, 5, 2, 9]
# n: 1
# first: 1
# ---------
# n: 10
# second: 10
# ---------
# n: 3
# second: 3
# ---------
# n: 5
# True
