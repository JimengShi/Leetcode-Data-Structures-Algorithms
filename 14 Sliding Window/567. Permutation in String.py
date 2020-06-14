class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # (0) edge case
        l1 = len(s1)         # s1 = "ab" 
        l2 = len(s2)         # s2 = "eidbaooo"
        if l2 < l1:
            return False
        
        # (1) initialize hash value = 0
        s1_hash, s2_hash = 0, 0
        
        # (2) compute the hash value of letters with the window size: len(s1)
        for i in range(l1):                               
            s1_hash += hash(s1[i])
            s2_hash += hash(s2[i])
        if s1_hash == s2_hash: 
            return True
        
        # (3) move the window ahead step by step
        for i in range(l2-l1):
            s2_hash = s2_hash - hash(s2[i]) + hash(s2[i + l1])
            if s1_hash == s2_hash:
                return True
        
        # (4) return result
        return False
    
# Time: O(N) when len(s) == len(p)
# Space: O(1) since we don't use extra space