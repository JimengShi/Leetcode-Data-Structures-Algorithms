# Two Pointers
# Time: O(n), in length n of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.
# Space: O(1). No extra space required, at all.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # (0) edge case
        if not s:
            return True
        
        # (1) initialize two pointers, head and tail
        i, j = 0, len(s) - 1
        
        # (2) traverse from start and tail at the same time, .isalnum() is to check if it's a letter
        while i < j:
            while i < j and not s[i].isalnum():   # (2.1) move i one step to right if it's not a letter
                i += 1
            while i < j and not s[j].isalnum():   # (2.2) move j one step to left if it's not a letter
                j -= 1
                
            if s[i].lower() != s[j].lower():      # (2.3) letter from head != letter from tail
                return False
            i += 1                                # (2.4) letter from head = letter from tail
            j -= 1

        # (3) return True when i = j, which means we jump out of the 'while' loop
        return True

# if s[i] != s[- 1 - i]
# if s = s[::-1]
