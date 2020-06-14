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
    
    
# [False, False, None, None, None, None, None, None, None, None]
# 2
# 1: [False, False, True, None, None, None, None, None, None, None]
# 2: [False, False, True, None, False, None, None, None, None, None]
# 2: [False, False, True, None, False, None, False, None, None, None]
# 2: [False, False, True, None, False, None, False, None, False, None]
# -----------------
# 3
# 1: [False, False, True, True, False, None, False, None, False, None]
# 2: [False, False, True, True, False, None, False, None, False, None]
# 2: [False, False, True, True, False, None, False, None, False, False]
# -----------------
# 4
# 5
# 1: [False, False, True, True, False, True, False, None, False, False]
# -----------------
# 6
# 7
# 1: [False, False, True, True, False, True, False, True, False, False]
# -----------------
# 8
# 9
    
    
    
    
    