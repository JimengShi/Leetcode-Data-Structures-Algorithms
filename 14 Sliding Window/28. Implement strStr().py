# Method 1: Slice
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2 = len(needle), len(haystack)

        for i in range(l1-l2+1):
            if haystack[i:i+l2] == needle:
                return i
                break
        return -1
    
# Time: O((N−L)L), where N is a length of haystack and L is a length of needle. We compute a substring of length L in a loop, which is executed (N - L) times.
# Space: O(1).



# Method 2: sliding window
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # (0) edge caese
        l1, l2 = len(haystack), len(needle)
        if l1 < l2: 
            return -1
        
        # (1) traverse array for moving window, i is used for traversing haystack, j is used for traversing needle.
        for i in range(l1-l2+1):
            temp_index = i
            j = 0
            while i < l1 and j < l2 and haystack[i]==needle[j]: 
                i += 1
                j += 1
            if j == l2:
                return temp_index
            
        # (2) otherwise return -1
        return -1
