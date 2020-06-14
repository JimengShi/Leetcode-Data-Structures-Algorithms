# Method 1: set
class Solution:
    def wordPattern(self, P: str, S: str) -> bool:
        # (1) split string s and zip P and S one by one
        S = S.split()
        if len(P) != len(S):
            return False
        
        # (2) check length and return result
        return len(set(zip(P, S))) == len(set(P)) == len(set(S))

# Time: O(N)
# Space: O(N)


# Method 2: dictionary
class Solution:
    def wordPattern(self, P: str, S: str) -> bool:
        # (1) initialize data structuree
        S, d1, d2 = S.split(), {}, {}
        if len(P) != len(S):
            return False
        
        # (2) bijection with zip(P, S) --- one by one
        for p, s in zip(P, S):
            if p not in d1 and s not in d2:    # both not in
                d1[p], d2[s] = s, p
            elif p in d1 and s in d2:          # both in
                if (d1[p], d2[s]) != (s, p):
                    return False
            else:                              # not a bijection
                return False
            
        # (3) otherwise return True    
        return True
    
# Time: O(N)
# Space: O(N)