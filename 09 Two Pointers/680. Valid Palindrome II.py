# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


# Method 1: brute force
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]:
                return True
        return s == s[::-1]

# Time: O(N^2)
# Space: O(N)
    
    
# Method 2: two pointers
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l] + s[l+1:]        # discard the left letter
                tmp2 = s[:r] + s[r+1:]        # discard the right letter
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
            
        return True
    
# Time: O(N)
# Space: O(N)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1 
        while l < r:
            if s[l] != s[r]:     # discard the left or right letteer
                return self.isPalin(s[l+1:r+1]) or self.isPalin(s[l:r])  
            l += 1
            r -= 1
        return True
    
    def isPalin(self, s):
        return s == s[::-1]
    
# Time: O(N)
# Space: O(1)