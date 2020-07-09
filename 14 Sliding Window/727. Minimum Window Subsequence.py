class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # (1) initialize two pointer
        sidx, slen = 0, len(S)
        tidx, tlen = 0, len(T)
        ret = ''
        
        # (2) expand window first and shrink it then
        while sidx < slen:
            if S[sidx] == T[tidx]:
                tidx += 1
                
                if tidx == tlen: # find the window
                    
                    # shrink to get the starting point
                    end = sidx + 1
                    
                    while tidx > 0:
                        if T[tidx - 1] == S[sidx]: 
                            tidx -= 1
                        sidx -= 1
                    sidx += 1
                    
                    if len(ret) == 0 or end - sidx < len(ret):
                        ret = S[sidx:end]
                    
            sidx += 1
        
        # (3) return result
        return ret
    
# Time: O(len(S)), since we need to traverse it twice at worst
# Space: O(1)