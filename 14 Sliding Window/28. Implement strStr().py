# Method 1: Slice
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
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
        
        # (1) traverse array for moving window
        for i in range(l1 - l2 + 1):
            # find start index and count
            count = 0
            while count < l2 and haystack[i + count] == needle[count]: 
                count += 1
            if count == l2:
                return i
            
        # (2) otherwise return -1
        return -1