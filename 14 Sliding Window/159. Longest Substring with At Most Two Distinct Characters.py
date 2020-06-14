# Method 1: sliding window 1
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # (0) edge case
        if len(s) == 0:
            return 0

        # (1) maintain a dictionary to hold charaters of string s
        dct = {}
        l = 0
        maxWindow = 0
        count = 0
        
        # (2) traverse the array
        for r in range(len(s)):
            dct[s[r]] = dct.get(s[r], 0) + 1 # (2.1) add characters of s into dictionary

            if dct[s[r]] == 1:               # (2.2) count when dct[char] == 1
                count += 1

            while count > 2:                 # (2.3) greedily control length of dictionary
                dct[s[l]] -= 1               # (2.3.1) delete the leftmost letter
                if dct[s[l]] == 0:
                    count -= 1
                    del dct[s[l]]
                l += 1                       # (2.3.2) update the left pointer

            maxWindow = max(maxWindow, r - l + 1) # (2.4) update the maxwindow
            
        # (3) return the result maxWindow
        return maxWindow
    
# Time: O(N) where N is a number of characters in the input string.
# Space: O(1) since additional space is used only for a dictionary with at most 3 elements.


# Method 2: sliding window 2
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # (0) edge case
        if len(s) == 0:
            return 0

        # (1) maintain a dictionary to hold charaters of string s
        d = {}
        l = 0
        maxWindow = 0
        
        def isValid():
            return len(d) <= 2
        
        # (2) traverse the array
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1       # (2.1) add characters of s into dictionary

            while not isValid():               # (2.2) deal with len(d) > 2
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1

            maxWindow = max(maxWindow, r - l + 1) # (2.3) update the maxwindow
            
        # (3) return the result maxWindow
        return maxWindow
    
# Time: O(N) where N is a number of characters in the input string.
# Space: O(1) since additional space is used only for a dictionary with at most 3 elements.        
