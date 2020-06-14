# Method 1: sliding window with hashing
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # (0) edge case
        l1, l2 = len(p), len(s)
        if l2 < l1:         
            return
        
        # (1) initialize an empty list for result
        res = []
        p_hash, s_hash = 0, 0
        
        # (2) compute the hash value of the first l1 elments (window size) in string p and string s
        for i in range(l1):                               
            p_hash += hash(p[i])
            s_hash += hash(s[i])
        if p_hash == s_hash:
            res.append(0)
        
        # (3) move the window(string p) in string s ahead step by step
        for i in range(l2-l1):
            s_hash = s_hash - hash(s[i]) + hash(s[i + l1])
            if s_hash == p_hash:
                res.append(i+1)
        
        # (4) return result
        return res
    
# p = "a b c"                   3
# s = "c b a e b a b a c d"     10
# idx: 0 1 2 3 4 5 6 7 8 9
    
# Time: O(N) when len(s) == len(p)
# Space: O(N) when string p has only one letter (let's say x) and all letters in string p are x