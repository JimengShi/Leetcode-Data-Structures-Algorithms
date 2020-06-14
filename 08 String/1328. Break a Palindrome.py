class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # case 1: replace non-'a' by 'a' at the first half of the sting, like 'abccba'
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        # case 2: replace the last one by 'b' when all 'a' in first half of string, like 'aaabaaa'
        if len(palindrome) > 1:
            return palindrome[:-1] + 'b'
        
        # case: len(palindrome) == 1 or 0
        return ''
    
# Time: O(N)
# Space: O(N) to keep output