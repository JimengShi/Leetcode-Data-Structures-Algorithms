'''
Two pointers.
1. max[seen]: the number of the most frequent chars within s[left:right+1]
2. Move left pointer right when right - left + 1 - m > k, because more than k chars need to be replaced to make s[left:right+1] is repeating of single char.

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # (0) edge case
        if not s:
            return 0
        
        # (1) initialize a seen list to record letters and two pointers
        seen = [0] * 26
        res, left = 0, 0
        
        # (2) traverse the string s
        for right in range(len(s)):
            seen[ord(s[left])-ord('A')] += 1         # (2.1) record all letters in string
            
            # window size - no. of most frequent element = how many elements needed to be replaced (5-3=2 )
            while right - left + 1 - max(seen) > k:  
                seen[ord(s[left])-ord('A')] -= 1     # (2.2) shrink window
                left += 1
                
            res = max(res, right - left + 1)         # (2.3) update result
        
        # (3) return result
        return res
    
# Time: O(n)
# Space: O(1)