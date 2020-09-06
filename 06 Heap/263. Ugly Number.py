# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

# Example 1:
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2

# Example 3:
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.


class Solution:
    def isUgly(self, num: int) -> bool:
        # (0) edge case
        if num == 0 or num < 0:
            return False
        
        # (1) traverse given_prime
        given_prime = [2, 3, 5]
        for p in given_prime:
            while num % p == 0:
                num //= p
        
        # (2) return result
        if num == 1:
            return True
        else:
            return False
        
# Time: O(3*logn), n is the given number
# Space: O(1)