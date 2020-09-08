# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false


# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # (0) edge case
        if not s:
            return True
        
        # (1) initialize two pointers, head and tail
        i, j = 0, len(s)-1
        
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


# Time: O(N)
# Space: O(1)