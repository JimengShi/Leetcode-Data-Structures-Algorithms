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
                tmp1 = s[:l] + s[l+1:]
                tmp2 = s[:r] + s[r+1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
            
        return True
    
# Time: O(N)
# Space: O(N)



# if just determine if the given string is a valid palindrome, we can use:

# def isPalindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[- 1 - i]:
#             return False
#     return True

# def isPalindrome(s):
#     return s == s[::-1]