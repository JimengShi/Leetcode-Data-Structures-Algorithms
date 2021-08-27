import collections
class Solution:         
    def balancedString(self, s):
        # (0) edge case
        if not s:
            return 0
        
        # (1) count each character of string
        count = collections.Counter(s)           # O(n)
        min_len = n = len(s)
        l = 0
        
        # (2) replace and update the dictionary state
        for r, item in enumerate(s):             # O(n)
            
            # (2.1) find the first window candidate
            count[item] -= 1
            
            # (2.2) minimize the window size   --->  greedy
            while l < n and count['Q'] <= n/4 and count['W'] <= n/4 and count['E'] <= n/4 and count['R'] <= n/4: # (2.2)
                min_len = min(res, r-l+1)
                count[s[l]] += 1
                l += 1
                
        # (3) return the result
        return min_len
    
# Time: O(n)
# Space: O(1)


#   0 1 2 3 4 5 6 7
# ‘[W Q W R Q] Q Q W’     counter = {W:3,Q:4,R:1}      counter = {W:3,Q:4}      counter_balanced = {W:2,Q:2,E:2,R:2}
#   W[Q W R Q] Q Q W’ 
