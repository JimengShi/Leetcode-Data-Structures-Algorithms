# Count the number of prime numbers less than a non-negative number, n.

# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n: int) -> int:
        # (0) edge case
        if n < 3: 
            return 0            # n = 1, 2, no prime number less than n at the moment
        
        # (1) create a list to mark numbers less than n
        nums = [None] * n 
        nums[0] = False         # except 0 and 1, because 0 and 1 are not prime numbers
        nums[1] = False
        
        # (2) traverse the nums list
        for i in range(2, n):
            if nums[i] == None:
                nums[i] = True
                
                for j in range(i+i, n, i):
                    nums[j] = False
                    
        # (3) return result: sum(nums) means return the number of nums[True]
        return sum(nums)

# Time: O(n^2)
# Space: o(1)
    
#    0,     1,    2,    3,    4,    5,    6,    7,    8,    9   
# [False, False, None, None, None, None, None, None, None, None]
#                 i
# i = 2
# [False, False, True, None, None, None, None, None, None, None]
# [False, False, True, None, False, None, False, None, False, None]
# -----------------
# i = 3
# [False, False, True, True, False, None, False, None, False, None]
# [False, False, True, True, False, None, False, None, False, None]
# -----------------
# i = 4
# i = 5
# [False, False, True, True, False, True, False, None, False, False]
# -----------------
# 6
# 7
# [False, False, True, True, False, True, False, True, False, False]
# -----------------
# 8
# 9