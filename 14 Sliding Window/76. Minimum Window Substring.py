class Solution(object):
    def minWindow(self, s, t):
        # (0) edge case
        if not t or not s:
            return ""
        
        # (1) initialize two pointers: left and right and res = ""
        l, r = 0, 0
        lookup = collections.Counter(t)   # lookup = Counter({'A': 1, 'B': 1, 'C': 1})
        min_len = float("inf")            # min_len = +inf
        missing = len(t)
        res = ""
        
        # (2) traverse the string S 
        while r < len(s):    
            # (2.1) look for a window includng string T
            if lookup[s[r]] > 0:  # lookup = {'A': 0, 'B': 0, 'C': 0}
                missing -= 1      # idx= 0 1 2 3 4 5 6 7 8 9 10 11 12
            lookup[s[r]] -= 1     # S = "A D O B E C O D E B A  N  C", T = "A B C"
            r += 1                #      l           r 
            
            # (2.2) already find a window includng string T and optimize the window
            while missing == 0:
                # print the window
                if min_len > r - l:   # lookup = {'A': 0, 'B': 0, 'C': 0}
                    min_len = r - l   # min_len = r - l = 6 - 0 = 6
                    res = s[l:r]      # res = s[l:r] = [A D O B E C]
                
                if lookup[s[l]] == 0: 
                    missing += 1
                lookup[s[l]] += 1
                
                l += 1                # greedy minimize the window size
        
        # return res
        return res
    
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

# Time: O(S + T)
# Space: O(S + T)