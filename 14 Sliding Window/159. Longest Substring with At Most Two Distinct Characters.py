class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # (0) edge case
        if len(s) == 0:
            return 0

        # (1) maintain a dictionary
        d = {}
        l = 0
        maxWindow = 0
        
        # (2) traverse the array
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1       # (2.1) add characters of s into dictionary

            while len(d) > 2:                  # (2.2) deal with len(d) > 2
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1

            maxWindow = max(maxWindow, r-l+1)  # (2.3) update the maxwindow
            
        # (3) return the result maxWindow
        return maxWindow
    
# Time: O(N) where N is a number of characters in the input string.
# Space: O(1) since additional space is used only for a dictionary with at most 3 elements.        
