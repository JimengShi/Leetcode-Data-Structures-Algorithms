import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # (0) edge case
        if not s:
            return 0
        
        # (1) initialize a dictionary and a valid function
        d = {}
        l = 0
        result = 0
        
        def isValid():
            return len(d) <= k
        
        # (2) traverse the array
        for r, char in enumerate(s):
            d[s[r]] = d.get(s[r], 0) + 1      # (2.1) add characters of s into dictionary

            while not isValid():              # (2.2) deal with len(d) > 2
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1

            result = max(result, r - l + 1)   # (2.3) update the maxwindow

        # (3) return the result maxWindow
        return result
    
# Time: O(N) where N is a number of characters in the input string.
# Space: O(k) since additional space is used only for a hashmap with at most k + 1 elements.